# -*- coding: utf-8 -*-
import unittest
from wargame import deck


class TestDeck(unittest.TestCase):
    def test_import_debug(self):
        self.assertEqual(deck, deck)
