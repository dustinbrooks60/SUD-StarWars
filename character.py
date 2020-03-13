import random
import doctest


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """Simulates the rolling of a die.

    PARAM: number_of_rolls, a positive integer
    PARAM: number_of_sides, a positive integer
    PRECONDITION: number_of_rolls and number_of_sides must be positive integers
    POSTCONDITION: returns a random total from number_of_rolls to number_of_sides
    RETURN: Returns a random total
    >>> random.seed(1)
    >>> roll_die(1, 8)
    3
    >>> random.seed(3)
    >>> roll_die(2, 6)
    5
    >>> random.seed(12)
    >>> roll_die(3, 6)
    18
    >>> random.seed()
    """
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return 0

    max_total = number_of_sides * number_of_rolls

    return random.randint(number_of_rolls, max_total)


def choose_inventory() -> list:
    """Returns a starting item

    PARAM: character, a dictionary
    PRECONDITION: character must be a well-formed dictionary and user input must be 1,2,3,4,5,6, or 7
    POSTCONDITION: Appends an item to a character's inventory
    RETURN: An item chosen from user input
    """
    print("What weapon would you like to start with? Enter the corresponding number\n(1) Blaster Pistol\n"
          "(2) Blaster Rifle\n(3) Assault Cannon\n(4) Sniper Rifle\n")
    item_list = ["Blaster Pistol", "Blaster Rifle", "Assault Cannon", "Sniper Rifle"]
    user_input = str(input())
    if user_input == "1":
        return [item_list[0]]
    elif user_input == "2":
        return [item_list[1]]
    elif user_input == "3":
        return [item_list[2]]
    elif user_input == "4":
        return [item_list[3]]
    else:
        print("Please enter a valid item number")
        choose_inventory()


def class_selection() -> str:
    """Allows the user to pick a Star Wars class

    POSTCONDITION: user must enter a valid character otherwise the function will return None
    RETURN: Returns the chosen class as a string
    """
    dict_classes = {'1': 'Bounty Hunter', '2': 'Imperial Agent', '3': 'Jedi Consular', '4': 'Jedi Knight',
                    '5': 'Sith Warrior', '6': 'Sith Inquisitor', '7': 'Smuggler', '8': 'Trooper'}
    print("(1) Bounty Hunter\n(2) Imperial Agent\n(3) Jedi Consular\n(4) Jedi Knight\n"
          "(5) Sith Warrior\n(6) Sith Inquisitor\n(7) Smuggler\n(8) Trooper\n")
    chosen_class = str(input("Choose your class by entering a number from 1-8, ie. for Bounty Hunter type 1\n"))
    for key, value in dict_classes.items():
        if key == chosen_class:
            return value


def increase_character_health(character: dict):
    """Increases a characters health by 1 if it is below 10, otherwise it does nothing

    PARAM: character, a dictionary
    PRECONDITION: character is a well formed dictionary with a 'HP' key
    POSTCONDITION: A characters health stays the same, or it increases by 1
    """
    if character['HP'] == 10:
        return
    else:
        character['HP'] += 1
        return


def get_character_health(character: dict):
    """Retrieves a characters health

    PARAM: character, a dictionary
    PRECONDITION: character is a well formed dictionary with a 'HP' key
    POSTCONDITION: A character's health is printed
    >>> get_character_health({'HP': 10})
    Your health is: 10
    >>> get_character_health({'HP': 5})
    Your health is: 5
    """
    print("Your health is: %d" % character['HP'])


def get_character_position(character: dict) -> list:
    """Retrieves a characters position

    PARAM: character, a dictionary
    PRECONDITION: character is a well formed dictionary with a 'Position' key
    POSTCONDITION: A character dictionary's 'Position' key is returned
    RETURN: A character's position on an 8x8 board
    >>> get_character_position({'Position': [3, 4]})
    [3, 4]
    >>> get_character_position({'Position': [1, 7]})
    [1, 7]
    """
    return character['Position']


def create_name() -> str:
    """Allows the user to set a name

    POSTCONDITION: User input is returned as a string
    RETURN: A name, as a string, is returned
    """
    user_input = str(input("What is your name?\n"))
    return user_input


def create_character() -> dict:
    """Creates a character with a chosen name, HP set to 10, 6 random core attributes, XP, an inventory, and a position.

    POSTCONDITION: Creates a character with a name, a class determined from user input, HP set to 10,
    POSTCONDITION: attributes with randomly chosen values, XP set to 0, Inventory determined from class, and a position
    RETURN: A dictionary containing a name, a class, 6 attributes, XP, an inventory, and a position
    """

    character_class = class_selection()
    character_dictionary = {'Name': create_name(), 'Class': character_class, 'HP': 10,
                            'Strength': roll_die(3, 6), 'Dexterity': roll_die(3, 6),
                            'Constitution:': roll_die(3, 6), 'Intelligence': roll_die(3, 6), 'Wisdom': roll_die(3, 6),
                            'Charisma': roll_die(3, 6), 'XP': 0, 'Inventory': [], 'Position': [7, 4]}

    # If the character class is a Jedi Consular, Jedi Knight, or Sith, set their corresponding lightsaber colours
    if character_dictionary['Class'] == 'Jedi Consular':
        character_dictionary['Inventory'] = ['Lightsaber - Orange']
    elif character_dictionary['Class'] == 'Jedi Knight':
        character_dictionary['Inventory'] = ['Lightsaber - Blue']
    elif character_dictionary['Class'] == 'Sith Inquisitor' or character_dictionary['Class'] == 'Sith Warrior':
        character_dictionary['Inventory'] = ['Lightsaber - Red']
    # If the character class is not a Jedi or Sith, then call choose_inventory
    else:
        character_dictionary['Inventory'] = choose_inventory()

    return character_dictionary


def combat_to_death(opponent_one: dict, opponent_two: dict):
    """Performs opponent_one's attack against opponent_two

    opponent_one's attack depends on their class, if opponent_two's health goes below zero they die
    PARAM: opponent_one, a well-formed dictionary
    PARAM: opponent_two, a well-formed dictionary
    PRECONDITION: opponent_one and opponent_two must be well-formed dictionaries
    POSTCONDITION: opponent_two gets hit and their corresponding HP is reduced, opponent_two's dexterity is higher
                   than the attack roll so they don't get hit, or opponent_two dies
    """

    attack_damage = roll_die(1, 6)
    print('%s hits for %i' % (opponent_one['Name'], attack_damage))
    opponent_two['HP'] -= attack_damage
    print("The new health of the %s is %i" % (opponent_two['Name'], opponent_two['HP']))

    if opponent_two['HP'] <= 0:
        print('The %s has died' % opponent_two['Name'])
        opponent_one['XP'] += 5
        return

    attack_damage = roll_die(1, 6)
    print('The %s hits for %i' % (opponent_two['Name'], attack_damage))
    opponent_one['HP'] -= attack_damage
    print("The new health of %s is %i" % (opponent_one['Name'], opponent_one['HP']))

    if opponent_one['HP'] <= 0:
        print('%s has died' % opponent_one['Name'])
        return

    else:
        combat_to_death(opponent_one, opponent_two)


def main():
    pass


if __name__ == "__main__":
    doctest.testmod()

