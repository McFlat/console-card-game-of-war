# -*- coding: utf-8 -*-
# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

import random
import logging

from wargame.card import Card


class Deck(object):
    def __init__(self):
        """
        Grab a new deck of cards
        """
        super(Deck, self).__init__()
        logging.info('=== Grabbing 🎴 new Deck ===')
        self.cards = []

    def shuffle(self):
        """
        Shuffle deck of cards
        :return:
        """
        logging.info('=== Deck 🔀 being shuffled ===')
        random.shuffle(self.cards)
        return self

    def open(self):
        """
        Open deck of cards
        :return:
        """
        logging.info('=== Deck 👐 being opened ===')
        for i in range(0, 4):  # suits
            for j in range(2, 15):  # kind/ranks

                card = Card(kind=j, suit=i, rank=j)
                self.cards.append(card)
        return self
