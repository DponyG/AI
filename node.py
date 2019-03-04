

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
        self.key = 0
        self.parent = None
        

    def copy(self, nodeIn):
        self.children = nodeIn.children
        self.pile = nodeIn.pile
        self.miniMax = nodeIn.miniMax
        self.depth = nodeIn.depth

    def getChildren(self):
        return self.children

    def printChildren(self):
        return
        print(self.pile)
    
    #only used for continuing the game
    def setPile(self, number):
        self.pile = [number]
    
    def isLeaf(self):
        for number in self.pile:
            if number > 2:
                return False       
        return True


        
    
      
class Tree:  
    def __init__(self, node):
        self.nodeCount = 0
        self.treeDepth = 0
        self.removeDuplicates = []
        self.lookUpTable = {}
        self.lookUpTable2 = {}
        self.generateTree(node)
    
    
    #  def GenerateBranches()
    #  Called recursivley from generateTree.
    #  Takes the old pile and splits it up into a new pile
    #  Count goes to number/2 to prevent recreating nodes
    #  for example it prevents 4 splitting into 1 3 and 3 1
    #  it the number is in the look up table it wont recalulate it

    def generateBranches(self, node):
        tup = tuple(node.pile) #This is because a list is not hashable.
        if tup in self.lookUpTable.keys():
            node.copy(self.lookUpTable[tup])
            return True
        else:
            for number in node.pile:
                count = int(number/2)+1
                for i in range(1,count):  
                    newPile = node.pile.copy()
                    newNum = number - i
                    checkNum = newNum+newNum  
                    if checkNum != number:
                        newNode = Node()
                        newNode.depth = node.depth + 1
                        if self.treeDepth < newNode.depth:
                            self.treeDepth = newNode.depth
                        newPile.remove(number)
                        newPile.append(newNum)
                        newPile.append(i)
                        newNode.pile = newPile.copy()
                        newNode.pile.sort()
                        node.pile.sort()
                        node.children.append(newNode)        
            self.lookUpTable[tup] = node
            return False
         
     
    #  Debugging function to find all the children
    def printChildren(self, node):
        if not self.isLeafNode(node):
            for child in node.children:
                print(node.pile, child.pile, "here")
                self.printChildren(child)
    
    #def GenerateTree(self, node)
    # Recursive Function. Base Case if its a lead node.
    # If base case add the approptiate minimax 0 = loss
    # for max 1 = loss for min.
     
    def generateTree(self, node):
       
        if len(node.pile) == 1:
            self.generateBranches(node)
        if not self.isLeafNode(node):
            node.pile.sort() 
            for node in node.children: 
                if self.generateBranches(node):
                    continue
                self.generateTree(node)       
        else:
            if node.depth % 2 == 0: 
                node.miniMax = 1
            else:
                node.miniMax = 0
                
   #  Actually redefined in node but I didn't want to remove it         
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
    
    def getTreeDepth(self):
        return self.treeDepth

    # def miniMax(self, root, depth)
    # Recursive MiniMax function that cycles
    # up from a leaf node. Alternating between min
    # and max based on the depth of tree 
    def miniMax(self, root, depth):
        tup = tuple(root.pile)
        if depth == 0:
            return root.miniMax
        if tup in self.lookUpTable2.keys():
            root.miniMax = self.lookUpTable2[tup]
            return root.miniMax

        if len(root.pile) % 2 == 0: ##Max's turn
            root.miniMax = 0
            for node in root.children:       
                eval = self.miniMax(node, depth -1)
                root.miniMax = max(root.miniMax, eval)
            self.lookUpTable2[tup] = root.miniMax      
            return root.miniMax    
        else:
            root.miniMax = 1 
            for node in root.children:
                eval = self.miniMax(node, depth -1 )
                root.miniMax = min(root.miniMax, eval)
            self.lookUpTable2[tup] = root.miniMax 
            return root.miniMax
    
    #  def alphaBeta(self, root, depth, alpha, beta)
    #  Recursive AlphaBeta function that cycles
    #  up from a leaf node. Alternating between min
    #  and max based on the depth of tree slow because
    #  not using look up table.
    def alphaBeta(self, root, depth, alpha, beta):
        tup = tuple(root.pile)
        if depth == 0:
            return root.miniMax
        if len(root.pile) % 2 == 0: ##Max's turn
            root.miniMax = 0
            for node in root.children:       
                eval = self.alphaBeta(node, depth -1, alpha, beta)
                root.miniMax = max(root.miniMax, eval)
                alpha = max(alpha, root.miniMax)
                if beta <= alpha:
                    break
            return root.miniMax    
        else:
            root.miniMax = 1 
            for node in root.children:
                eval = self.alphaBeta(node, depth -1, alpha, beta )
                root.miniMax = min(root.miniMax, eval)
                beta = min(beta, root.miniMax)
                if beta <= alpha:
                    break
            return root.miniMax

            