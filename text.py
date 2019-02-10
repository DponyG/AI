import pygame

class Text:
    maxScore = 0
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
       
       
    
   
