import os
import unittest
import wargame

version_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'VERSION'))
if not os.path.isfile(version_file_path):
    exit('VERSION file not found: %s' % version_file_path)

with open(version_file_path) as version:
    _version = version.read().strip()

_all = [
    'card',
    'coin',
    'dealer',
    'deck',
    'game',
    'player',
    'table',
]


class TestWarGame(unittest.TestCase):
    def test_import_sys(self):
        self.assertEqual(wargame.os, os)

    def test_name(self):
        self.assertEqual(wargame.name, 'wargame')

    def test___version__(self):
        self.assertEqual(wargame.__version__, _version)

    def test___all__(self):
        self.assertEqual(wargame.__all__, _all)

    def test_debug(self):
        self.assertEqual(type(wargame.debug), lambda: '')

    def test_red(self):
        self.assertEqual(type(wargame.red), lambda: '')

    def test_green(self):
        self.assertEqual(type(wargame.green), lambda: '')

    def test_magenta(self):
        self.assertEqual(type(wargame.magenta), lambda: '')

    def test_yellow(self):
        self.assertEqual(type(wargame.yellow), lambda: '')
