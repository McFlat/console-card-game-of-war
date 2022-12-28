# -*- coding: utf-8 -*-
# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

import random
import logging
from wargame import debug, yellow, green

# https://www.asciiart.eu/miscellaneous/money


class Coin(object):
    side = random.randint(0, 1)

    @staticmethod
    def animate():
        """
        animation meh
        """
        return yellow("""
                 ______________
    __,.,---'''''              '''''---..._
 ,-'             .....:::''::.:            '`-.
'           ...:::.....       '
            ''':::'''''       .               ,
|'-.._           ''''':::..::':          __,,-
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....---''
      💰 !!!COIN SPINS AND SPARKLES!!! 💰""")

    def draw(self):
        """
        draw side
        """

        return yellow("""
             _.oood"""""""booo._
         _.o""   |`.  |    |   ""o._
       oP"  |`.  |  `.|    |    |  "Yo
     o8 `.  |  `.|    |.   |    |    `8o
    d'    `.|    |.   | `. |    |      `b
   d"-------*====+====+====+====+-------"b
  8'  `.    INNNNINNNNINNNNINNNNI        `8
 8      `.  INNNNINNNNINNNNINNNNI          8
,8----------+====*====+====+====+----------8.
8'  `.     `|    |`.  |gnnnnnnnn|.         `8
8     `.    |`.  |  `.|8   |.   | `.        8
8-----------+----+----*8---+----+-----------8
8        `. |   `|    |8,gnnnn:.|    `.     8
8.         `|    |`.  |8P".| "Yb|..png.`.  ,8
`8----------+----+----+----+---8+-8--`"----8'
 8          | `. |   `|n.  |`.dP| 8`. n    8
  8.        |   `|    |"YbnnndP.| `bnnP  ,8
   Y.-------+----+----+----+----+-------.P
    Y.      |    | `. |   `|    |`.    ,P
     "8.    | cg |   `|    |`.  |  `. 8"
       "Y_  | mm |  19|89  |  `.|  _P"
         `'"oo_  |    |  `.|  _oo""'
              `""""ooodboo""""'
           💰 !!! COIN LANDS !!! 💰""")

    @staticmethod
    def flip():
        logging.info(Coin.animate())
        coin = Coin()
        coin.side = random.randint(0, 1)
        logging.info(coin.draw())

        return coin

    @staticmethod
    def parse(side):
        debug('$$$ Coin::parse(side): %s', side)
        if isinstance(side, str):
            side = 0 if side.lower() is 'Heads'.lower() else 1
        return green('🐴 Heads' if side == 0 else '🐒 Tails')

    def __str__(self):
        return Coin.parse(self.side)
