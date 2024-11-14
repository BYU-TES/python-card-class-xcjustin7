#definition for a card class

class Card:

    def __init__(self, s, r):
        self.suit = s
        self.rank = r
        self.value = 0
        if r == "Two":
            self.value = 2
        elif r == 'Three':
                self.value = 3
        elif r == 'Four':
                self.value = 4
        elif r == 'Five':
                self.value = 5
        elif r == 'Six':
                self.value = 6
        elif r == 'Seven':
                self.value = 7
        elif r == 'Eight':
                self.value = 8
        elif r == 'Nine':
                self.value = 9
        elif r == 'Ten':
                self.value = 10
        elif r == 'Jack':
                self.value = 10
        elif r == 'Queen':
                self.value = 10
        elif r == 'King':
                self.value = 10
        elif r == 'Ace':
                self.value = 11


    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def get_value(self):
        return (self.value)
    
    def __str__(self):
        result = f'{self.rank} of {self.suit}'
        return result
    
    def change_ace(self):
            if self.rank == 'Ace' and self.value == 11:
                self.value = 1
                return True
            else:
                return False
            
