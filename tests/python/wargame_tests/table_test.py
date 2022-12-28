# -*- coding: utf-8 -*-
import unittest
import logging
from wargame import table, debug, magenta, cyan


class TestTable(unittest.TestCase):
    def test_import_logging(self):
        self.assertEqual(table.logging, logging)

    def test_import_debug(self):
        self.assertEqual(table.debug, debug)

    def test_import_magenta(self):
        self.assertEqual(table.magenta, magenta)

    def test_import_cyan(self):
        self.assertEqual(table.cyan, cyan)


class TestTableInstance(unittest.TestCase):
    def setUp(self):
        self.cardJC = table.Card(kind=11, suit=1, rank=11)
        self.cardQH = card.Card(kind=12, suit=2, rank=12)
        self.cardKD = card.Card(kind=13, suit=0, rank=13)
        self.cardAS = card.Card(kind=14, suit=3, rank=14)