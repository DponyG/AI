class Cards:
    
    def __init__(self):
        self.cardfaces = []
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.royals = ["J", "Q", "K", "A"]
        self.deck = []

        for i in range (2,11):
            self.cardfaces.append(str(i))
        for j in range(4):
            self.cardfaces.append(self.royals[j])
        for k in range(4):
            for l in range(13):
                card = (self.cardfaces[l] + " " + self.suits[k])
                self.deck.append(card)

    
    def getdeck(self):
        return self.deck






    



    

        

        
    



