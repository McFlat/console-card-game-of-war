# -*- coding: utf-8 -*-
import unittest
from wargame import player, debug


class TestPlayer(unittest.TestCase):
    def test_import_debug(self):
        self.assertEqual(player.debug, debug)
