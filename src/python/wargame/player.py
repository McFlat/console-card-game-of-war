# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

import random
import logging

from wargame import debug
from wargame.coin import Coin


class Player(object):
    name = None
    number = 0
    stack = []
    guess = None
    table = None

    def __init__(self, name):
        super(Player, self).__init__()
        debug('$$$ Player::new(name): %s', name)
        self.name = name

    def play(self, opponent):
        debug('$$$ Player%s::play(opponent): %s', self.number, opponent)
        # play card from top of stack
        try:
            played = self.stack[0]
            if self.count() > 1:
                self.stack = self.stack[1:]
            return played
        except IndexError:
            raise IndexError('\n!!! GAME OVER !!!\nPlayer %s: %s WINS! Player%s: %s LOSES!' % (
                self.number, self.name, opponent.number, opponent.name
            ))

    def add(self, *cards):
        # put card in stack and shuffle
        debug('$$$ Player%s::add(cards): %s', self.number, cards)
        self.stack.extend(cards)
        self.shuffle()

    def take(self, *cards):
        # put cards at bottom of stack
        debug('$$$ Player%s::take(cards): %s', self.number,  cards)
        self.stack.extend(cards)

    def shuffle(self):
        """
        Shuffle cards in stack
        :return:
        """
        debug('*$& %s SHUFFLING CARDS &$*' % self.label())
        random.shuffle(self.stack)

    def count(self):
        # count the stack of cards
        return len(self.stack)

    def seat(self, index):
        """
        Player takes a seat after coin toss
        :param index:
        :return:
        """
        self.number = index

    def sit(self, table):
        # join a new game/table
        self.table = table
        self.stack = []

        try:
            guess = table.players[0].guess
        except IndexError:
            guess = None
        if guess is None:
            self.guess = Coin.parse(random.randint(0, 1))
        else:
            self.guess = Coin.parse(1 if guess is 'Heads' else 0)

        logging.info('>>> {} joined the table and is guessing {}'.format(self.name, self.guess))
        return self

    def stats(self):
        return '{} has {} cards'.format(self, self.count())

    def label(self):
        return 'Player%s: %s' % (self.number, self)

    def __str__(self):
        return self.name
