from node import Node
from node import Tree
from text import Text
from button import Button
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
    def __init__(self, number, width, height):
      
        self.text = Text()
        self.pileNumber = number
        self.width = width
        self.height = height
        self.text = None
        self.root = None
        self.tree = None
        self.currentMove = None
        self.moveStorage = None
        self.gameBoard = None
        self.possibleMoves = None
        self.startGame(self.pileNumber)
   
        
    def startGame(self, number):
        print("Starting new Game with one higher number")
        self.root = Node()
        self.root.setPile(number)
        self.tree = Tree(self.root)
        print("Done Generating Tree")
        #print(self.tree.printChildren(self.root))
        self.depth = self.tree.depth(self.root)
        self.tree.miniMax(self.root, self.depth) ## Give all nodes 0 or 1
        self.moveStorage = []
        self.gameBoard = GameBoard(self.width, self.height)
        self.playerVsAiMoveList(self.root)
        
    def playerVsAiMoveList(self, node):
        self.currentMove = node
        self.changePileText(node)
        self.possibleMoves = self.gameBoard.createButtonMoves(self.currentMove) ##Creates the moves
    
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

    def getMoves (self):
        return self.possibleMoves

    def printStorage(self):
        for move in self.moveStorage:
            print(move)




    

    

                
        

            
            
        
        





        
    


   




    
    
    
