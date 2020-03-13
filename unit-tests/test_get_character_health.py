from unittest import TestCase
from character import get_character_health
import unittest.mock
import io


class TestGet_character_health(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_max_get_character_health(self, mock_stdout):
        character_dictionary = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                                'Strength': 18, 'Dexterity': 18,
                                'Constitution:': 18, 'Intelligence': 18,
                                'Wisdom': 18,
                                'Charisma': 18, 'XP': 0, 'Inventory': ['Sniper Rifle'], 'Position': [7, 4]}
        expected_output = "Your health is: 10\n"
        get_character_health(character_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_middle_get_character_health(self, mock_stdout):
        character_dictionary = {'Name': 'Grand Moff Tarkin', 'Class': 'Imperial Agent', 'HP': 5,
                                'Strength': 18, 'Dexterity': 18,
                                'Constitution:': 18, 'Intelligence': 18,
                                'Wisdom': 18,
                                'Charisma': 18, 'XP': 0, 'Inventory': ['Blaster Pistol'], 'Position': [7, 4]}
        expected_output = "Your health is: 5\n"
        get_character_health(character_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_lowest_get_character_health(self, mock_stdout):
        character_dictionary = {'Name': 'Ahsoka Tano', 'Class': 'Jedi Knight', 'HP': 1,
                                'Strength': 18, 'Dexterity': 18,
                                'Constitution:': 18, 'Intelligence': 18,
                                'Wisdom': 18,
                                'Charisma': 18, 'XP': 0, 'Inventory': ["Lightsaber - Blue"], 'Position': [7, 4]}
        expected_output = "Your health is: 1\n"
        get_character_health(character_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)