from button import Button

class GameBoard:
    def __init__(self):
        self.width = 768
        self.height = 1024
        self.placementWidth = self.width*.50
        self.placementHeight = self.height*.05
      
  
    def createButtonMoves(self, node):
        xVal = 0
        yVal = 0
        count = 0
        buttonArray = []
        for children in node.children:
            if  count == 8:
                xVal += 265
                yVal = 0
                count = 0
            button = Button((255,140,0), self.placementWidth+xVal, self.placementHeight + yVal, 260, 50, str(children.pile), children)  
            yVal += 55  
            buttonArray.append(button)
            count +=1
        return buttonArray

    # def getMoves(self):
    #     return self.buttonArray