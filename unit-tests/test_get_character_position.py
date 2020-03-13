from unittest import TestCase
from character import get_character_position


class TestGet_character_position(TestCase):
    def test_origin_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 4]}
        self.assertEqual(get_character_position(new_character), [7, 4])

    def test_middle_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [4, 4]}
        self.assertEqual(get_character_position(new_character), [4, 4])

    def test_end_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [1, 4]}
        self.assertEqual(get_character_position(new_character), [1, 4])

    def test_top_left_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [1, 1]}
        self.assertEqual(get_character_position(new_character), [1, 1])

    def test_top_right_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [1, 7]}
        self.assertEqual(get_character_position(new_character), [1, 7])

    def test_bottom_left_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 1]}
        self.assertEqual(get_character_position(new_character), [7, 1])

    def test_bottom_right_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 7]}
        self.assertEqual(get_character_position(new_character), [7, 7])

    def test_type_get_character_position(self):
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18,
                         'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': [], 'Position': [7, 7]}
        self.assertIsInstance(get_character_position(new_character), list)