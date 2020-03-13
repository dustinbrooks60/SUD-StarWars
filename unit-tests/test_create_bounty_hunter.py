from unittest import TestCase
from monster import create_bounty_hunter

class TestCreate_bounty_hunter(TestCase):
    def test_create_bounty_hunter(self):
        expected_output = {'Name': 'Bounty Hunter', 'Class': 'Monster', 'HP': 5,
                           'Strength': 6, 'Dexterity': 16,
                           'Constitution:': 10, 'Intelligence': 17, 'Wisdom': 13,
                           'Charisma': 18, 'XP': 0, 'Inventory': []}
        self.assertEqual(create_bounty_hunter(), expected_output)

    def test_proper_dictionary_create_bounty_hunter(self):
        new_bounty = create_bounty_hunter()
        self.assertIsInstance(new_bounty, dict)

    def test_length_dictionary_create_bounty_hunter(self):
        new_bounty = create_bounty_hunter()
        length_of_dict = len(new_bounty)
        self.assertEqual(length_of_dict, 11)
