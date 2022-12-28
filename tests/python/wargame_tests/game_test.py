# -*- coding: utf-8 -*-
import unittest
from wargame import game, debug


class TestGame(unittest.TestCase):
    def test_import_debug(self):
        self.assertEqual(game.debug, debug)
