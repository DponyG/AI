from node import Node
from node import Tree
import random

class Game:
    def __init__(self, number):
        self.number = number
        self.root = Node(number)
        self.tree = Tree(self.root)
        self.depth = self.tree.depth(self.root)
        self.tree.miniMax(self.root, self.depth) ## Give all nodes 0 or 1
        self.moveStorage = []
        self.getMoveList(self.root, False)
     
    def getMoveList(self, node, maximizingPlayer):
        self.moveStorage.append(node.pile)
        if not self.tree.isLeafNode(node):
            self.printStorage()
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

    



    

    

                
        

            
            
        
        





        
    


   




    
    
    
