from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
from load_character import new_or_old_character
from load_character import store_new_character


class TestNew_or_old_character(TestCase):
    @patch('builtins.input', return_value='y')
    @patch('character.class_selection', return_value='Jedi Consular')
    @patch('character.create_name', return_value='Dustin')
    @patch('character.roll_die', side_effect=[8, 8, 8, 8, 8, 8])
    def test_first_option_new_or_old_character(self, mock_new_or_old_character, mock_create_character, mock_create_name,
                                               mock_roll_die):
        new_character = {"Name": "Dustin", "Class": "Jedi Consular", "HP": 10, "Strength": 8, "Dexterity": 8,
                         "Constitution:": 8, "Intelligence": 8, "Wisdom": 8, "Charisma": 8, "XP": 0,
                         "Inventory": ["Lightsaber - Orange"], "Position": [7, 4]}
        self.assertEqual(new_or_old_character(), new_character)

    @patch('builtins.input', return_value='n')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_second_option_new_or_old_character(self, mock_new_or_old_character, mock_create_character):
        old_character = {"Name": "Dustin", "Class": "Imperial Agent", "HP": 10, "Strength": 17, "Dexterity": 5,
                         "Constitution:": 13, "Intelligence": 3, "Wisdom": 9, "Charisma": 3, "XP": 0,
                         "Inventory": "Sniper Rifle", "Position": [2, 4]}
        store_new_character(old_character)
        self.assertEqual(new_or_old_character(), old_character)

    @patch('builtins.input', side_effect=['t', 'n'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_error_option_new_or_old_character(self, mock_stdout, mock_error):
        expected_output = """Please enter y or n
Welcome back, Dustin\n"""
        new_or_old_character()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['t', 'y'])
    @patch('character.class_selection', return_value='Jedi Consular')
    @patch('character.create_name', return_value='Dustin')
    @patch('character.roll_die', side_effect=[8, 8, 8, 8, 8, 8])
    def test_error2_option_new_or_old_character(self, mock_new_or_old_character, mock_create_character, mock_create_name,
                                               mock_roll_die):
        new_character = {"Name": "Dustin", "Class": "Jedi Consular", "HP": 10, "Strength": 8, "Dexterity": 8,
                         "Constitution:": 8, "Intelligence": 8, "Wisdom": 8, "Charisma": 8, "XP": 0,
                         "Inventory": ["Lightsaber - Orange"], "Position": [7, 4]}
        self.assertEqual(new_or_old_character(), new_character)
