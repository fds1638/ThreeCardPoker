from players import player

class Game:
    def __init__(self,**kwargs):
        """Initialize pot, ante amount, and bet amount from json config file."""
        self.pot = 0
        self.ante = kwargs['ante']
        self.bet = kwargs['bet']

    def get_antes(self, p1, p2):
        """Get antes at beginning of round."""
        self.pot += 2*self.bet
        p1.ante_up(self.ante)
        p2.ante_up(self.ante)

    def get_bet(self, player):
        """When a player has decided to wager, get money for the bet."""
        self.pot += self.bet
        player.pay_bet(self.bet)

    def distribute_pot(self, player):
        """When round is over, distribute the pot."""
        player.amount += self.pot
        self.pot = 0