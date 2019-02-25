import pygame

#  file: text.py
#  Author: Samuel Grenon
#  Class: Text
#  Handles the Text in pygame

class Text:
    playerScore = 0 # Static Variable used to increment the score
    computerScore = 0
    num = 5
    pile = []
    previousPile = []
    def __init__(self):
        self.black = [0,0,0]
        self.green = [0,128,0]
        self.purple = [128,0,128]
        self.font = pygame.font.SysFont('comicsans', 30)
        self.player = self.font.render("Player", True, self.black)
        self.computer= self.font.render("Computer", True, self.black)
        self.allPossibleMoves= self.font.render("All Possible Moves :", True, self.black)
       

    
    def drawPlayerText(self, window):
        window.blit(self.player,( 25, 50 ))
        window.blit(self.computer,( 25, 100))
    
    def drawAllMoves(self,window):
        window.blit(self.allPossibleMoves,(500,125))

    def drawPlayerScore(self,window):
        maxPlayerScore = self.font.render(str(Text.playerScore), True, self.green)
        minPlayerScore = self.font.render(str(Text.computerScore), True, self.green)
        window.blit(maxPlayerScore,(250,50))
        window.blit(minPlayerScore,(250,100))
    
    
    def drawNumber(self,window):
        pileStr = "Current number : "
        pileValue = str(Text.num)
        pileStr = self.font.render(pileStr, True, self.black)
        pileValue = self.font.render(pileValue, True, self.green)
        window.blit(pileStr,(25, 150))
        window.blit(pileValue,(250, 150))
        pileStr = self.font.render
        pileValue = self.font.render
    
    def drawGamePile(self,window):
        pileStr = "Current Pile :"
        pileValue = str(Text.pile)
        pileStr = self.font.render(pileStr, True, self.black)
        pileValue = self.font.render(pileValue, True, self.green)
        window.blit(pileStr,(25, 200))
        window.blit(pileValue,(250, 200))
        pileStr = self.font.render
        pileValue = self.font.render
    
    def drawPreviousPile(self, window):
        pileStr = "Previous Pile :"
        pileValue = str(Text.previousPile)
        pileStr = self.font.render(pileStr, True, self.black)
        pileValue = self.font.render(pileValue, True, self.green)
        window.blit(pileStr,(25, 250))
        window.blit(pileValue,(250, 250))
        pileStr = self.font.render
        pileValue = self.font.render
    


    
    @staticmethod
    def incNum():
        Text.num += 1

    @staticmethod
    def changeGamePile(pile):
        Text.previousPile = Text.pile
        Text.pile = pile
    
    @staticmethod
    def computerStatic():
        Text.computerScore += 1

    @staticmethod
    def playerStatic():
        Text.playerScore += 1
       
       
    
   
