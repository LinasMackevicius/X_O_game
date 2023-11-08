from unittest import TestCase
from game import TicTacToeGame, Move, Player

class TestTicTacToeGame(TestCase):
    def setUp(self):
        # Initialize a TicTacToeGame instance
        self.game = TicTacToeGame(players=(
            Player(label="X", color="blue"),
            Player(label="O", color="green"),
        ), board_size=3)

    def test__setup_board(self):
        # Check if the board is correctly set up with empty moves
        self.game._setup_board()
        for row in self.game._current_moves:
            for move in row:
                self.assertEqual(move.label, "")

    def test__get_winning_combos(self):
        # Check if winning combos are correctly generated
        winning_combos = self.game._get_winning_combos()
        # You can write assertions based on the game's logic and the board size

    def test_toggle_player(self):
        # Test toggling players
        initial_player = self.game.current_player
        self.game.toggle_player()
        self.assertNotEqual(initial_player, self.game.current_player)

    def test_is_valid_move(self):
        # Test valid and invalid moves
        valid_move = Move(row=0, col=0, label="X")
        self.assertTrue(self.game.is_valid_move(valid_move))
        invalid_move = Move(row=0, col=0, label="O")
        self.assertFalse(self.game.is_valid_move(invalid_move))

    def test_process_move(self):
        # Test processing a move
        move = Move(row=0, col=0, label="X")
        self.game.process_move(move)
        self.assertEqual(self.game._current_moves[0][0].label, "X")

    def test_has_winner(self):
        # Test checking for a winner
        # You can create a test case where there is a winner and one where there isn't

    def test_is_tied(self):
        # Test checking for a tied game
        # You can create a test case where the game is tied and one where it's not

    def test_reset_game(self):
        # Test resetting the game
        self.game.process_move(Move(row=0, col=0, label="X"))
        self.game.reset_game()
        for row in self.game._current_moves:
            for move in row:
                self.assertEqual(move.label, "")
