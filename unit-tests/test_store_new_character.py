from unittest import TestCase
from load_character import store_new_character
import unittest.mock
import io
from os import path


class TestStore_new_character(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_store1_new_character(self, mock_stdout):
        new_character = {'Charisma': 5, 'Class': 'Jedi Knight', 'Constitution:': 4, 'Dexterity': 7, 'HP': 6,
         'Intelligence': 14, 'Inventory': 'Lightsaber - Blue', 'Name': 'Dustin', 'Position': [3, 4],
         'Strength': 6, 'Wisdom': 18, 'XP': 0}
        expected_output = "Thanks for playing! We'll remember you when you come back, Dustin\n"
        store_new_character(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_store2_new_character(self, mock_stdout):
        new_character = {'Charisma': 5, 'Class': 'Jedi Consular', 'Constitution:': 4, 'Dexterity': 7, 'HP': 6,
         'Intelligence': 14, 'Inventory': 'Lightsaber - Orange', 'Name': 'Qwerty', 'Position': [4, 6],
         'Strength': 6, 'Wisdom': 18, 'XP': 0}
        expected_output = "Thanks for playing! We'll remember you when you come back, Qwerty\n"
        store_new_character(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_store3_new_character(self, mock_stdout):
        new_character = {'Charisma': 5, 'Class': 'Sith Warrior', 'Constitution:': 4, 'Dexterity': 7, 'HP': 6,
         'Intelligence': 14, 'Inventory': 'Lightsaber - Red', 'Name': 'Destroyer of Worlds', 'Position': [1, 1],
         'Strength': 6, 'Wisdom': 18, 'XP': 0}
        expected_output = "Thanks for playing! We'll remember you when you come back, Destroyer of Worlds\n"
        store_new_character(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_store4_new_character(self, mock_stdout):
        new_character = {'Charisma': 5, 'Class': 'Imperial Agent', 'Constitution:': 10, 'Dexterity': 7, 'HP': 6,
         'Intelligence': 18, 'Inventory': 'Blaster Rifle', 'Name': 'IG-88', 'Position': [2, 7],
         'Strength': 6, 'Wisdom': 5, 'XP': 0}
        expected_output = "Thanks for playing! We'll remember you when you come back, IG-88\n"
        store_new_character(new_character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_file_exists_store_new_character(self):
        self.assertTrue(path.exists("username.json"))


