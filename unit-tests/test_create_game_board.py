from unittest import TestCase
from sud import create_game_board


class TestCreate_game_board(TestCase):
    def test_normal_create_game_board(self):
        self.assertEqual(create_game_board(), {(0, 0): '*', (0, 1): '*', (0, 2): '*', (0, 3): '*', (0, 4): '*',
                                               (0, 5): '*', (0, 6): '*', (0, 7): '*', (0, 8): '*', (1, 0): '*',
                                               (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                                               (1, 6): '*', (1, 7): '*', (1, 8): '*', (2, 0): '*', (2, 1): '*',
                                               (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                                               (2, 7): '*', (2, 8): '*', (3, 0): '*', (3, 1): '*', (3, 2): '*',
                                               (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                                               (3, 8): '*', (4, 0): '*', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                                               (4, 4): '*', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): '*',
                                               (5, 0): '*', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                                               (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): '*', (6, 0): '*',
                                               (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                                               (6, 6): '*', (6, 7): '*', (6, 8): '*', (7, 0): '*', (7, 1): '*',
                                               (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                                               (7, 7): '*', (7, 8): '*', (8, 0): '*', (8, 1): '*', (8, 2): '*',
                                               (8, 3): '*', (8, 4): '*', (8, 5): '*', (8, 6): '*', (8, 7): '*',
                                               (8, 8): '*'})

    def test_length_create_game_board(self):
        self.assertTrue(len(create_game_board()), 8)

    def test_correct_1_create_game_board(self):
        new_board = create_game_board()
        self.assertEqual(new_board[(0, 0)], '*')

    def test_correct_2_create_game_board(self):
        new_board = create_game_board()
        self.assertEqual(new_board[(8, 0)], '*')

    def test_correct_3_create_game_board(self):
        new_board = create_game_board()
        self.assertEqual(new_board[(0, 8)], '*')

    def test_correct_4_create_game_board(self):
        new_board = create_game_board()
        self.assertEqual(new_board[(8, 8)], '*')

    def test_type_create_game_board(self):
        new_board = create_game_board()
        self.assertIsInstance(new_board, dict)
