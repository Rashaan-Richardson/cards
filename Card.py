import datetime
import logging
import math
import random
import time

# 1 - 'shuffle' to reorder the cards
    #Define a class to categorize the cards
logging.basicConfig(filename='/Users/rashaanrichardson/Desktop/Practice Python/Dev_Ops/card_logger.log', level=logging.INFO)

class Deck_of_Cards:
    def __init__(self):
        self.create_deck()
        self.number_of_cards = len(self.cards)
        self.start_time = datetime.datetime.now()
        logging.info(f'Created new instance of Deck of Cards {self.start_time}')


# Creating the deck
    def create_deck(self,deck=1):
        self.start_time = datetime.datetime.now()
        cards = []
        face_cards = ['Jack','Queen','King','Ace']
        non_face_cards = list(range(2,11))
        suit = ['Spades','Clubs','Hearts','Diamonds']
        for i in range(deck):
            cards += [f'{card} of {s}' for card in non_face_cards + face_cards for s in suit]
            # Add logging to count number of decks
            logging.info(f'Creating deck {i}')
        self.end_time = datetime.datetime.now()
        logging.info(f'The time it took to run was {self.end_time - self.start_time}. The amount of decks made was {deck}')
        self.cards = cards

    def __str__(self):
        logging.info(f'There are {self.number_of_cards} cards in the deck')

# Shuffling the deck
    def shuffle(self):
        random.shuffle(self.cards)
        
    def cut(self,num_of_cards_to_cut = 0):
        if num_of_cards_to_cut == 0:
            logging.info('You tapped the cards')
        if num_of_cards_to_cut > 0 and num_of_cards_to_cut < self.number_of_cards:
            self.cards = self.cards[num_of_cards_to_cut:] + self.cards[:num_of_cards_to_cut]

# Dealing the cards
    def deal(self,cards_to_deal=1):
        if cards_to_deal > self.number_of_cards:
            logging.info('You cannot deal more cards than are in the deck')
        else:
            for i in range(cards_to_deal):
                if self.number_of_cards > 0:
                    card = self.cards[0]
                    print(f'Dealt {card}')
                    # remove the card
                    self.cards.remove(card)
                    self.number_of_cards -= 1


if __name__ == '__main__':

    new_deal = Deck_of_Cards()
    # print(new_deal.cards)
    # new_deal.shuffle()
    # print(new_deal)
    # print(new_deal.cards)
    # new_deal.cut(20)
    # print(new_deal.cards)
    # new_deal.deal(10)
    # print(new_deal.cards)
    # new_deal.deal(10)
    # print(new_deal.cards)
    # new_deal.deal(10)
    # print(new_deal.cards)
    # new_deal.deal(10)
    # print(new_deal.cards)
    # new_deal.deal(10)
    # print(new_deal.cards)
    # new_deal.deal(3)
    print(new_deal.cards)
    new_deal.create_deck(5)
    print(len(new_deal.cards))
