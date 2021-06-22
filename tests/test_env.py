import unittest
import os
import sys

root_dir = os.path.dirname( __file__ )
src_dir = os.path.join(root_dir, '..')
sys.path.append(src_dir)

from src.environment import Easy21

class TestRewardValues(unittest.TestCase):
    
    def test_win(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 21
        self.assertEqual(e._step(5, 5, False)[2], 1)

    def test_loss_bust_21(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 23
        self.assertEqual(e._step(5, 5, False)[2], -1)

    def test_loss_bust_1(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 0
        self.assertEqual(e._step(5, 5, False)[2], -1)

    def test_tie(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 17
        self.assertEqual(e._step(5, 5, False)[2], 0)


if __name__ == '__main__':
    unittest.main()