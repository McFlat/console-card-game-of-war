# -*- coding: utf-8 -*-
import unittest
from wargame import card, debug

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

__all__ = [
    'TestCard',
    'TestCardInstance'
]


class TestCard(unittest.TestCase):
    def test_import_debug(self):
        self.assertEqual(card.debug, debug)

    def test_kinds(self):
        self.assertEqual(card.kinds, kinds)

    def test_suits(self):
        self.assertEqual(card.suits, suits)

    def test_ranks(self):
        self.assertEqual(card.ranks, ranks)

    def test_faces(self):
        self.assertEqual(card.faces, faces)


class TestCardInstance(unittest.TestCase):
    def setUp(self):
        self.cardJC = card.Card(kind=11, suit=1, rank=11)
        self.cardQH = card.Card(kind=12, suit=2, rank=12)
        self.cardKD = card.Card(kind=13, suit=0, rank=13)
        self.cardAS = card.Card(kind=14, suit=3, rank=14)

    def test_card_instance(self):
        self.assertEqual(str(self.cardJC), 'Jack of Clubs %s' % faces[1])
        self.assertEqual(self.cardJC.face, 'JC')
        self.assertEqual(self.cardJC.get_kind(), 'Jack')
        self.assertEqual(self.cardJC.get_suit(), 'Clubs')
        self.assertEqual(self.cardJC.get_face(), faces[1])
        self.assertEqual(self.cardJC.get_rank(), 11)

        self.assertEqual(str(self.cardQH), 'Queen of Hearts %s' % faces[2])
        self.assertEqual(self.cardQH.face, 'QH')
        self.assertEqual(self.cardQH.get_kind(), 'Queen')
        self.assertEqual(self.cardQH.get_suit(), 'Hearts')
        self.assertEqual(self.cardQH.get_face(), faces[2])
        self.assertEqual(self.cardQH.get_rank(), 12)

        self.assertEqual(str(self.cardKD), 'King of Diamonds %s' % faces[0])
        self.assertEqual(self.cardKD.face, 'KD')
        self.assertEqual(self.cardKD.get_kind(), 'King')
        self.assertEqual(self.cardKD.get_suit(), 'Diamonds')
        self.assertEqual(self.cardKD.get_face(), faces[0])
        self.assertEqual(self.cardKD.get_rank(), 13)

        self.assertEqual(str(self.cardAS), 'Ace of Spades %s' % faces[3])
        self.assertEqual(self.cardAS.face, 'AS')
        self.assertEqual(self.cardAS.get_kind(), 'Ace')
        self.assertEqual(self.cardAS.get_suit(), 'Spades')
        self.assertEqual(self.cardAS.get_face(), faces[3])
        self.assertEqual(self.cardAS.get_rank(), 14)
