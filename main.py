from node import Node
from node import Tree
from game import Game
from button import Button
from text import Text
import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode((400,300))
    window.fill((255,255,255))
    button = Button((0,255,0), 150, 200, 100, 50, 'Start')
    text = Text()
    startGame = False


    ##game = Game(7)
  
    ##game = Game(100)
    while True:
        button.draw(window, (0,0,0))
        text.drawPlayerText(window)
       
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.isOver(pos):
                    print('clicked the button')
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                if button.isOver(pos):
                    button.color = (255,0,0)
                else:
                    button.color = (0,255,0)
        pygame.display.update()
       

   
    
if __name__ == "__main__":
    main()
  