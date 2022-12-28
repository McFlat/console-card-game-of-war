#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import names

from wargame.game import Game

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='count', default=1)
args = parser.parse_args()

levels = [logging.WARNING, logging.INFO, logging.DEBUG]
level = levels[min(len(levels)-1, args.verbose)]

logging.basicConfig(level=level, format="%(message)s")


def run():
    Game(name=names.get_full_name()).join(
        names.get_full_name(), names.get_full_name()
    ).start()

if __name__ == '__main__':
    run()
