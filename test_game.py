from unittest import TestCase

from game import TicTacToeGame, Move


class TestTicTacToeGame(TestCase):
    def test__setup_board(self):

        your_instance = TicTacToeGame()  # Replace with the actual class name
        expected_moves = [
            [Move(row, col) for col in range(your_instance.board_size)]
            for row in range(your_instance.board_size)
        ]

        # Act
        your_instance._setup_board()

        # Assert
        self.assertEqual(your_instance._current_moves, expected_moves)

    def test__get_winning_combos(self):
        self.fail()

    def test_toggle_player(self):
        self.fail()
