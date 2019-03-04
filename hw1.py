
import pygame
from game import Game
from node import Node
from button import Button
from agent import Player
from agent import Max
from agent import Min
from agent import Random
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
    button = Button((0,255,0), 25, 350, 100, 50, 'PlayerVsMax') # need to change this name
    stop = Button((0,255,0), 50, 200,100,50, 'Stop')
    minVsMax = Button((0,255,0), 25,400,100,50, 'MinVsMax')
    randomVsMax = Button((0,255,0),25, 450, 100,50, 'RandomVsMax')
    exitButton = Button((0,255,0), 25, 500, 100, 50, 'Exit')
    text = Text()
    number = 33
    newGamePlayer = False
    newGameMiniMax = False
    newGameRandomVsMax = False
    isPlaying = False
    startGameMiniMax = False
    startGameRandomVsMax = False
    moveList = []

    while True:
        window.fill((255,255,255))
        text.drawPlayerText(window)
        text.drawPlayerScore(window)
        text.drawNumber(window)
        text.drawGamePile(window)
        exitButton.draw(window, (0,0,0))
        minVsMax.draw(window, (0,0,0))
        button.draw(window, (0,0,0))
        randomVsMax.draw(window, (0,0,0))
        stop.draw(window, (0,0,0))
        

       
           
        if newGamePlayer:
            root = Node()
            text.setNum(number)
            root.setPile(number)
            text.changeGamePile(root.pile)
            player = Player()
            maxi = Max()
            game = Game(player, maxi, root)
            moveList = game.getPlayerMoves()
            newGamePlayer = False
            isPlaying = True
            number -=1
        
        if newGameMiniMax:
            if startGameMiniMax: ## Because it is automated
                root = Node()
                number = randint(6,20)
                root.setPile(number)
                text.setNum(number)
                maxi = Max()
                mini = Min()
                game = Game(mini, maxi, root)
                currentMoveMini = game.getCurrentMove() 
                startGameMiniMax = False
            else:
                    print(currentMoveMini.pile)        

                    if currentMoveMini.isLeaf():           # Possible null reference here
                        print("Mini Has Won")
                        Text.agentOneStatic()
                        startGameMiniMax = True
                    else:
                        currentMoveMaxi = game.setMoves(currentMoveMini, maxi)
                    print(currentMoveMaxi.pile)
                
                    if currentMoveMaxi.isLeaf():
                        print("Max Has Won")
                        Text.agentTwoStatic()
                        startGameMiniMax = True
                    else:
                        currentMoveMini = game.setMoves(currentMoveMaxi, mini)

        if newGameRandomVsMax:
            if startGameRandomVsMax:
                root = Node()
                number = randint(10,25)
                root.setPile(number)
                text.setNum(number)
                rand = Random()
                maxi = Max()
                game = Game(rand, maxi, root)
                currentMoveRand = game.getCurrentMove()  
                startGameRandomVsMax = False
            else:
                print(currentMoveRand.pile, currentMoveRand.miniMax)    # Possible null reference here
                if currentMoveRand.isLeaf():   
                    print("Random Has Won")
                    Text.agentOneStatic()
                    startGameRandomVsMax = True
                else:
                    currentMoveMaxi = game.setMoves(currentMoveRand, maxi)
                    print(currentMoveMaxi.pile)
                    if currentMoveMaxi.isLeaf():
                        print("Max Has Won")
                        Text.agentTwoStatic()
                        startGameRandomVsMax = True
                    else:
                        currentMoveRand = game.setMoves(currentMoveMaxi, rand)
            
        
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
                            newGamePlayer = True
                        else:
                            currentMoveAi = game.setMoves(currentMovePlayer, maxi)
                            print(currentMoveAi.pile)
                        if currentMoveAi.isLeaf():
                            Text.agentTwoStatic()
                            print("AI has Won")
                            newGamePlayer = True
                        else:
                            currentMovePlayer = game.setMoves(currentMoveAi, player)
                        text.changeGamePile(currentMovePlayer.pile)  
                        moveList = game.getPlayerMoves()
                if not isPlaying:
                    if button.isOver(pos):
                        button.setColor((211,211,211))
                        minVsMax.setColor((211,211,211))
                        randomVsMax.setColor((211,211,211))
                        text.setAgents("Player", "Max")
                        text.setAgentScore(0,0)
                        isPlaying = True
                        newGamePlayer = True
                    if minVsMax.isOver(pos) :
                        button.setColor((211,211,211))
                        minVsMax.setColor((211,211,211))
                        randomVsMax.setColor((211,211,211))
                        text.setAgents("Min", "Max")
                        text.setAgentScore(0,0)
                        newGameMiniMax = True
                        startGameMiniMax = True
                        isPlaying = True
                    if randomVsMax.isOver(pos) :
                        button.setColor((211,211,211))
                        minVsMax.setColor((211,211,211))
                        randomVsMax.setColor((211,211,211))
                        text.setAgents("Random", "Max")
                        text.setAgentScore(0,0)
                        newGameRandomVsMax = True
                        startGameRandomVsMax = True
                        isPlaying = True
                if stop.isOver(pos):
                    button.setColor((0,255,0))
                    minVsMax.setColor((0,255,0))
                    moveList.clear()
                    text.changeGamePile(None)
                    newGameMiniMax = False
                    newGamePlayer = False
                    newGameRandomVsMax = False
                    isPlaying = False
                    number = 33
                    
                if exitButton.isOver(pos):
                    pygame.quit()
     
            if event.type == pygame.MOUSEMOTION:
                if not isPlaying:
                    if button.isOver(pos):
                        button.color = (255,0,0)
                    else:     
                        button.color = (0,255,0)
                    if minVsMax.isOver(pos):
                        minVsMax.color = (255,0,0)
                    else:
                        minVsMax.color = (0,255,0)  
                    if randomVsMax.isOver(pos):
                        randomVsMax.color = (255,0,0)
                    else:
                        randomVsMax.color = (0,255,0)               
                for moves in moveList:
                    if(moves.isOver(pos)):
                        moves.color = (255,0,0)
                    else:
                        moves.color = (255,140,0) 
                if exitButton.isOver(pos):
                    exitButton.color = (255,0,0)
                else:     
                    exitButton.color = (0,255,0)
                if stop.isOver(pos):
                    stop.color = (255,0,0)
                else:     
                    stop.color = (0,255,0)   
            if event.type == pygame.QUIT: #For the X button in the window
                pygame.quit()

        pygame.display.update()
     
         
if __name__ == "__main__":
    main()
  