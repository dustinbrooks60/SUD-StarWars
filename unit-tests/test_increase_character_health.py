from unittest import TestCase
from character import increase_character_health


class TestIncrease_character_health(TestCase):
    def test_no_increase_character_health(self):
        character_dictionary = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                                'Strength': 18, 'Dexterity': 18,
                                'Constitution:': 18, 'Intelligence': 18,
                                'Wisdom': 18,
                                'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        expected_output = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                           'Strength': 18, 'Dexterity': 18,
                           'Constitution:': 18, 'Intelligence': 18,
                           'Wisdom': 18,
                           'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        increase_character_health(character_dictionary)
        self.assertEqual(character_dictionary, expected_output)

    def test_increase_by_1_character_health(self):
        character_dictionary = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 9,
                                'Strength': 18, 'Dexterity': 18,
                                'Constitution:': 18, 'Intelligence': 18,
                                'Wisdom': 18,
                                'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        expected_output = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                           'Strength': 18, 'Dexterity': 18,
                           'Constitution:': 18, 'Intelligence': 18,
                           'Wisdom': 18,
                           'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        increase_character_health(character_dictionary)
        self.assertEqual(character_dictionary, expected_output)

    def test_middle_increase_character_health(self):
        character_dictionary = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 4,
                                'Strength': 18, 'Dexterity': 18,
                                'Constitution:': 18, 'Intelligence': 18,
                                'Wisdom': 18,
                                'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        expected_output = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 5,
                           'Strength': 18, 'Dexterity': 18,
                           'Constitution:': 18, 'Intelligence': 18,
                           'Wisdom': 18,
                           'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        increase_character_health(character_dictionary)
        self.assertEqual(character_dictionary, expected_output)

    def test_lowest_increase_character_health(self):
        character_dictionary = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 1,
                                'Strength': 18, 'Dexterity': 18,
                                'Constitution:': 18, 'Intelligence': 18,
                                'Wisdom': 18,
                                'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        expected_output = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 2,
                           'Strength': 18, 'Dexterity': 18,
                           'Constitution:': 18, 'Intelligence': 18,
                           'Wisdom': 18,
                           'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        increase_character_health(character_dictionary)
        self.assertEqual(character_dictionary, expected_output)