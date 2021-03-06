import pygame

#  file: Button.py
#  Author: Samuel Grenon
#  Class: Button
#  Handles the Buttons in Pygame

class Button:
  
    active = True #Static Variable to disable the button. Dosen't really work as intended
  
    def __init__(self, color, x,y,width,height, text='', node = None): 
        self.color = color 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.text = text
        self.textColor = None
        self.node = node

    def setColor(self, color):
        self.color = color

    def setText(self, text):
        self.text = text


    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
                
        if self.text != '': 
            font = pygame.font.SysFont('comicsans', 15) 
            text = font.render(self.text, 1, (0,0,0)) 
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos): #Pos is the mouse position or a tuple of (x,y) 
        if pos[0] > self.x and pos[0] < self.x + self.width: 
            if pos[1] > self.y and pos[1] < self.y + self.height: 
                return True 
        return False
    
    def getNode(self):
        return self.node

    def printTest(self):
        print(self.node.pile)

    
    @staticmethod
    def setActive(status):
        Button.active = status

    @staticmethod
    def isActive():
        return Button.active
        
        
        
        