import unittest
from unittest.mock import patch
from io import StringIO
from dice_game import calculate_score, computer_strategy, Dice, Player, play_round


class TestDiceGame(unittest.TestCase):
    def test_calculate_score(self):
        self.assertEqual(calculate_score([1, 2, 3, 4, 5]), 1500)
        self.assertEqual(calculate_score([2, 3, 4, 5, 6]), 1500)
        self.assertEqual(calculate_score([1, 1, 1, 2, 3]), 9)
        self.assertEqual(calculate_score([4, 4, 4, 4, 1]), 4096)
        self.assertEqual(calculate_score([5, 5, 5, 5, 5]), 390625)
        self.assertEqual(calculate_score([1, 2, 3, 4, 6]), 0)
        self.assertEqual(calculate_score([1, 1, 2, 2, 2]), 36)
        self.assertEqual(calculate_score([3, 3, 3, 3, 3]), 50625)

    def test_computer_strategy(self):
        self.assertTrue(computer_strategy(200, 2))
        self.assertFalse(computer_strategy(400, 1))
        self.assertFalse(computer_strategy(100, 0))
        self.assertTrue(computer_strategy(250, 3))
        self.assertFalse(computer_strategy(300, 1))

    def test_dice_roll(self):
        dice = Dice(5)
        rolls = dice.roll()
        self.assertEqual(len(rolls), 5)
        self.assertTrue(all(1 <= roll <= 6 for roll in rolls))

    def test_player_play_round(self):
        player = Player("Player")
        dice = Dice(5)

        with patch('builtins.input', side_effect=['y', 'n']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                player.play_round(dice)
                output = fake_output.getvalue().strip()
                self.assertIn("Player's turn:", output)
                self.assertIn("Initial roll:", output)
                self.assertIn("Score:", output)
                self.assertIn("New roll:", output)

    def test_player_get_user_decision(self):
        player = Player("Player")

        with patch('builtins.input', return_value='y'):
            self.assertTrue(player.get_user_decision("Test prompt"))

        with patch('builtins.input', return_value='n'):
            self.assertFalse(player.get_user_decision("Test prompt"))

        with patch('builtins.input', side_effect=['invalid', 'y']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                player.get_user_decision("Test prompt")
                output = fake_output.getvalue().strip()
                self.assertIn("Invalid input. Please enter 'y' or 'n'.", output)

    def test_play_round(self):
        player = Player("Player")
        computer = Player("Computer")
        dice = Dice(5)

        with patch('builtins.input', side_effect=['n', 'n', 'n']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                play_round(player, computer, dice, 1)
                output = fake_output.getvalue().strip()
                self.assertIn("Round 1", output)
                self.assertIn("Player's turn:", output)
                self.assertIn("Player score for round 1:", output)
                self.assertIn("Player total score:", output)
                self.assertIn("Computer score for round 1:", output)
                self.assertIn("Computer total score:", output)


if __name__ == '__main__':
    unittest.main()

