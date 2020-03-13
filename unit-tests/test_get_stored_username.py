from unittest import TestCase
from load_character import get_stored_username
from load_character import store_new_character


class TestGet_stored_username(TestCase):
    def test_example1_get_stored_username(self):
        character_dictionary = {'Charisma': 5, 'Class': 'Imperial Agent', 'Constitution:': 4, 'Dexterity': 7, 'HP': 10,
                                'Intelligence': 14, 'Inventory': 'Sniper Rifle', 'Name': 'Dustin', 'Position': [6, 4],
                                'Strength': 6, 'Wisdom': 18, 'XP': 0}
        store_new_character(character_dictionary)
        self.assertEqual(get_stored_username(), character_dictionary)

    def test_example2_get_stored_username(self):
        character_dictionary = {'Charisma': 18, 'Class': 'Smuggler', 'Constitution:': 4, 'Dexterity': 7, 'HP': 10,
                                'Intelligence': 14, 'Inventory': ['Sniper Rifle'], 'Name': 'Han Solo', 'Position': [4, 6],
                                'Strength': 6, 'Wisdom': 18, 'XP': 0}
        store_new_character(character_dictionary)
        self.assertEqual(get_stored_username(), character_dictionary)

    def test_example3_get_stored_username(self):
        character_dictionary = {'Charisma': 5, 'Class': 'Sith Warrior', 'Constitution:': 10, 'Dexterity': 7, 'HP': 10,
                                'Intelligence': 8, 'Inventory': ['Lightsaber - Red'], 'Name': 'Valkorion',
                                'Position': [4, 6], 'Strength': 18, 'Wisdom': 18, 'XP': 0}
        store_new_character(character_dictionary)
        self.assertEqual(get_stored_username(), character_dictionary)

    def test_example4_get_stored_username(self):
        character_dictionary = {'Charisma': 8, 'Class': 'Sith Inquisitor', 'Constitution:': 10, 'Dexterity': 7,
                                'HP': 10, 'Intelligence': 15, 'Inventory': ['Lightsaber - Red'],
                                'Name': 'Senator Palpatine', 'Position': [4, 6], 'Strength': 12, 'Wisdom': 18, 'XP': 0}
        store_new_character(character_dictionary)
        self.assertEqual(get_stored_username(), character_dictionary)
