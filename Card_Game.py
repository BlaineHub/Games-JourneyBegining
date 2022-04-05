from random import shuffle

class Cards:
    suits = ["spades","hearts","diamonds","clubs"]
    values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

    def __init__(self,v,s):
        """creates card with value & suit"""
        self.value = v
        self.suit = s

    def __It__(self, c2):
        """allows compare if card lower than another card"""
        if self.value < c2.value:
            return True

        if self.value == c2.value:
             if self.suit <c2.suit:
                 return True
             else:
               return False
        return False

    def __gt__(self, c2):
        """allows compare if card greater than another card"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        """turns card values into string and prints it"""
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    """Creates a Deck of cards, for loop and using cards class"""
    def __init__(self):
        self.cards = []
        for i in range(2,15):
          for j in range(4):
            self.cards.append(Cards(i,j))
        shuffle(self.cards)

    def rm_card(self):
        """Removes card everytime created from deck, no duplicates"""
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
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        """Inputs player names and starts the deck"""

    def wins(self,winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n,p1c,p2n,p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)

    def play_game(self):
        """Intializing the Deck"""
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >=2:
            m = 'q to quit. Press any key to draw!'
            response = input(m)
            if response =='q':
                break
            """first cards taken out go p1 etc..."""
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            """Prints cards drawn"""
            if p1c > p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
                """adding 1 to p1 total and feeding name to win fucntion"""
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)
        win = self.winner(self.p1,self.p2)
        print("War is over.{} wins".format(win))
        print("{} {} vs {} {}".format(self.p1.name,self.p1.wins,self.p2.name,self.p2.wins))

    def winner(self,p1,p2):
        """After while loop we go to the win function"""
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "it was a tie"

game_new = Game()
game_new.play_game()

