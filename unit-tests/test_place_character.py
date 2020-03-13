from unittest import TestCase
import sud

class TestPlace_character(TestCase):
    def test_top_left_place_character(self):
        new_board = sud.create_game_board()
        new_board = sud.set_border(new_board)
        expected_output = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                           (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                           (1, 1): '@', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                           (1, 6): '*', (1, 7): '*', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
                           (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                           (2, 7): '*', (2, 8): 'X', (3, 0): 'X', (3, 1): '*', (3, 2): '*',
                           (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                           (3, 8): 'X', (4, 0): 'X', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                           (4, 4): '*', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): 'X',
                           (5, 0): 'X', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                           (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): 'X', (6, 0): 'X',
                           (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                           (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '*',
                           (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                           (7, 7): '*', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                           (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18, 'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': ['Blaster Pistol'], 'Position': [1, 1]}
        self.assertEqual(sud.place_character(new_board, new_character), expected_output)

    def test_bottom_left_place_character(self):
        new_board = sud.create_game_board()
        new_board = sud.set_border(new_board)
        expected_output = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                           (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                           (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                           (1, 6): '*', (1, 7): '*', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
                           (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                           (2, 7): '*', (2, 8): 'X', (3, 0): 'X', (3, 1): '*', (3, 2): '*',
                           (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                           (3, 8): 'X', (4, 0): 'X', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                           (4, 4): '*', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): 'X',
                           (5, 0): 'X', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                           (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): 'X', (6, 0): 'X',
                           (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                           (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '@',
                           (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                           (7, 7): '*', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                           (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18, 'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': ['Blaster Pistol'], 'Position': [7, 1]}
        self.assertEqual(sud.place_character(new_board, new_character), expected_output)

    def test_top_right_place_character(self):
        new_board = sud.create_game_board()
        new_board = sud.set_border(new_board)
        expected_output = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                           (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                           (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                           (1, 6): '*', (1, 7): '@', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
                           (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                           (2, 7): '*', (2, 8): 'X', (3, 0): 'X', (3, 1): '*', (3, 2): '*',
                           (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                           (3, 8): 'X', (4, 0): 'X', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                           (4, 4): '*', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): 'X',
                           (5, 0): 'X', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                           (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): 'X', (6, 0): 'X',
                           (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                           (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '*',
                           (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                           (7, 7): '*', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                           (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18, 'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': ['Blaster Pistol'], 'Position': [1, 7]}
        self.assertEqual(sud.place_character(new_board, new_character), expected_output)

    def test_bottom_right_place_character(self):
        new_board = sud.create_game_board()
        new_board = sud.set_border(new_board)
        expected_output = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                           (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                           (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                           (1, 6): '*', (1, 7): '*', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
                           (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                           (2, 7): '*', (2, 8): 'X', (3, 0): 'X', (3, 1): '*', (3, 2): '*',
                           (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                           (3, 8): 'X', (4, 0): 'X', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                           (4, 4): '*', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): 'X',
                           (5, 0): 'X', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                           (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): 'X', (6, 0): 'X',
                           (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                           (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '*',
                           (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                           (7, 7): '@', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                           (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18, 'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': ['Blaster Pistol'], 'Position': [7, 7]}
        self.assertEqual(sud.place_character(new_board, new_character), expected_output)

    def test_middle_place_character(self):
        new_board = sud.create_game_board()
        new_board = sud.set_border(new_board)
        expected_output = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X', (0, 4): ' ',
                           (0, 5): 'X', (0, 6): 'X', (0, 7): 'X', (0, 8): 'X', (1, 0): 'X',
                           (1, 1): '*', (1, 2): '*', (1, 3): '*', (1, 4): '*', (1, 5): '*',
                           (1, 6): '*', (1, 7): '*', (1, 8): 'X', (2, 0): 'X', (2, 1): '*',
                           (2, 2): '*', (2, 3): '*', (2, 4): '*', (2, 5): '*', (2, 6): '*',
                           (2, 7): '*', (2, 8): 'X', (3, 0): 'X', (3, 1): '*', (3, 2): '*',
                           (3, 3): '*', (3, 4): '*', (3, 5): '*', (3, 6): '*', (3, 7): '*',
                           (3, 8): 'X', (4, 0): 'X', (4, 1): '*', (4, 2): '*', (4, 3): '*',
                           (4, 4): '@', (4, 5): '*', (4, 6): '*', (4, 7): '*', (4, 8): 'X',
                           (5, 0): 'X', (5, 1): '*', (5, 2): '*', (5, 3): '*', (5, 4): '*',
                           (5, 5): '*', (5, 6): '*', (5, 7): '*', (5, 8): 'X', (6, 0): 'X',
                           (6, 1): '*', (6, 2): '*', (6, 3): '*', (6, 4): '*', (6, 5): '*',
                           (6, 6): '*', (6, 7): '*', (6, 8): 'X', (7, 0): 'X', (7, 1): '*',
                           (7, 2): '*', (7, 3): '*', (7, 4): '*', (7, 5): '*', (7, 6): '*',
                           (7, 7): '*', (7, 8): 'X', (8, 0): 'X', (8, 1): 'X', (8, 2): 'X',
                           (8, 3): 'X', (8, 4): 'X', (8, 5): 'X', (8, 6): 'X', (8, 7): 'X', (8, 8): 'X'}
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18, 'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': ['Blaster Pistol'], 'Position': [4, 4]}
        self.assertEqual(sud.place_character(new_board, new_character), expected_output)

    def test_error_place_character(self):
        new_board = sud.create_game_board()
        new_board = sud.set_border(new_board)
        new_character = {'Name': 'Dustin', 'Class': 'Smuggler', 'HP': 10,
                         'Strength': 18, 'Dexterity': 18,
                         'Constitution:': 18, 'Intelligence': 18, 'Wisdom': 18,
                         'Charisma': 18, 'XP': 0, 'Inventory': ['Blaster Pistol'], 'Position': [8, 9]}
        self.assertRaises(TypeError, sud.place_character(new_board, new_character))