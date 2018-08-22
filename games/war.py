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