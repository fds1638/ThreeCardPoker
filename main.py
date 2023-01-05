import os
import json
import numpy as np

import games
import players
from games.game import Game
#from players import player

def deal_cards():
    """From a deck of three return two cards."""
    deck = ['K','Q','J']
    first_card, second_card, _ = np.random.permutation(deck)
    return first_card, second_card

def initialize_game():
    """Initialize ante, bet, and number of rounds in game.
    Initialize player names and stake amounts."""
    f = open("config/config.json","r")
    lines = f.readlines()
    s = ""
    for line in lines:
        s = s + line + "\n"
    d = json.loads(s)
    g = games.game.Game(**d['game'])
    p1 = players.player.Player(**d['player1'])
    p2 = players.player.Player(**d['player2'])
    num_rounds = d['game']['rounds']
    return g, p1, p2, num_rounds

def play_a_round(g,p1,p2):
    """Given a game and two players, play a round."""
    g.get_antes(p1,p2)
    card1, card2 = deal_cards()
    print('{} drew {} and {} drew {}'.format(p1.name,card1,p2.name,card2))
    if p1.wager(1,card1):
        g.get_bet(p1)
        print('{} bet'.format(p1.name))
    else:
        g.distribute_pot(p2)
        print('{} folded'.format(p1.name))
        return g, p1, p2
    if p2.wager(2,card2):
        print('{} bet'.format(p2.name))
        g.get_bet(p2)
    else:
        g.distribute_pot(p1)
        print('{} folded'.format(p2.name))
        return g, p1, p2
    if card1=='K' or (card1=='Q' and card2=='J'):
        g.distribute_pot(p1)
    else:
        g.distribute_pot(p2)
    return g, p1, p2

def run_game():
    g, p1, p2, num_rounds = initialize_game()
    print('Player 1 is {} and Player 2 is {}'.format(p1.name,p2.name))
    print('{} starts with {} and {} starts with {}\n'.format(p1.name,p1.amount,p2.name,p2.amount))
    for _ in range(num_rounds):
        g, p1, p2 = play_a_round(g, p1, p2)
        print('{} has {} and {} has {}\n'.format(p1.name, p1.amount, p2.name, p2.amount))

if __name__=='__main__':
    run_game()