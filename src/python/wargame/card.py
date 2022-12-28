# -*- coding: utf-8 -*-
# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

from wargame import debug

kinds = {
    11: 'Jack',
    12: 'Queen',
    13: 'King',
    14: 'Ace',
}
suits = {
    0: 'Diamonds',
    1: 'Clubs',
    2: 'Hearts',
    3: 'Spades',
}
ranks = range(2, 15)
faces = [
    '♦️', '♣️', '♥️', '♠️'
]


class Card(object):
    kind = None
    suit = None
    rank = None

    def __init__(self, **kwargs):
        super(Card, self).__init__()
        self.set(**kwargs)

    @staticmethod
    def draw():
        """
        draw card not implemented yet
         -------------   -------------   -------------   -------------   -------------   -------------   -------------
        |10♣          | |J♦           | |Q♥           | |K♠           | |A♣           | |* * * * * * *| |J            |
        |   -------   | |   -------   | |   -------   | |   -------   | |   -------   | | * * * * * * | |O  -------   |
        |  |♣     ♣|  | |  |♦      |  | |  |♥      |  | |  |♠      |  | |  |       |  | |* * * * * * *| |K |       |  |
        |  |   ♣   |  | |  |       |  | |  |       |  | |  |       |  | |  |       |  | | * * * * * * | |E | J     |  |
        |  |♣     ♣|  | |  |       |  | |  |       |  | |  |       |  | |  |       |  | |* * * * * * *| |R |  O    |  |
        |  |       |  | |  |   J   |  | |  |   Q   |  | |  |   K   |  | |  |   ♣   |  | | * * * * * * | |  |   K   |  |
        |  |♣     ♣|  | |  |       |  | |  |       |  | |  |       |  | |  |       |  | |* * * * * * *| |  |    E  | J|
        |  |   ♣   |  | |  |       |  | |  |       |  | |  |       |  | |  |       |  | | * * * * * * | |  |     R | O|
        |  |♣     ♣|  | |  |      ♦|  | |  |      ♥|  | |  |      ♠|  | |  |       |  | |* * * * * * *| |  |       | K|
        |   -------   | |   -------   | |   -------   | |   -------   | |   -------   | | * * * * * * | |   -------  E|
        |          ♣10| |           ♦J| |           ♥Q| |           ♠K| |           ♣A| |* * * * * * *| |            R|
         -------------   -------------   -------------   -------------   -------------   -------------   -------------
        """
        pass

    def set(self, **kwargs):
        """
        set the card which was pulled out of the deck and dealt
        :param kwargs: int(kind) 2-14, int(suit) 0-3, int(rank) 2-14
        """
        debug('$$$ Card::set(**kwargs): %s', kwargs)
        [setattr(self, i, v) for i, v in kwargs.items()
            if i in ['kind', 'suit', 'rank'] and v < 15]

    def get_kind(self):
        """
        get kind value
        :return: str|int - card kind value
        """
        try:
            return kinds[self.kind]
        except KeyError:
            return self.kind

    def get_suit(self):
        """
        get suit value
        :return: str - card suit value
        """
        try:
            return suits[self.suit]
        except KeyError:
            raise KeyError("That suit does not exist")

    def get_rank(self):
        """
        get rank value
        :return: int - card rank value
        """
        return self.rank

    def get_face(self):
        """
        get face suit
        :return: str - card face suit
        """
        try:
            return faces[self.suit]
        except KeyError:
            raise KeyError("That face does not exist")

    # def __get__(self):
    #     return {
    #         'kind': self.get_kind(),
    #         'suit': self.get_suit(),
    #         'rank': self.get_rank(),
    #     }

    @property
    def face(self):
        kind = self.get_kind()
        if isinstance(kind, str):  # must be str, not unicode or doesn't work, for skip int
            kind = kind[0]
        return '{}{}'.format(kind, self.get_suit()[0])

    def __str__(self):
        return '{} of {} {}'.format(self.get_kind(), self.get_suit(), self.get_face())
