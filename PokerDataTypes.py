class Cards(Enum):
    Card_A=0
    Card_2=1
    Card_3=2
    Card_4=3
    Card_5=4
    Card_6=5
    Card_7=6
    Card_8=7
    Card_9=8
    Card_T=9
    Card_J=10
    Card_Q=11
    Card_K=12

class Suits(Enum):
    Spades = 0
    Hearts = 1
    Diamonds = 2
    Clubs = 3

class TablePositions(Enum):
    UTG = 0
    HJ = 1
    CO = 2
    BTN = 3
    SB = 4
    BB = 5

class Card():
    def __init__(self,card, suit):
        self.card = card
        self.suit = suit

    def getCard():
        return [self.card, self.suit]

class Hand():
    def __init__(self,cardA, cardB):
        self.cardA=cardA
        self.cardB=cardB
