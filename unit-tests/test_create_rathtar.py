from unittest import TestCase
from monster import create_rathtar

class TestCreate_rathtar(TestCase):
    def test_create_rathtar(self):
        expected_output = {'Name': 'Rathtar', 'Class': 'Monster', 'HP': 5,
                              'Strength': 14, 'Dexterity': 17,
                              'Constitution:': 10, 'Intelligence': 10, 'Wisdom': 1,
                              'Charisma': 1, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_rathtar(), expected_output)

    def test_proper_dictionary_create_rathtar(self):
        new_rathtar = create_rathtar()
        self.assertIsInstance(new_rathtar, dict)

    def test_length_dictionary_create_rathtar(self):
        new_rathtar = create_rathtar()
        length_of_dict = len(new_rathtar)
        self.assertEqual(length_of_dict, 11)