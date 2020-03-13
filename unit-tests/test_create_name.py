from unittest import TestCase
from unittest.mock import patch
from character import create_name


class TestCreate_name(TestCase):
    @patch('builtins.input', return_value='Dustin')
    def test_example1_create_name(self, mock_stdout):
        self.assertEqual(create_name(), 'Dustin')

    @patch('builtins.input', return_value='Han Solo')
    def test_example2_create_name(self, mock_stdout):
        self.assertEqual(create_name(), 'Han Solo')

    @patch('builtins.input', return_value='Darth Vader')
    def test_example3_create_name(self, mock_stdout):
        self.assertEqual(create_name(), 'Darth Vader')

    @patch('builtins.input', return_value='Luke Skywalker')
    def test_example4_create_name(self, mock_stdout):
        self.assertEqual(create_name(), 'Luke Skywalker')

    @patch('builtins.input', return_value='Luke Skywalker')
    def test_type_create_name(self, mock_stdout):
        self.assertIsInstance(create_name(), str)
