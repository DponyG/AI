from node import Node
from node import Tree

class Game:
    def __init__(self, number):
        self.number = number
        self.root = Node()
        self.tree = Tree(self.root)
        self.depth = self.tree.depth(self.root)
        self.tree.miniMax(self.root, self.depth) ## Give all nodes 0 or 1
        self.getMoveMinimax(self.root)
        self.moveStorage = None
        
    def getMoveMinimax(self, node, maximizingPlayer):
        possibleMoves = self.root.getChildren()
        for node in possibleMoves:
            if maximizingPlayer:
                if node.miniMax == 1:
                    print("made it")
                    self.root = node
                    self.moveStorage.append(self.root.pile)
                    break    
        for child in self.root.children:
            print(child.pile)

            
            
        
        





        
    


   




    
    
    
