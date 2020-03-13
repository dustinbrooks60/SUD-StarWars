from unittest import TestCase
from unittest.mock import patch
from character import create_character


class TestCreate_character(TestCase):
    @patch('character.class_selection', return_value='Jedi Consular')
    @patch('character.create_name', return_value='Dustin')
    @patch('character.roll_die', side_effect=[8, 8, 8, 8, 8, 8])
    def test_regular_create_character(self, mock_class_selection, mock_create_name, mock_roll_die):
        new_character = {"Name": "Dustin", "Class": "Jedi Consular", "HP": 10, "Strength": 8, "Dexterity": 8,
                         "Constitution:": 8, "Intelligence": 8, "Wisdom": 8, "Charisma": 8, "XP": 0,
                         "Inventory": ["Lightsaber - Orange"], "Position": [7, 4]}
        self.assertEqual(create_character(), new_character)

    @patch('character.class_selection', return_value='Smuggler')
    @patch('character.create_name', return_value='Han Solo')
    @patch('character.roll_die', side_effect=[18, 18, 18, 18, 18, 18])
    @patch('character.choose_inventory', return_value=['Blaster Pistol'])
    def test_regular2_create_character(self, mock_class_selection, mock_create_name, mock_roll_die, choose_inventory):
        new_character = {"Name": "Han Solo", "Class": "Smuggler", "HP": 10, "Strength": 18, "Dexterity": 18,
                         "Constitution:": 18, "Intelligence": 18, "Wisdom": 18, "Charisma": 18, "XP": 0,
                         "Inventory": ["Blaster Pistol"], "Position": [7, 4]}
        self.assertEqual(create_character(), new_character)

    @patch('character.class_selection', return_value='Sith Warrior')
    @patch('character.create_name', return_value='Darth Vader')
    @patch('character.roll_die', side_effect=[15, 15, 15, 15, 15, 15])
    def test_regular3_create_character(self, mock_class_selection, mock_create_name, mock_roll_die):
        new_character = {"Name": "Darth Vader", "Class": "Sith Warrior", "HP": 10, "Strength": 15, "Dexterity": 15,
                         "Constitution:": 15, "Intelligence": 15, "Wisdom": 15, "Charisma": 15, "XP": 0,
                         "Inventory": ["Lightsaber - Red"], "Position": [7, 4]}
        self.assertEqual(create_character(), new_character)

    @patch('character.class_selection', return_value='Bounty Hunter')
    @patch('character.create_name', return_value='Boba Fett')
    @patch('character.roll_die', side_effect=[16, 14, 13, 16, 14, 16])
    @patch('character.choose_inventory', return_value=['Sniper Rifle'])
    def test_regular4_create_character(self, mock_class_selection, mock_create_name, mock_roll_die, choose_inventory):
        new_character = {"Name": "Boba Fett", "Class": "Bounty Hunter", "HP": 10, "Strength": 16, "Dexterity": 14,
                         "Constitution:": 13, "Intelligence": 16, "Wisdom": 14, "Charisma": 16, "XP": 0,
                         "Inventory": ["Sniper Rifle"], "Position": [7, 4]}
        self.assertEqual(create_character(), new_character)

    @patch('character.class_selection', return_value='Trooper')
    @patch('character.create_name', return_value='Commander Cody')
    @patch('character.roll_die', side_effect=[18, 9, 16, 15, 5, 5])
    @patch('character.choose_inventory', return_value=['Assault Cannon'])
    def test_regular5_create_character(self, mock_class_selection, mock_create_name, mock_roll_die, choose_inventory):
        new_character = {"Name": "Commander Cody", "Class": "Trooper", "HP": 10, "Strength": 18, "Dexterity": 9,
                         "Constitution:": 16, "Intelligence": 15, "Wisdom": 5, "Charisma": 5, "XP": 0,
                         "Inventory": ["Assault Cannon"], "Position": [7, 4]}
        self.assertEqual(create_character(), new_character)

    @patch('character.class_selection', return_value='Trooper')
    @patch('character.create_name', return_value='Commander Cody')
    @patch('character.roll_die', side_effect=[18, 9, 16, 15, 5, 5])
    @patch('character.choose_inventory', return_value=['Assault Cannon'])
    def test_type_create_character(self, mock_class_selection, mock_create_name, mock_roll_die, choose_inventory):
        self.assertIsInstance(create_character(), dict)