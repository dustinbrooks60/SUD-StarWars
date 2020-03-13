from unittest import TestCase
from monster import monster_combat
from unittest.mock import patch
import unittest.mock
import io
import random


class TestMonster_combat(TestCase):
    @patch('monster.select_a_monster', return_value={'Name': 'Rancor', 'Class': 'Monster', 'HP': 5,
                                                     'Strength': 15, 'Dexterity': 6,
                                                     'Constitution:': 14, 'Intelligence': 2, 'Wisdom': 1,
                                                     'Charisma': 1, 'XP': 0, 'Inventory': []})
    @patch('builtins.input', return_value='n')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_combat(self, mock_stdout, mock_select_a_monster, mock_input):
        random.seed(1)
        new_character = {"Name": "Dustin", "Class": "Imperial Agent", "HP": 10, "Strength": 17, "Dexterity": 5,
                         "Constitution:": 13, "Intelligence": 3, "Wisdom": 9, "Charisma": 3, "XP": 0,
                         "Inventory": "Sniper Rifle", "Position": [2, 4]}
        expected_output = """You've encountered a Rancor!

You successfully ran away without taking damage!\n"""
        monster_combat(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('monster.select_a_monster', return_value={'Name': 'Krayt Dragon', 'Class': 'Monster', 'HP': 5,
                                                     'Strength': 18, 'Dexterity': 8,
                                                     'Constitution:': 16, 'Intelligence': 6, 'Wisdom': 8,
                                                     'Charisma': 3, 'XP': 0, 'Inventory': []})
    @patch('builtins.input', return_value='y')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_2nd_monster_combat(self, mock_stdout, mock_select_a_monster, mock_input):
        random.seed(3)
        new_character = {"Name": "Dustin", "Class": "Imperial Agent", "HP": 10, "Strength": 17, "Dexterity": 5,
                         "Constitution:": 13, "Intelligence": 3, "Wisdom": 9, "Charisma": 3, "XP": 0,
                         "Inventory": "Sniper Rifle", "Position": [2, 4]}
        expected_output = """You've encountered a Krayt Dragon!

Dustin hits for 2
The new health of the Krayt Dragon is 3
The Krayt Dragon hits for 5
The new health of Dustin is 5
Dustin hits for 5
The new health of the Krayt Dragon is -2
The Krayt Dragon has died\n"""
        monster_combat(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('monster.select_a_monster', return_value={'Name': 'Krayt Dragon', 'Class': 'Monster', 'HP': 5,
                                                     'Strength': 18, 'Dexterity': 8,
                                                     'Constitution:': 16, 'Intelligence': 6, 'Wisdom': 8,
                                                     'Charisma': 3, 'XP': 0, 'Inventory': []})
    @patch('builtins.input', return_value='y')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_3rd_monster_combat(self, mock_stdout, mock_select_a_monster, mock_input):
        random.seed(2)
        new_character = {"Name": "Dustin", "Class": "Imperial Agent", "HP": 10, "Strength": 17, "Dexterity": 5,
                         "Constitution:": 13, "Intelligence": 3, "Wisdom": 9, "Charisma": 3, "XP": 0,
                         "Inventory": "Sniper Rifle", "Position": [2, 4]}
        expected_output = """You've encountered a Krayt Dragon!

Dustin hits for 1
The new health of the Krayt Dragon is 4
The Krayt Dragon hits for 1
The new health of Dustin is 9
Dustin hits for 1
The new health of the Krayt Dragon is 3
The Krayt Dragon hits for 3
The new health of Dustin is 6
Dustin hits for 2
The new health of the Krayt Dragon is 1
The Krayt Dragon hits for 6
The new health of Dustin is 0
Dustin has died
"""
        monster_combat(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('monster.select_a_monster', return_value={'Name': 'Krayt Dragon', 'Class': 'Monster', 'HP': 5,
                                                     'Strength': 18, 'Dexterity': 8,
                                                     'Constitution:': 16, 'Intelligence': 6, 'Wisdom': 8,
                                                     'Charisma': 3, 'XP': 0, 'Inventory': []})
    @patch('builtins.input', return_value='n')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_4th_monster_combat(self, mock_stdout, mock_select_a_monster, mock_input):
        random.seed(19)
        new_character = {"Name": "Dustin", "Class": "Imperial Agent", "HP": 10, "Strength": 17, "Dexterity": 5,
                         "Constitution:": 13, "Intelligence": 3, "Wisdom": 9, "Charisma": 3, "XP": 0,
                         "Inventory": "Sniper Rifle", "Position": [2, 4]}
        expected_output = """You've encountered a Krayt Dragon!

You ran away, but took 1 damage
"""
        monster_combat(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()