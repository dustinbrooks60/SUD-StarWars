from unittest import TestCase
from monster import create_tusken_raider


class TestCreate_tusken_raider(TestCase):
    def test_create_tusken_raider(self):
        expected_output = {'Name': 'Tusken Raider', 'Class': 'Monster', 'HP': 5,
                           'Strength': 5, 'Dexterity': 10,
                           'Constitution:': 12, 'Intelligence': 12, 'Wisdom': 5,
                           'Charisma': 2, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_tusken_raider(), expected_output)

    def test_proper_dictionary_create_tusken_raider(self):
        new_raider = create_tusken_raider()
        self.assertIsInstance(new_raider, dict)

    def test_length_dictionary_create_tusken_raider(self):
        new_raider = create_tusken_raider()
        length_of_dict = len(new_raider)
        self.assertEqual(length_of_dict, 11)
