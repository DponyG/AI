
import pygame
import random
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
        self.removeDuplicates = []
        #self.removeDuplicates.append(node)
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
                    newPile.sort()
                    newNode.pile = newPile.copy()
                   # newNode = self.checkDuplicates(newNode)
                    if not self.checkDuplicateNodes(node, newNode):
                        node.children.append(newNode)

    def checkDuplicateNodes(self, parent, child):
        for node in parent.children:
            if child.pile == node.pile:
                print("Here")
                return True
        return False

    # def checkDuplicates(self, node):
    #     for duplicateNode in self.removeDuplicates:
    #        # print(node.pile, duplicateNode.pile)
    #         if node.pile == duplicateNode.pile:
    #             return duplicateNode    
    #     self.removeDuplicates.append(node)
    #     return node

        
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
           # print(root.pile, "depth")
            return root.miniMax
        if len(root.pile) % 2 == 0: ##Max's turn
            root.miniMax = 0
            for node in root.children:       
                    eval = self.miniMax(node, depth -1)
                    root.miniMax = max(root.miniMax, eval) 
                    #print(node.pile , node.miniMax, root.pile )  
           # print(root.pile , root.miniMax )        
            return root.miniMax    
        else:
            root.miniMax = 1 
            for node in root.children:
                eval = self.miniMax(node, depth -1 )
                root.miniMax = min(root.miniMax, eval)
               # print(node.pile , node.miniMax, root.pile ) 
           # print(root.pile , root.miniMax )   
           # print(root.pile , root.miniMax )   
            return root.miniMax

    # def printMiniMax(self, root):
    #     if not self.isLeafNode:
    #         for node in root.children:
    #             print("here")
    #             print(node.pile)
    #             print(node.minimax)
    #             self.printMiniMax(node)
            
        

#  file: text.py
#  Author: Samuel Grenon
#  Class: Text
#  Handles the Text in pygame

class Text:
    maxScore = 0 # Static Variable used to increment the score
    minScore = 0
    num = 3
    def __init__(self):
        self.black = [0,0,0]
        self.green = [0,128,0]
        self.purple = [128,0,128]
        self.font = pygame.font.SysFont('comicsans', 30)
        self.maxPlayer = self.font.render("Max Player", True, self.black)
        self.minPlayer = self.font.render("Min Player", True, self.black)
       

    
    def drawPlayerText(self, window):
        window.blit(self.maxPlayer,( 25, 50 ))
        window.blit(self.minPlayer,( 25, 100))

    def drawPlayerScore(self,window):
        maxPlayerScore = self.font.render(str(Text.maxScore), True, self.green)
        minPlayerScore = self.font.render(str(Text.minScore), True, self.green)
        window.blit(maxPlayerScore,(250,50))
        window.blit(minPlayerScore,(250,100))
    
    
    def drawPile(self,window):
        pileStr = "Current number " + str(Text.num)
        pile = self.font.render(pileStr, True, self.purple)
        window.blit(pile,(125, 150))
    
    @staticmethod
    def incNum():
        Text.num += 1

    @staticmethod
    def maxStatic():
        Text.maxScore += 1

    @staticmethod
    def minStatic():
        Text.minScore += 1
       
       
    
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


#  file: Button.py
#  Author: Samuel Grenon
#  Class: Button
#  Handles the Buttons in Pygame

class Button:
  
    active = True #Static Variable to disable the button. Dosen't really work as intended
  
    def __init__(self, color, x,y,width,height, text=''): 
        self.color = color 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.text = text
        self.textColor = None

    def setColor(self, color):
        self.color = color

    def setText(self, text):
        self.text = text


    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
            
        if self.text != '': 
            font = pygame.font.SysFont('comicsans', 60) 
            text = font.render(self.text, 1, (0,0,0)) 
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos): #Pos is the mouse position or a tuple of (x,y) 
        if pos[0] > self.x and pos[0] < self.x + self.width: 
            if pos[1] > self.y and pos[1] < self.y + self.height: 
                return True 
        return False

    
    @staticmethod
    def setActive(status):
        Button.active = status

    @staticmethod
    def isActive():
        return Button.active
        
        
        
        
#  file: main.py
#  Author: Samuel Grenon
#  Class: main
#  Handles the window and the game loop

def main():
    pygame.init()
    window = pygame.display.set_mode((400,300))
    pygame.display.set_caption('NIM')
    button = Button((0,255,0), 75, 200, 100, 50, 'Start')
    exitButton = Button((0,255,0), 200, 200, 100, 50, 'Exit')
    text = Text()
    number = 3
    startGame = False

   







    while True:
        window.fill((255,255,255))
        text.drawPlayerText(window)
        text.drawPlayerScore(window)
        text.drawPile(window)
        button.draw(window, (0,0,0))
        exitButton.draw(window, (0,0,0))
           
        if startGame:
            game = Game(number)
            startGame = False
            number += 1

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.isOver(pos):
                    startGame = True
                if exitButton.isOver(pos):
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                    if button.isOver(pos):
                        button.color = (255,0,0)
                    else:     
                        button.color = (0,255,0)

                    if exitButton.isOver(pos):
                        exitButton.color = (255,0,0)
                    else:     
                        exitButton.color = (0,255,0)       
            if event.type == pygame.QUIT: #For the X button in the window
                pygame.quit()

        pygame.display.update()
     
         
if __name__ == "__main__":
    main()
  