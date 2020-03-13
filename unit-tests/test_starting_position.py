from unittest import TestCase
import sud
from unittest.mock import patch
import unittest.mock
import io


class TestStarting_position(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_position(self, mock_stdout):
        new_board = sud.create_game_board()
        new_board = sud.set_border(new_board)
        new_board = sud.starting_position(new_board)
        expected_output = """Your starting position is: 
X X X X   X X X X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * * * * * X 
X * * * @ * * * X 
X X X X X X X X X \n"""
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_error_starting_position(self):
        new_board = ()
        with self.assertRaises(TypeError):
            self.test_error_starting_position(new_board)