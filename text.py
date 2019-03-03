import pygame

#  file: text.py
#  Author: Samuel Grenon
#  Class: Text
#  Handles the Text in pygame

class Text:
    agentOneScore = 0 # Static Variable used to increment the score
    agentTwoScore = 0
    num = 5
    pile = []
    previousPile = []
    def __init__(self):
        self.black = [0,0,0]
        self.green = [0,128,0]
        self.purple = [128,0,128]
        self.font = pygame.font.SysFont('comicsans', 30)
        self.agentOne = self.font.render("Agent 1", True, self.black)
        self.agentTwo= self.font.render("Agent 2", True, self.black)
        self.allPossibleMoves= self.font.render("All Possible Moves :", True, self.black)
       

    def setAgents(self, type1, type2):
        self.agentOne = self.font.render(type1, True, self.black)
        self.agentTwo = self.font.render(type2, True, self.black)
    
    
    def drawPlayerText(self, window):
        window.blit(self.agentOne,( 25, 50 ))
        window.blit(self.agentTwo,( 25, 100))
    
    def drawAllMoves(self,window):
        window.blit(self.allPossibleMoves,(500,125))

    def drawPlayerScore(self,window):
        maxPlayerScore = self.font.render(str(Text.agentOneScore), True, self.green)
        minPlayerScore = self.font.render(str(Text.agentTwoScore), True, self.green)
        window.blit(maxPlayerScore,(250,50))
        window.blit(minPlayerScore,(250,100))
    
    
    def drawNumber(self,window):
        pileStr = "Starting number : "
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
        window.blit(pileStr,(25, 0))
        window.blit(pileValue,(400, 0))
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
    def agentTwoStatic():
        Text.agentTwoScore += 1

    @staticmethod
    def agentOneStatic():
        Text.agentOneScore += 1
    
    @staticmethod
    def setAgentScore(score1, score2):
        Text.agentOneScore = score1
        Text.agentTwoScore = score2

   
       
       
    
   
