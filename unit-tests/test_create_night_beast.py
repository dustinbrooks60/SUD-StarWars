from unittest import TestCase
from monster import create_night_beast

class TestCreate_night_beast(TestCase):
    def test_create_night_beast(self):
        expected_output = {'Name': 'Night Beast', 'Class': 'Monster', 'HP': 5,
                          'Strength': 8, 'Dexterity': 16,
                          'Constitution:': 8, 'Intelligence': 16, 'Wisdom': 5,
                          'Charisma': 5, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_night_beast(), expected_output)

    def test_proper_dictionary_create_night_beast(self):
        new_beast = create_night_beast()
        self.assertIsInstance(new_beast, dict)

    def test_length_dictionary_create_night_beast(self):
        new_beast = create_night_beast()
        length_of_dict = len(new_beast)
        self.assertEqual(length_of_dict, 11)
