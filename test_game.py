import unittest
from unittest import TestCase
from game import TicTacToeBoard, TicTacToeGame, Player, Move
import tkinter as tk
from unittest.mock import Mock, patch


class TestTicTacToeGame(TestCase):
    def test__setup_board(self):
        your_instance = TicTacToeGame()
        expected_moves = [
            [Move(row, col) for col in range(your_instance.board_size)]
            for row in range(your_instance.board_size)
        ]

        # Act
        your_instance._setup_board()

        # Assert
        self.assertEqual(your_instance._current_moves, expected_moves)

    def test__get_winning_combos(self):
        # Arrange
        your_instance = TicTacToeGame()
        your_instance._current_moves = [
            [Move(0, 0), Move(0, 1), Move(0, 2)],
            [Move(1, 0), Move(1, 1), Move(1, 2)],
            [Move(2, 0), Move(2, 1), Move(2, 2)],
        ]

        combos = your_instance._get_winning_combos()

        expected_combos = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
            [(0, 2), (1, 1), (2, 0)],  # Diagonal from top-right to bottom-left
        ]

        self.assertEqual(combos, expected_combos)

    def test_toggle_player(self):
        def test_toggle_player(self):
            # Arrange
            your_instance = TicTacToeGame
            initial_player = your_instance.current_player

            # Act
            your_instance.toggle_player()
            toggled_player = your_instance.current_player

            # Assert
            # Add assertions to check that the player was toggled correctly
            self.assertNotEqual(initial_player, toggled_player)

    def setUp(self):
        self.game = TicTacToeGame()

    def test_is_valid_move_valid(self):
        # Arrange
        valid_move = Move(row=0, col=0)
        self.game._has_winner = False
        self.game._current_moves[0][0] = Move(row=0, col=0, label="")  # Create a new Move object

        # Act
        result = self.game.is_valid_move(valid_move)

        # Assert
        self.assertTrue(result)

    def test_is_valid_move_invalid_already_played(self):
        # Arrange
        played_move = Move(row=1, col=1)
        self.game._has_winner = False
        self.game._current_moves[1][1] = Move(row=1, col=1, label="X")  # Create a new Move object

        # Act
        result = self.game.is_valid_move(played_move)

        # Assert
        self.assertFalse(result)

    def test_is_valid_move_invalid_has_winner(self):
        # Arrange
        move = Move(row=2, col=2)
        self.game._has_winner = True
        self.game._current_moves[2][2] = Move(row=2, col=2, label="")  # Create a new Move object

        # Act
        result = self.game.is_valid_move(move)

        # Assert
        self.assertFalse(result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    # Create a test suite that includes all test cases
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TicTacToeGame)

    # Run the test suite
    unittest.TextTestRunner().run(test_suite)
