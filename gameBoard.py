from button import Button

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.placementWidth = width*.75
        self.placementHeight = height*.15
        self.count = 0
  
    def createButtonMoves(self, node):
        xVal = 0
        yVal = 0
        buttonArray = []
        self.count = 0
        if len(node.children) == 0:
            print("empty list")
        for children in node.children:
            print(children.pile, node.pile, "game")
            button = Button((255,140,0), self.placementWidth, self.placementHeight + yVal, 100, 50, str(children.pile), children)  
            yVal += 50   
            buttonArray.append(button)
        return buttonArray

    # def getMoves(self):
    #     return self.buttonArray