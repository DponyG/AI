import pygame

class Text:
    def __init__(self):
        self.black = [0,0,0]
        self.font = pygame.font.SysFont('comicsans', 30)
        self.maxPlayer = self.font.render("Max Player", True, self.black)
        self.minPlayer = self.font.render("Min Player", True, self.black)

    
    def drawPlayerText(self, window):
        window.blit(self.maxPlayer,( 25, 50 ))
        window.blit(self.minPlayer,( 25, 100))


