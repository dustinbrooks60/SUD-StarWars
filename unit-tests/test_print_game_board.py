from unittest import TestCase
from sud import print_game_board
import unittest.mock
import io

class TestPrint_game_board(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_unbordered_print_game_board(self, mock_stdout):
        game_dictionary = {(0, 0): '*', (0, 1): '*', (0, 2): '*', (0, 3): '*', (0, 4): '*',
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
                           (8, 3): '*', (8, 4): '*', (8, 5): '*', (8, 6): '*', (8, 7): '*', (8, 8): '*'}

        expected_output = ("""* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * \n"""

        )
        print_game_board(game_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bordered_print_game_board(self, mock_stdout):
        game_dictionary = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): 'X',
                           (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                           (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                           (1, 6): '*', (1, 7): '*', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
                           (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                           (2, 7): '*', (2, 8): 'X', (3, 0): 'X', (3, 1): '*', (3, 2): '*',
                           (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                           (3, 8): 'X', (4, 0): 'X', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                           (4, 4): '*', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): 'X',
                           (5, 0): 'X', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                           (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): 'X', (6, 0): 'X',
                           (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                           (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '*',
                           (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                           (7, 7): '*', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                           (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}

        expected_output = """X X X X X X X X X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X X X X X X X X X \n"""
        print_game_board(game_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
