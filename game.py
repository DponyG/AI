from node import Node
from node import Tree
from text import Text
from button import Button
import random

class Game:
    def __init__(self, number):
        # self.text = Text()
        # self.root = Node()
        # self.tree = Tree(self.root)
        # self.depth = self.tree.depth(self.root)
        # self.tree.miniMax(self.root, self.depth) ## Give all nodes 0 or 1
        # self.moveStorage = []
        # self.getMoveList(self.root, False)
        button = Button((0,255,0), 150, 200, 100, 50, 'Start') # set buttons status to true when we hit a leaf node
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

    



    

    

                
        

            
            
        
        





        
    


   




    
    
    
