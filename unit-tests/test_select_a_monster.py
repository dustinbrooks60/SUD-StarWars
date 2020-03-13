from unittest import TestCase
from monster import select_a_monster
import random


class TestSelect_a_monster(TestCase):
    def test_rancor_select_a_monster(self):
        random.seed(19)
        rancor_dictionary = {'Name': 'Rancor', 'Class': 'Monster', 'HP': 5,
                              'Strength': 15, 'Dexterity': 6,
                              'Constitution:': 14, 'Intelligence': 2, 'Wisdom': 1,
                              'Charisma': 1, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), rancor_dictionary)
        random.seed()

    def test_rathtar_select_a_monster(self):
        random.seed(6)
        rathtar_dictionary = {'Name': 'Rathtar', 'Class': 'Monster', 'HP': 5,
                          'Strength': 14, 'Dexterity': 17,
                          'Constitution:': 10, 'Intelligence': 10, 'Wisdom': 1,
                          'Charisma': 1, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), rathtar_dictionary)
        random.seed()

    def test_dianoga_select_a_monster(self):
        random.seed(1)
        dianoga_dictionary = {'Name': 'Dianoga', 'Class': 'Monster', 'HP': 5,
                          'Strength': 12, 'Dexterity': 13,
                          'Constitution:': 12, 'Intelligence': 14, 'Wisdom': 5,
                          'Charisma': 1, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), dianoga_dictionary)
        random.seed()

    def test_krayt_select_a_monster(self):
        random.seed(4)
        krayt_dictionary = {'Name': 'Krayt Dragon', 'Class': 'Monster', 'HP': 5,
                          'Strength': 18, 'Dexterity': 8,
                          'Constitution:': 16, 'Intelligence': 6, 'Wisdom': 8,
                          'Charisma': 3, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), krayt_dictionary)
        random.seed()

    def test_night_beast_select_a_monster(self):
        random.seed(5)
        beast_dictionary = {'Name': 'Night Beast', 'Class': 'Monster', 'HP': 5,
                          'Strength': 8, 'Dexterity': 16,
                          'Constitution:': 8, 'Intelligence': 16, 'Wisdom': 5,
                          'Charisma': 5, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), beast_dictionary)
        random.seed()

    def test_corrupted_jedi_select_a_monster(self):
        random.seed(7)
        corrupted_dictionary = {'Name': 'Corrupted Jedi', 'Class': 'Monster', 'HP': 5,
                          'Strength': 8, 'Dexterity': 14,
                          'Constitution:': 15, 'Intelligence': 16, 'Wisdom': 16,
                          'Charisma': 15, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), corrupted_dictionary)
        random.seed()

    def test_bounty_select_a_monster(self):
        random.seed(17)
        bounty_dictionary = {'Name': 'Bounty Hunter', 'Class': 'Monster', 'HP': 5,
                          'Strength': 6, 'Dexterity': 16,
                          'Constitution:': 10, 'Intelligence': 17, 'Wisdom': 13,
                          'Charisma': 18, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), bounty_dictionary)
        random.seed()

    def test_tusken_select_a_monster(self):
        random.seed(27)
        tusken_dictionary = {'Name': 'Tusken Raider', 'Class': 'Monster', 'HP': 5,
                          'Strength': 5, 'Dexterity': 10,
                          'Constitution:': 12, 'Intelligence': 12, 'Wisdom': 5,
                          'Charisma': 2, 'XP': 0, 'Inventory': []}
        self.assertEqual(select_a_monster(), tusken_dictionary)
        random.seed()
