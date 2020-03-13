from unittest import TestCase
from sud import move_west
import unittest.mock
import io


class TestMove_west(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_top_left_border_move_west(self, mock_stdout):
        new_board = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                     (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                     (1, 1): '@', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
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
        expected_output = ("You've hit the border! Please select another direction\n")
        move_west(new_board)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_top_right_move_west(self, mock_stdout):
        new_board = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                     (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                     (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                     (1, 6): '*', (1, 7): '@', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
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
        expected_output = (
"""You moved west by 1: 
X X X X   X X X X 
X * * * * * @ * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X X X X X X X X X \n""")
        move_west(new_board)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bottom_left_border_move_north(self, mock_stdout):
        new_board = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
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
                     (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '@',
                     (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                     (7, 7): '*', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                     (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        expected_output = ("You've hit the border! Please select another direction\n")
        move_west(new_board)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bottom_right_move_north(self, mock_stdout):
        expected_output = (
            """You moved west by 1: 
X X X X   X X X X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * @ * X 
X X X X X X X X X \n"""
        )

        new_board = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
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
                     (7, 7): '@', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                     (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        move_west(new_board)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_middle_move_north(self, mock_stdout):
        expected_output = (
            """You moved west by 1: 
X X X X   X X X X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * @ * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X X X X X X X X X \n"""
        )

        new_board = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                     (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                     (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                     (1, 6): '*', (1, 7): '*', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
                     (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                     (2, 7): '*', (2, 8): 'X', (3, 0): 'X', (3, 1): '*', (3, 2): '*',
                     (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                     (3, 8): 'X', (4, 0): 'X', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                     (4, 4): '@', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): 'X',
                     (5, 0): 'X', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                     (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): 'X', (6, 0): 'X',
                     (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                     (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '*',
                     (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                     (7, 7): '*', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                     (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        move_west(new_board)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
