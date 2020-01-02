import random
from Card import Card

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine',
             'Ten','Jack','Queen','King','Ace')

class Deck:

    def __init__(self):

        global suits
        global ranks

        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        card_deck = 'Card deck contains: \n'

        for card in self.deck:
            card_deck += card.__str__() + '\n'

        return card_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        delt_card = random.choice(self.deck)
        self.deck.remove(delt_card)
        return delt_card
