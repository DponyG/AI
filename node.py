import math

class Node:

    def __init__(self, number):
       ## self.state = state
        self.children = []
        self.pile = [number]
        self.miniMax = 0
        self.depth = 0
        self.parent = None

    def getChildren(self):
        return self.children

    def printChildren(self):
        print(self.pile)
      
class Tree:  
    def __init__(self, node):
        self.treeDebth = 0
        self.generateTree(node)
      
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
          
    def generateTree(self, node):   
        if len(node.pile) == 1:
            self.generateBranches(node)
            self.treeDebth += 1
        if self.isLeafNode(node):
            for node in node.children:
                self.generateBranches(node)
                print(node.printChildren())
               ## node.printChildren(node)
                self.generateTree(node)
        else:
            if(node.depth % 2 == 1): 
                node.miniMax = 0    
            else:
                node.miniMax = 1

                   
    def isLeafNode(self, node):
        for number in node.pile:
            if number > 2:
                return True       
        return False
  
    def depth(self, root):  
        if root is None:
            return 0
        if root.children == []:
            return 1
        return 1 + max(self.depth(child) for child in root.children)

    def miniMax(self, root, depth):
        if depth == 0:
            return root.miniMax
        if depth%2 ==1: ##Max's turn
            maxEval = 0
            for node in root.children:       
                    eval = self.miniMax(node, depth -1)
                    maxEval = max(eval, maxEval)
            root.miniMax = maxEval             
            return maxEval    
        else:
            minEval = 1 
            for node in root.children:
                eval = self.miniMax(node, depth -1)
                minEval = min(eval, minEval)
            root.miniMax = minEval
            return minEval

    def printMiniMax(self, root):
        for node in root.children:
            print(minimax)

    def printTree(self, root):
        if self.isLeafNode(root):
            print(root.pile)
            print(root.miniMax)
        for node in root.children:
            print(node.pile)
            print(node.miniMax)
            self.printTree(node)
        
      