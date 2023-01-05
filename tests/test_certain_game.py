import unittest
import mock
import sys

import runner
from runner import gamerunner

class TestCertainGame(unittest.TestCase):
    @mock.patch('runner.gamerunner.deal_cards')
    def test_run_game(self,mock_deal_cards):
        """
        Test if one round produces expected result.
        Use Player 1 draws Q and Player 2 draws K since that is only situation
        where we are sure of what both players will do (i.e. bet).
        """
        mock_deal_cards.return_value = 'Q', 'K'
        g, p1, p2, _ = runner.gamerunner.initialize_game(file="test_config.json")
        g, p1, p2 = runner.gamerunner.play_a_round(g, p1, p2)
        print('{} has {} and {} has {}\n'.format(p1.name, p1.amount, p2.name, p2.amount))
        self.assertEqual(p1.amount,8)
        self.assertEqual(p2.amount,12)

if __name__ == '__main__':
    unittest.main()
