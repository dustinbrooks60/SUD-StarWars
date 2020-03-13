from unittest import TestCase
from monster import create_rancor


class TestCreate_rancor(TestCase):
    def test_create_rancor(self):
        expected_output = {'Name': 'Rancor', 'Class': 'Monster', 'HP': 5,
                              'Strength': 15, 'Dexterity': 6,
                              'Constitution:': 14, 'Intelligence': 2, 'Wisdom': 1,
                              'Charisma': 1, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_rancor(), expected_output)

    def test_proper_dictionary_create_rancor(self):
        new_rancor = create_rancor()
        self.assertIsInstance(new_rancor, dict)

    def test_length_dictionary_create_rancor(self):
        new_rancor = create_rancor()
        length_of_dict = len(new_rancor)
        self.assertEqual(length_of_dict, 11)
