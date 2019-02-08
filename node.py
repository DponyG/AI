class Node:
    def __init__(self):
       ## self.state = state
        self.children = []
        self.pile = [7]
        self.minimax = 0 
        self.debth = 0 
        self.parent = None

    def addChild(self, obj): 
        self.children.append(obj)
    
    @property
    def setPile(pile):
        self.pile = pile

    def printChildren(self, node):
        print(node.pile)
        print(node.debth)
    
       

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
                    newNode.debth = node.debth + 1
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
                node.printChildren(node)
                self.generateTree(node)
           
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
       
    
            
                 
       

      
           
        

        
    
  
            

        

        
        
    


        
            


    
                

   




                    
        



