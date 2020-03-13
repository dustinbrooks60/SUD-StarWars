from unittest import TestCase
from monster import create_krayt_dragon

class TestCreate_krayt_dragon(TestCase):
    def test_create_krayt_dragon(self):
        expected_output = {'Name': 'Krayt Dragon', 'Class': 'Monster', 'HP': 5,
                              'Strength': 18, 'Dexterity': 8,
                              'Constitution:': 16, 'Intelligence': 6, 'Wisdom': 8,
                              'Charisma': 3, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_krayt_dragon(), expected_output)

    def test_proper_dictionary_create_krayt_dragon(self):
        new_krayt = create_krayt_dragon()
        self.assertIsInstance(new_krayt, dict)

    def test_length_dictionary_create_krayt_dragon(self):
        new_krayt = create_krayt_dragon()
        length_of_dict = len(new_krayt)
        self.assertEqual(length_of_dict, 11)