from unittest import TestCase
from monster import create_dianoga


class TestCreate_dianoga(TestCase):
    def test_create_dianoga(self):
        expected_output = {'Name': 'Dianoga', 'Class': 'Monster', 'HP': 5,
                              'Strength': 12, 'Dexterity': 13,
                              'Constitution:': 12, 'Intelligence': 14, 'Wisdom': 5,
                              'Charisma': 1, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_dianoga(), expected_output)

    def test_proper_dictionary_create_dianoga(self):
        new_dianoga = create_dianoga()
        self.assertIsInstance(new_dianoga, dict)

    def test_length_dictionary_create_dianoga(self):
        new_dianoga = create_dianoga()
        length_of_dict = len(new_dianoga)
        self.assertEqual(length_of_dict, 11)
