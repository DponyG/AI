from abc import ABC, abstractmethod
from node import Tree
from node import Node
from gameBoard import GameBoard
import random

class Agent(ABC):
    @abstractmethod
    def sense(self): pass

    @abstractmethod   
    def think(self): pass

    @abstractmethod    
    def move (self): pass

class Max(Agent):
    def __init__(self):
        self.allMoves = []
        self.type = "Max"
        self.root = None
      
    def sense(self, root):
        self.root = root
        self.tree = Tree(self.root)

        self.depth = self.tree.getTreeDepth()
        self.tree.miniMax(self.root, self.depth) 
        #self.tree.alphaBeta(self.root, self.depth, 0, 1) ## Give all 
      
    
    def think(self, node):
        self.allMoves = node.getChildren()
        for node in self.allMoves:
            if node.miniMax == 1:
                return node   
        return random.choice (self.allMoves)  
        
    def move(self, node):
        return self.think(node) 

class Min(Agent):
    def __init__(self):
        self.allMoves = []
        self.type = "Min"
        self.root = None
    
    def sense(self): pass ## I let Min and Max share the same tree to save some time.
    
    def think(self, node):
        self.allMoves = node.getChildren()
        for node in self.allMoves:
            if node.miniMax == 0:
                return node   
        return random.choice (self.allMoves)  
    
    def move(self, node):
        return self.think(node)

class Player(Agent):
    def __init__(self):
        self.type = "Player"
        self.currentMove = []
        self.possibleMoves = []
        self.gameBoard = GameBoard()
       
    def sense(self): pass

    def think(self, node):
        self.possibleMoves = self.gameBoard.createButtonMoves(node) ##Creates the moves
        return self.possibleMoves

    def move(self, node): 
        return(self.think(node))

class Random(Agent):
    def __init__(self):
        self.type = "Random"
        self.possibleMoves = []
       
    def sense(self): pass

    def think(self, node):
        self.allMoves = node.getChildren()
        return random.choice (self.allMoves)  

    def move(self, node): 
        return(self.think(node))
        
        



        







