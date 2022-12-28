# -*- coding: utf-8 -*-
import unittest
import random
import logging
from wargame import coin, logging, debug, yellow, green


__all__ = [
    'TestCoin',
    # 'TestCoinInstance'
]


class TestCoin(unittest.TestCase):
    def test_import_random(self):
        self.assertEqual(coin.random, random)

    def test_import_logging(self):
        self.assertEqual(coin.logging, logging)

    def test_import_debug(self):
        self.assertEqual(coin.debug, debug)

