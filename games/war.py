from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    
    values = [None, None, "2", "3", "4", "5", "6", "7", "8",
              "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, v, s):
        """スートも値も整数値です"""
        self.value = v
        self.suit = s
    
    def __lt__(self, c2):
        """＜の演算子で計算できるようになります"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレイヤー１の名前 :")
        name2 = input("プレイヤー２の名前 :")
        self.deck = Player(name1)
        self.p1 =
        
