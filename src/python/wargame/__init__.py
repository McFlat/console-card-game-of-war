# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

import os
import logging
try:
    from termcolor import colored, cprint
    with_colors = True
except ImportError:
    with_colors = False

name = "wargame"
version_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'VERSION'))
if not os.path.isfile(version_file_path):
    exit('VERSION file not found: %s' % version_file_path)

with open(version_file_path) as version:
    __version__ = version.read().strip()

__all__ = [
    'card',
    'coin',
    'dealer',
    'deck',
    'game',
    'player',
    'table',
]


def debug(message, *args):
    if with_colors:
        return logging.debug(colored(message, 'yellow'), *args)
    else:
        return logging.debug(message, *args)


def red(message):
    if with_colors:
        return colored(message, 'red')
    else:
        return message


def green(message):
    if with_colors:
        return colored(message, 'green')
    else:
        return message


def magenta(message):
    if with_colors:
        return colored(message, 'magenta')
    else:
        return message


def cyan(message):
    if with_colors:
        return colored(message, 'cyan')
    else:
        return message


def yellow(message):
    return colored(message, 'yellow')
