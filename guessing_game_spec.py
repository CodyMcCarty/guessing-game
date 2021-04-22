
import unittest
# from unittest.mock import patch
from guessing_game import GuessingGame



class GuessingGameTestCase(unittest.TestCase):
    "Test for `guessing_game.py`"

    def test_returns_not_solved(self):
        """When you call GuessingGame(), it should not start solved"""
        self.assertEqual(GuessingGame().is_solved, False)

# make test patch or mock in order to test user input and hardcode answer
if __name__ == '__main__':
    unittest.main()