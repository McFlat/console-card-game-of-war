# -*- coding: utf-8 -*-
# console-card-game-of-war by Alex Goretoy <alex@goretoy.com> http://alexgoretoy.com

import logging

from wargame import debug, magenta, cyan


class Table(object):
    players = []
    dealer = None
    battles = []
    rounds = []

    def __init__(self, dealer):
        super(Table, self).__init__()
        self.dealer = dealer

    def clear(self):
        self.players = []

    def join(self, player):
        # player joins table and sites down
        # if there's already a guess from the first player
        # then the second player gets the other side of the coin guess before the toss
        self.players.append(player)
        player.sit(table=self)

    def arrange(self, coin, players):
        if len(players) > 1:
            if coin.side is not players[0].guess:
                players.reverse()

            for p in range(len(players)):
                logging.info('=== %s is Player%s 🤞' % (players[p], p + 1))
                players[p].seat(index=p + 1)
            logging.info('🤝 >>> PLAYERS SHAKE HANDS <<< 🍻')
        else:
            print('! Not enough players to determine who goes first')

    def play(self, callback):
        if len(self.players) > 1:
            # reset the number of battles
            # logging.debug('@@@ Reset number of battles')
            battles = []
            # dealer deal new deck of cards to players
            self.dealer.deal(*self.players)
            # dealer coin toss and arrange players at table
            logging.info('=== DEALER TOSSES COIN 💸')
            landing = self.dealer.toss()
            logging.info('=== COIN IS %s' % str(landing).upper())
            self.arrange(landing, self.players)

            # print(self.players[0].stack)
            # print(self.players[1].stack)

            while len(battles) <= 99:
                def play():
                    result = []
                    for p in range(len(self.players)):
                        if len(self.players) is 2:
                            op = self.players[0 if p is 1 else 1]
                        else:
                            raise IndexError('Round with more than 2 players are not yet implemented')
                        card = self.players[p].play(op)
                        logging.info('=== %s played a %s' % (self.players[p], card))
                        result.append(card)
                    return result

                logging.info(magenta('🥊 BATTLE %s ROUND 1 ♦️ ♣️ ♥️ ♠️'), len(battles) + 1)
                first = play()

                counter = 0

                def who(cards, count):
                    count += 1
                    if cards[0].rank is not cards[1].rank:
                        ranks = [c.rank for c in cards]
                        winning = max(ranks)
                        winner = self.players[ranks.index(winning)]
                        winner.take(*cards)
                        logging.info('🏆 Winner %s' % winner.label())
                    else:  # tied
                        logging.info(cyan('🥊 ♦️ ♣️ ♥️ ♠️ ROUND %s'), count + 1)
                        second = play()
                        winner = None
                        who(cards=second, count=count)
                    battles.append({'id': len(battles) + 1, 'cards': [str(c) for c in cards], 'winner': winner})
                    count += 1
                if isinstance(first[0], list):
                    first = first[1]

                who(cards=first, count=counter)

            if len(battles):
                callback(battles)
                return True
        else:
            print('! Not enough players to start game')
        return False

    def __str__(self):
        stats = '=== Dealer name: {}\n'.format(self.dealer.name)
        for idx in range(0, len(self.players)):
            stats = '{}Player{} name: {}\n'.format(
                stats, idx + 1, self.players[idx]
            )
        return stats
