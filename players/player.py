from games import game
import random

class Player:
    def __init__(self,**kwargs):
        """Initialize name and amount."""
        self.name = kwargs['name']
        self.amount = kwargs['amount']

    def wager(self, player, card):
        """Follows the optimal rules regarding how much to wager when ante=1 and bet=1.
        Player 1 always bets with K or Q, and bets with J with probability 1/3.
        Player 2 always bets with K, bets with Q with probability 1/3, and never bets with J.
        """
        chance = random.Random()
        to_wager_or_not = chance.choice([1,2,3])
        if player==1:
            if card=='K':
                return True
            elif card=='Q':
                return True
            else:
                return True if to_wager_or_not == 1 else False
        else:
            if card=='K':
                return True
            elif card=='Q':
                return True if to_wager_or_not == 1 else False
            else:
                return False

    def ante_up(self, ante):
        """Put ante at beginning of a round."""
        self.amount -= ante

    def pay_bet(self, bet):
        """If wager has returned true, place money for bet."""
        self.amount -= bet

