from node import Node
from node import Tree
from text import Text
from button import Button
import random

#  file: game.py
#  Author: Samuel Grenon
#  Class: Game
#  Handles some Game Logic. Min goes first
#  and will chose the first 0 if there is no
#  0 available it will chose a random viable node.
#  max is the same way, however will choose a 1 if possble.

class Game:
    def __init__(self, number):
      
        self.text = Text()
        self.pileNumber = number
        self.text = None
        self.root = None
        self.tree = None
        self.moveStorage = None
        self.startGame(self.pileNumber)
        
    
    def startGame(self, number):
        print("Starting new Game with one higher number")
        self.root = Node()
        self.root.setPile(number)
        self.tree = Tree(self.root)
        print("Dont Generating Tree")
        self.depth = self.tree.depth(self.root)
        self.tree.miniMax(self.root, self.depth) ## Give all nodes 0 or 1
        self.moveStorage = []
        self.getMoveList(self.root, False)
    


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

    def printStorage(self):
        for move in self.moveStorage:
            print(move)

    



    

    

                
        

            
            
        
        





        
    


   




    
    
    
