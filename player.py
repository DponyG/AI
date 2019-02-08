import pygame

class Player:

    def __init__(self):
        self.card = pygame.Rect(400,300,10,10)

    @property
    def getHand(self):
        return self.card
