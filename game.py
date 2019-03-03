from node import Node
from node import Tree
from text import Text
from button import Button
from agent import Max
from agent import Player
from gameBoard import GameBoard
import random

#  file: game.py
#  Author: Samuel Grenon
#  Class: Game
#  Handles some Game Logic. Min goes first
#  and will chose the first 0 if there is no
#  0 available it will chose a random viable node.
#  max is the same way, however will choose a 1 if possble.

class Game:
    def __init__(self, agent_one, agent_two, node):
        
        self.root = node
        self.agent_one = agent_one
        self.agent_two = agent_two
        self.currentMove = None
        self.moveStorage = None
        self.playerMoves = []
        self.startGame()
   
        
    def startGame(self):
        self.initiateSenses(self.agent_one)
        self.initiateSenses(self.agent_two)
        self.moveStorage = []
        self.setMoves(self.root, self.agent_one)
       
    def setMoves(self, node, agent):
        self.currentMove = node
        if agent.type == "Player":
                self.playerMoves = agent.move(self.currentMove)
                return self.currentMove
        if agent.type == "Max":         
                self.currentMove = agent.move(self.currentMove)
                return self.currentMove
        if agent.type == "Min":         
                self.currentMove = agent.move(self.currentMove)
                return self.currentMove
            
    def initiateSenses(self, agent):
        if agent.type == "Max":
            agent.sense(self.root)
         
  
    def playerThink(self, node):
        self.currentMove = node
        if self.tree.isLeafNode(self.currentMove):
            print("You have Won with the ending pile :" + str(self.currentMove.pile))
            Text.playerStatic()
            Text.incNum()
            self.playerVsAiMoveList(self.currentMove)
        else:
            print(self.currentMove.pile)
            self.playerVsAiMoveList(self.currentMove)
            self.computerThink(self.currentMove)
        
    
    #For Player vs Ai MiniMax
    def computerThink(self,node):
       # print(self.currentMove.pile)
        self.currentMove = self.setMove(node, True)
        if self.tree.isLeafNode(self.currentMove):
            print("The computer has Won with the ending pile :" + str(self.currentMove.pile))
            Text.computerStatic()
            Text.incNum()
            self.playerVsAiMoveList(self.currentMove)
        else:
            print(self.currentMove.pile)
            self.playerVsAiMoveList(self.currentMove)
    
    def changePileText(self, node):
        Text.changeGamePile(node.pile)
        
    #Will be used for Ai vs Ai for when the mode selected is minimax
    #currently not used.
    def getMoveList(self, node, maximizingPlayer):
        self.moveStorage.append(node.pile)
        if self.tree.isLeafNode(node):
            if maximizingPlayer:
                print("Max player lost!! See the move list is below")
                self.printStorage()
                Text.maxStatic()
                Text.incNum()
              
                                     
            else :
                print("Min player lost!! See the move list is below")
                self.printStorage()
                Text.minStatic()
                Text.incNum()
              
            
            return -1

            
        if maximizingPlayer:
            node = self.setMove(node, maximizingPlayer)
            self.getMoveList(node, False )
        else:
             node = self.setMove(node, maximizingPlayer)
             self.getMoveList(node, True)
             

    def setMove(self, node, maximizingPlayer):
        allMoves = node.getChildren()
        if maximizingPlayer:
            for node in allMoves:
                if node.miniMax == 1:
                    return node   
            return random.choice (allMoves)  
        else:
            for node in allMoves:
                if node.miniMax == 0:
                    return node
            return random.choice (allMoves)     

    def getPlayerMoves (self):
        return self.playerMoves
        
    def getCurrentMove(self):
        return self.currentMove

    def printStorage(self):
        for move in self.moveStorage:
            print(move)




    

    

                
        

            
            
        
        





        
    


   




    
    
    
