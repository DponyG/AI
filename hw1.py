
import pygame
from game import Game
from button import Button
from text import Text



   
#  file: main.py
#  Author: Samuel Grenon
#  Class: main
#  Handles the window and the game loop

def main():
    pygame.init()
    height = 768
    width = 1024
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption('NIM')
    button = Button((0,255,0), 25, 350, 100, 50, 'Start')
    exitButton = Button((0,255,0), 150, 350, 100, 50, 'Exit')
    text = Text()
    number = 5
    startGame = False
    moveList = []

    while True:
        window.fill((255,255,255))
        text.drawPlayerText(window)
        text.drawPlayerScore(window)
        text.drawNumber(window)
        text.drawGamePile(window)
        text.drawPreviousPile(window)
        text.drawAllMoves(window)
        button.draw(window, (0,0,0))
        exitButton.draw(window, (0,0,0))
           
        if startGame:
            game = Game(number, width, height)
            moveList = game.getMoves()
            startGame = False
            number += 1

        for moves in moveList:
            moves.draw(window, (0,0,0))
        
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for moves in moveList:
                    if(moves.isOver(pos)):
                        game.playerThink(moves.getNode())
                        moveList = game.getMoves()
                if button.isOver(pos):
                    startGame = True
                if exitButton.isOver(pos):
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                for moves in moveList:
                    if(moves.isOver(pos)):
                        moves.color = (255,0,0)
                    else:
                        moves.color = (255,140,0)

                if button.isOver(pos):
                        button.color = (255,0,0)
                else:     
                    button.color = (0,255,0)
                    
                if exitButton.isOver(pos):
                    exitButton.color = (255,0,0)
                else:     
                    exitButton.color = (0,255,0)       
            if event.type == pygame.QUIT: #For the X button in the window
                pygame.quit()

        pygame.display.update()
     
         
if __name__ == "__main__":
    main()
  