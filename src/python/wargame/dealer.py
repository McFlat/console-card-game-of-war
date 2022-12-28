# -*- coding: utf-8 -*-
# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

import logging
from wargame import debug

from wargame.deck import Deck
from wargame.coin import Coin

ordinal = lambda n: \
    str(n) + (list(['th', 'st', 'nd', 'rd'] + ['th'] * 6)
              [(int(str(n)[-1])) % 10]
              if not int(str(n)[-2:]) % 100 in range(11, 14) else 'th')


class Dealer(object):
    name = None

    def __init__(self, name):
        super(Dealer, self).__init__()
        self.name = name

    @staticmethod
    def toss():
        return Coin.flip()

    def deal(self, *players):
        """
        Deal a new Deck of cards

        :return:
        """
        debug('$$$ Dealer::(*players): %s', players)
        if len(players) > 1:
            # 1. get a fresh new deck
            deck = Deck().open()

            # 2. shuffle all the cards
            deck.shuffle()

            # 3. put any old cards aside
            for player in players:
                player.stack = []
                logging.info('=== %s is ready for new cards' % player.name)

            logging.info('=== DEALER: %s 👱 giving out the cards' % self.name)

            # 4. deal cards to the players
            for card in range(0, len(deck.cards)):
                # player index to give card to
                idx = card % len(players)
                # player takes card given
                players[idx].add(deck.cards[card])
                debug('+++ Dealer gave the %s card (%s) to %s' % (
                    ordinal(card + 1), deck.cards[card], players[idx].name
                ))

            print('=== %s has dealt all cards to %s ⌛' % (
                self.name, ' and '.join([p.name for p in players]))
            )
            return players
        else:
            print('! Not enough players to open new deck and deal out cards')
            return None
