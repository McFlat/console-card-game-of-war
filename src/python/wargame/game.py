# -*- coding: utf-8 -*-
# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

import logging

from wargame import debug, red, green
from wargame.dealer import Dealer
from wargame.player import Player
from wargame.table import Table


class Game(object):
    table = None
    dealer = None
    players = []

    battles = []
    rounds = []

    def __init__(self, name):
        debug('$$$ Game::new(name): %s', name)
        logging.info('>>> FINDING 🏓 TABLE <<<')
        self.table = Table(Dealer(name=name))
        logging.info('>>> DEALER: %s 👱 clearing the table' % name)
        self.table.clear()

    def start(self):
        """
        Start playing the Game
        :return: Game
        """
        logging.info('>>> STARTING 🃏 NEW GAME <<<')
        logging.info(self.table)

        if self.table.play(callback=self.finish):
            logging.info(self.suggest())

        return self

    def finish(self, battles):
        logging.info(green('♦♣♥♠ PLAYED %s BATTLES 🎲🎲' % len(battles)))
        logging.info('STATS: %s' % self.stats(battles))
        logging.info(red('>>> GAME 🎮 OVER <<<'))

    def stats(self, *battles):
        result = {'ties': 0}
        for rnd in battles[0]:
            if rnd['winner'] and rnd['winner'].number:
                if rnd['winner'].number not in result.keys():
                    result[rnd['winner'].number] = 0  # init count
                result[rnd['winner'].number] += 1
            else:
                result['ties'] += 1
        return result

    def join(self, *player):
        """
        Players can join the Game one at a time or in a group all together
        :param player: list of players to join the game table
        :return: Game
        """
        debug('$$$ Game::join(*player): %s', player)
        if isinstance(player, tuple):
            player = list(player)
        if isinstance(player, list):
            if isinstance(player[0], list):
                player = player[0]
            for person in player:
                if not isinstance(person, Player):
                    person = Player(person)
                self.table.join(player=person)
        return self

    @staticmethod
    def suggest():
        # TODO: use unicode symbols instead https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode
        chess = """
     A       B       C       D       E       F       G       H
  ------- ------- ------- ------- ------- ------- ------- -------
 | @___@ |  %~b  |  .@.  | \o*o/ | __+__ |  .@.  |  %~b  | @___@ |
8|  @♜@  | `'♞X  |  @♝@  |  @♛@  | `@♚@' |  @♝@  | `'♞X  |  @♜@  |8
 | d@@@b |  d@@b | ./A\. | d@@@b | d@@@b | ./A\. |  d@@b | d@@@b |
  ------- ------- ------- ------- ------- ------- ------- -------
 |   _   |   _   |   _   |   _   |   _   |   _   |   _   |   _   |
7|  (♟)  |  (♟)  |  (♟)  |  (♟)  |  (♟)  |  (♟)  |  (♟)  |  (♟)  |7
 |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |
  ------- ------- ------- ------- ------- ------- ------- -------
 |       | . . . |       | . . . |       | . . . |       | . . . |
6|       | . . . |       | . . . |       | . . . |       | . . . |6
 |       | . . . |       | . . . |       | . . . |       | . . . |
  ------- ------- ------- ------- ------- ------- ------- -------
 | . . . |       | . . . |       | . . . |       | . . . |       |
5| . . . |       | . . . |       | . . . |       | . . . |       |5
 | . . . |       | . . . |       | . . . |       | . . . |       |
  ------- ------- ------- ------- ------- ------- ------- -------
 |       | . . . |       | . . . |       | . . . |       | . . . |
4|       | . . . |       | . . . |       | . . . |       | . . . |4
 |       | . . . |       | . . . |       | . . . |       | . . . |
  ------- ------- ------- ------- ------- ------- ------- -------
 | . . . |       | . . . |       | . . . |       | . . . |       |
3| . . . |       | . . . |       | . . . |       | . . . |       |3
 | . . . |       | . . . |       | . . . |       | . . . |       |
  ------- ------- ------- ------- ------- ------- ------- -------
 |   _   |   _   |   _   |   _   |   _   |   _   |   _   |   _   |
2|  (♙)  |  (♙)  |  (♙)  |  (♙)  |  (♙)  |  (♙)  |  (♙)  |  (♙)  |2
 |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |
  ------- ------- ------- ------- ------- ------- ------- -------
 | [___] |  %~\  |  .O.  | \o^o/ | __+__ |  .O.  |  %~\  | [___] |
1|  [♖]  | `'♘(  |  \♗/  |  [♕]  | `.♔.' |  \♗/  | `'♘(  |  [♖]  |1
 | /___\ |  <__> |  /_\  | /___\ | /___\ |  /_\  |  <__> | /___\ |
  ------- ------- ------- ------- ------- ------- ------- -------
     A       B       C       D       E       F       G       H
""" + red("=== PLAY A GAME OF CHESS NEXT ===")

        return chess

    def __str__(self):
        return '{}'.format(self.table)
