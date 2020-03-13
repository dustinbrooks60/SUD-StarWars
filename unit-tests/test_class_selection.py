from unittest import TestCase
from character import class_selection
from unittest.mock import patch

class TestClass_selection(TestCase):
    @patch('builtins.input', return_value='1')
    def test_first_class_selection(self, mock_choose_inventory):
        expected_output = 'Bounty Hunter'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', return_value='2')
    def test_second_class_selection(self, mock_choose_inventory):
        expected_output = 'Imperial Agent'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', return_value='3')
    def test_third_class_selection(self, mock_choose_inventory):
        expected_output = 'Jedi Consular'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', return_value='4')
    def test_fourth_class_selection(self, mock_choose_inventory):
        expected_output = 'Jedi Knight'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', return_value='5')
    def test_fifth_class_selection(self, mock_choose_inventory):
        expected_output = 'Sith Warrior'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', return_value='6')
    def test_sixth_class_selection(self, mock_choose_inventory):
        expected_output = 'Sith Inquisitor'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', return_value='7')
    def test_seventh_class_selection(self, mock_choose_inventory):
        expected_output = 'Smuggler'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', return_value='8')
    def test_eighth_class_selection(self, mock_choose_inventory):
        expected_output = 'Trooper'
        self.assertEqual(class_selection(), expected_output)

    @patch('builtins.input', side_effect=['9', '2'])
    def test_error_class_selection(self, mock_choose_inventory):
        self.assertEqual(class_selection(), None)