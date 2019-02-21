import math


#  file: node.py
#  Author: Samuel Grenon
#  Class: Node, Tree
#  Generates the minimax of all possible moves

class Node:

    def __init__(self):
        self.children = []
        self.pile = []
        self.miniMax = 0
        self.depth = 0
        self.parent = None

    def getChildren(self):
        return self.children

    def printChildren(self):
        print(self.pile)
    
    #only used for continuing the game
    def setPile(self, number):
        self.pile = [number]
        
    
      
class Tree:  
    def __init__(self, node):
        self.treeDebth = 0
        self.generateTree(node)
    
    #def GenerateBranches()
    #Called recursivley from generateTree.
    #Takes the old pile and splits it up into a new pile
    #Count goes to number/2 to prevent recreating nodes
    #for example it prevents 4 splitting into 1 3 and 3 1

    def generateBranches(self, node):  
        for number in node.pile:
            count = int(number/2)
            for i in range(1,count+1):  
                newPile = node.pile.copy()
                newNum = number - i
                checkNum = newNum+newNum  
                if checkNum != number:
                    newNode = Node()
                    newNode.parent = node
                    newNode.depth = node.depth + 1
                    newPile.remove(number)
                    newPile.append(newNum)
                    newPile.append(i)
                    newNode.pile = newPile.copy()
                    node.children.append(newNode)

    #def GenerateTree(self, node)
    # Recursive Function. Base Case if its a lead node.
    # If base case add the approptiate minimax 0 = loss
    # for max 1 = loss for min.
     
    def generateTree(self, node):   
        if len(node.pile) == 1:
            self.generateBranches(node)
            self.treeDebth += 1
        if not self.isLeafNode(node):
            for node in node.children:
                self.generateBranches(node)
                self.generateTree(node)
        else:
            if(node.depth % 2 == 1): 
                node.miniMax = 0
            else:
                node.miniMax = 1
                

                   
    def isLeafNode(self, node):
        for number in node.pile:
            if number > 2:
                return False       
        return True
  
    #def GenerateTree()
    #Recursive function required to calculate
    #the depth of the tree. Needed for minimax
    def depth(self, root):  
        if root is None:
            return 0
        if root.children == []:
            return 0
        return 1 + max(self.depth(child) for child in root.children)

    # def miniMax(self, root, depth)
    # Recursive MiniMax function that cycles
    # up from a leaf node. Alternating between min
    # and max based on the depth of tree 
    def miniMax(self, root, depth):
        if depth == 0:
            for node in root.children:
                if node.miniMax < root.miniMax:
                    root.miniMax = node.miniMax
            return root.miniMax
        if depth%2 == 1: ##Max's turn
            maxEval = 0
            for node in root.children:       
                    eval = self.miniMax(node, depth -1)
                    root.miniMax = max(eval, maxEval)  
            print(root.pile , root.miniMax )        
            return root.miniMax    
        else:
            minEval = 1 
            for node in root.children:
                eval = self.miniMax(node, depth -1)
                root.miniMax = min(eval, minEval)
            print(root.pile , root.miniMax )   
            return root.miniMax

    # def printMiniMax(self, root):
    #     if not self.isLeafNode:
    #         for node in root.children:
    #             print("here")
    #             print(node.pile)
    #             print(node.minimax)
    #             self.printMiniMax(node)
            
        

    


        
      