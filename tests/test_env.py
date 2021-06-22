import unittest
import os
import sys

root_dir = os.path.dirname( __file__ )
src_dir = os.path.join(root_dir, '..')
sys.path.append(src_dir)

from src.environment import Easy21

class TestHits(unittest.TestCase):

    '''
    This only tests that a hit changes the value
    '''
    def test_hit(self):
        e = Easy21()
        init_state = e.get_state()
        new_state = e.step(init_state, True)
        self.assertNotEqual(init_state[1], new_state[1])

    def test_stick(self):
        e = Easy21()
        init_state = e.get_state()
        new_state = e.step(init_state, False)
        self.assertTrue(e._terminated)
        self.assertNotEqual(init_state[0], new_state[0])
        self.assertEqual(init_state[1], init_state[1])


class TestRewardValues(unittest.TestCase):
    
    def test_win(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 21
        self.assertEqual(e.step((5, 5), False)[1], 1)

    def test_loss_bust_21(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 23
        self.assertEqual(e.step((5, 5), False)[1], -1)

    def test_loss_bust_1(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 0
        self.assertEqual(e.step((5, 5), False)[1], -1)

    def test_tie(self):
        e = Easy21()
        e.dealer.score = 17
        e.player1.score = 17
        self.assertEqual(e.step((5, 5), False)[1], 0)


if __name__ == '__main__':
    unittest.main()