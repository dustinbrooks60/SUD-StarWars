from unittest import TestCase
from unittest.mock import patch
from character import combat_to_death
import unittest.mock
import io
import random


class TestCombat_to_death(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('character.roll_die', side_effect=[2, 2, 8])
    def test_example1_combat_to_death(self, mock_roll_die, mock_stdout):
        new_character1 = {"Name": "Boba Fett", "Class": "Bounty Hunter", "HP": 10, "Strength": 16, "Dexterity": 14,
                          "Constitution:": 13, "Intelligence": 16, "Wisdom": 14, "Charisma": 16, "XP": 0,
                          "Inventory": ["Sniper Rifle"], "Position": [7, 4]}
        new_character2 = {"Name": "Sarlacc Pitt", "Class": "Monster", "HP": 10, "Strength": 18, "Dexterity": 18,
                          "Constitution:": 18, "Intelligence": 18, "Wisdom": 18, "Charisma": 18, "XP": 0,
                          "Inventory": [], "Position": [7, 4]}
        expected_output = """Boba Fett hits for 2
The new health of the Sarlacc Pitt is 8
The Sarlacc Pitt hits for 2
The new health of Boba Fett is 8
Boba Fett hits for 8
The new health of the Sarlacc Pitt is 0
The Sarlacc Pitt has died\n"""
        combat_to_death(new_character1, new_character2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('character.roll_die', side_effect=[2, 2, 4, 4, 4])
    def test_example2_combat_to_death(self, mock_roll_die, mock_stdout):
        new_character1 = {"Name": "Han Solo", "Class": "Smuggler", "HP": 10, "Strength": 16, "Dexterity": 14,
                              "Constitution:": 13, "Intelligence": 16, "Wisdom": 14, "Charisma": 16, "XP": 0,
                              "Inventory": ["Blaster Pistol"], "Position": [7, 4]}
        new_character2 = {"Name": "Carbonite Imprisonment", "Class": "Monster", "HP": 10, "Strength": 18,
                              "Dexterity": 18, "Constitution:": 18, "Intelligence": 18, "Wisdom": 18, "Charisma": 18,
                              "XP": 0, "Inventory": [], "Position": [7, 4]}
        expected_output = """Han Solo hits for 2
The new health of the Carbonite Imprisonment is 8
The Carbonite Imprisonment hits for 2
The new health of Han Solo is 8
Han Solo hits for 4
The new health of the Carbonite Imprisonment is 4
The Carbonite Imprisonment hits for 4
The new health of Han Solo is 4
Han Solo hits for 4
The new health of the Carbonite Imprisonment is 0
The Carbonite Imprisonment has died\n"""
        combat_to_death(new_character1, new_character2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('character.roll_die', side_effect=[2, 2, 4, 4, 1, 4])
    def test_example3_combat_to_death(self, mock_roll_die, mock_stdout):
        new_character1 = {"Name": "Princess Leia", "Class": "Princess", "HP": 10, "Strength": 16, "Dexterity": 14,
                              "Constitution:": 13, "Intelligence": 16, "Wisdom": 14, "Charisma": 16, "XP": 0,
                              "Inventory": ["Blaster Pistol"], "Position": [7, 4]}
        new_character2 = {"Name": "Void of Space", "Class": "Monster", "HP": 10, "Strength": 18,
                              "Dexterity": 18, "Constitution:": 18, "Intelligence": 18, "Wisdom": 18, "Charisma": 18,
                              "XP": 0, "Inventory": [], "Position": [7, 4]}
        expected_output = """Princess Leia hits for 2
The new health of the Void of Space is 8
The Void of Space hits for 2
The new health of Princess Leia is 8
Princess Leia hits for 4
The new health of the Void of Space is 4
The Void of Space hits for 4
The new health of Princess Leia is 4
Princess Leia hits for 1
The new health of the Void of Space is 3
The Void of Space hits for 4
The new health of Princess Leia is 0
Princess Leia has died\n"""
        combat_to_death(new_character1, new_character2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('character.roll_die', side_effect=[1, 1, 1, 1, 1, 1, 6, 7])
    def test_example4_combat_to_death(self, mock_roll_die, mock_stdout):
        new_character1 = {"Name": "Snoke", "Class": "Sith Emperor", "HP": 10, "Strength": 16, "Dexterity": 14,
                              "Constitution:": 13, "Intelligence": 16, "Wisdom": 14, "Charisma": 16, "XP": 0,
                              "Inventory": ["Lightsaber - Red"], "Position": [7, 4]}
        new_character2 = {"Name": "Kylo Ren", "Class": "", "HP": 10, "Strength": 18,
                              "Dexterity": 18, "Constitution:": 18, "Intelligence": 18, "Wisdom": 18, "Charisma": 18,
                              "XP": 0, "Inventory": ["Lightsaber - Red"], "Position": [7, 4]}
        expected_output = """Snoke hits for 1
The new health of the Kylo Ren is 9
The Kylo Ren hits for 1
The new health of Snoke is 9
Snoke hits for 1
The new health of the Kylo Ren is 8
The Kylo Ren hits for 1
The new health of Snoke is 8
Snoke hits for 1
The new health of the Kylo Ren is 7
The Kylo Ren hits for 1
The new health of Snoke is 7
Snoke hits for 6
The new health of the Kylo Ren is 1
The Kylo Ren hits for 7
The new health of Snoke is 0
Snoke has died\n"""
        combat_to_death(new_character1, new_character2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
