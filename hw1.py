
import pygame
from game import Game
from node import Node
from button import Button
from agent import Player
from agent import Max
from agent import Min
from text import Text
from random import randint



   
#  file: main.py
#  Author: Samuel Grenon
#  Class: main
#  Handles the window and the game loop

def main():
    pygame.init()
    height = 768
    width = 1024
    window = pygame.display.set_mode((1024,768))
    pygame.display.set_caption('NIM')
    button = Button((0,255,0), 25, 350, 100, 50, 'PlayerVsMax')
    stop = Button((0,255,0), 50, 150,100,50, 'Stop')
    minVsMax = Button((0,255,0), 25,400,100,50, 'MinVsMax')
    randomVsMax = Button((0,255,0),25, 450, 100,50, 'RandomVsMax')
    exitButton = Button((0,255,0), 150, 350, 100, 50, 'Exit')
    text = Text()
    number = 5
    newGamePlayer = False
    newGameMiniMax = False
    isPlaying = False
    startGameMiniMax = True
    moveList = []

    while True:
        window.fill((255,255,255))
        text.drawPlayerText(window)
        text.drawPlayerScore(window)
        text.drawNumber(window)
        text.drawGamePile(window)
        text.drawAllMoves(window)
        exitButton.draw(window, (0,0,0))
        minVsMax.draw(window, (0,0,0))
        button.draw(window, (0,0,0))
        stop.draw(window, (0,0,0))
        

       
           
        if newGamePlayer:
            root = Node()
            root.setPile(number)
            text.changeGamePile(root.pile)
            player = Player()
            maxi = Max()
            game = Game(player, maxi, root)
            moveList = game.getPlayerMoves()
            newGamePlayer = False
            isPlaying = True
            number += 1
        
        if newGameMiniMax:
            if startGameMiniMax: ## Because it is automated
                root = Node()
                root.setPile(5)
                maxi = Max()
                mini = Min()
                game = Game(mini, maxi, root)
                currentMoveMini = game.setMove(root, mini)
                startGameMiniMax = False
            else:
                    if currentMoveMini.isLeaf():
                        print("Max Has Won")
                        startGameMiniMax = True
                    else:
                        currentMoveMaxi = game.setMoves(currentMoveMini, maxi)
                    if currentMoveMaxi.isLeaf():
                        print("Min Has Won")
                        startGameMiniMax = True
                    else:
                        currentMoveMini = game.setMoves(currentMoveMaxi, mini)
                        
        for moves in moveList:
            moves.draw(window, (0,0,0))
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for moves in moveList:
                    if(moves.isOver(pos)):
                        currentMovePlayer = moves.getNode()
                        text.changeGamePile(currentMovePlayer.pile)
                        print(currentMovePlayer.pile)
                        if currentMovePlayer.isLeaf():
                            Text.agentOneStatic()
                            print("You have Won")
                            Text.incNum()
                            newGamePlayer = True
                        else:
                            currentMoveAi = game.setMoves(currentMovePlayer, maxi)
                            print(currentMoveAi.pile)
                        if currentMoveAi.isLeaf():
                            Text.agentTwoStatic()
                            print("AI has Won")
                            Text.incNum()
                            newGamePlayer = True
                        else:
                            currentMovePlayer = game.setMoves(currentMoveAi, player)  
                        moveList = game.getPlayerMoves()
                if button.isOver(pos) and not isPlaying:
                    button.setColor((211,211,211))
                    minVsMax.setColor((211,211,211))
                    text.setAgents("Player", "Max")
                    isPlayer = True
                    newGamePlayer = True
                if exitButton.isOver(pos):
                    pygame.quit()
                if minVsMax.isOver(pos) and not isPlaying:
                    button.setColor((211,211,211))
                    minVsMax.setColor((211,211,211))
                    text.setAgents("Min", "Max")
                    text.setAgentScore(0,0)
                    newGameMiniMax = True
                    isPlaying = True
                
            if event.type == pygame.MOUSEMOTION:
                if not isPlaying:
                    if button.isOver(pos):
                        button.color = (255,0,0)
                    else:     
                        button.color = (0,255,0)   
                for moves in moveList:
                    if(moves.isOver(pos)):
                        moves.color = (255,0,0)
                    else:
                        moves.color = (255,140,0) 
                if exitButton.isOver(pos):
                    exitButton.color = (255,0,0)
                else:     
                    exitButton.color = (0,255,0)       
            if event.type == pygame.QUIT: #For the X button in the window
                pygame.quit()

        pygame.display.update()
     
         
if __name__ == "__main__":
    main()
  