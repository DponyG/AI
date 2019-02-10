from node import Node
from node import Tree
from game import Game
from button import Button
from text import Text
import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode((400,300))
    button = Button((0,255,0), 75, 200, 100, 50, 'Start')
    exitButton = Button((0,255,0), 200, 200, 100, 50, 'Exit')
    text = Text()
    number = 3
    startGame = False

   

    ##game = Game(7)
  
    ##game = Game(100)
    while True:
        window.fill((255,255,255))
        text.drawPlayerText(window)
        text.drawPlayerScore(window)
        text.drawPile(window)
        button.draw(window, (0,0,0))
        exitButton.draw(window, (0,0,0))
           
        if startGame:
            game = Game(number)
            startGame = False
            number += 1

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.isOver(pos):
                    startGame = True
                if exitButton.isOver(pos):
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
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
  