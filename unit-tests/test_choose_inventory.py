from unittest import TestCase
from unittest.mock import patch
from character import choose_inventory
import unittest.mock
import io


class TestChoose_inventory(TestCase):
    @patch('builtins.input', return_value='1')
    def test_first_item_choose_inventory(self, mock_choose_inventory):
        expected_output = ['Blaster Pistol']
        self.assertEqual(choose_inventory(), expected_output)

    @patch('builtins.input', return_value='2')
    def test_second_item_choose_inventory(self, mock_choose_inventory):
        expected_output = ['Blaster Rifle']
        self.assertEqual(choose_inventory(), expected_output)

    @patch('builtins.input', return_value='3')
    def test_third_item_choose_inventory(self, mock_choose_inventory):
        expected_output = ['Assault Cannon']
        self.assertEqual(choose_inventory(), expected_output)

    @patch('builtins.input', return_value='4')
    def test_fourth_item_choose_inventory(self, mock_choose_inventory):
        expected_output = ['Sniper Rifle']
        self.assertEqual(choose_inventory(), expected_output)

    @patch('builtins.input', side_effect=['5', '2'])
    def test_error_item_choose_inventory(self, mock_choose_inventory):
        self.assertEqual(choose_inventory(), None)