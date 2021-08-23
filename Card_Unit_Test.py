import os
from Card  import Deck_of_Cards
import unittest
import datetime

class Test_Cards(unittest.TestCase):
    # Test Creating deck
    def test_base(self):
        deck = Deck_of_Cards()
        self.assertEquals(len(deck.cards),52)


        # Test shuffle
        first_card = deck.cards[0]
        last_card = deck.cards[-1]
        deck.shuffle()
        self.assertNotEquals(first_card + last_card,deck.cards[0] + deck.cards[-1])

        # Test Cut
        first_card = deck.cards[0]
        deck.cut(1)
        self.assertEquals(first_card,deck.cards[-1])

        # Test Deal
        deck.deal(1)
        self.assertEquals(len(deck.cards),51)

        # Create Black Jack
        deck.create_blackJack(3)
        # Remember, the deal function, on line 25, takes a card
        self.assertEquals(len(deck.cards),43)
        
        # Test multi deck feature
        deck.create_deck(5)
        self.assertEquals(len(deck.cards),260)

if __name__ == '__main__':
    unittest.main()