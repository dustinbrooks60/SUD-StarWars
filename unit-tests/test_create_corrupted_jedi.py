from unittest import TestCase
from monster import create_corrupted_jedi


class TestCreate_corrupted_jedi(TestCase):
    def test_create_corrupted_jedi(self):
        expected_output = {'Name': 'Corrupted Jedi', 'Class': 'Monster', 'HP': 5,
                           'Strength': 8, 'Dexterity': 14,
                           'Constitution:': 15, 'Intelligence': 16, 'Wisdom': 16,
                           'Charisma': 15, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_corrupted_jedi(), expected_output)

    def test_proper_dictionary_create_corrupted_jedi(self):
        new_corrupted = create_corrupted_jedi()
        self.assertIsInstance(new_corrupted, dict)

    def test_length_dictionary_create_corrupted_jedi(self):
        new_corrupted = create_corrupted_jedi()
        length_of_dict = len(new_corrupted)
        self.assertEqual(length_of_dict, 11)
