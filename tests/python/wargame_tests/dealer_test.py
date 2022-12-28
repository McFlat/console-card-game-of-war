# -*- coding: utf-8 -*-
import unittest
from wargame import dealer, debug


class TestDealer(unittest.TestCase):
    def test_import_debug(self):
        self.assertEqual(dealer.debug, debug)
