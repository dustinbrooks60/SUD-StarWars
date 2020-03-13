import random
import character
import doctest


def roll_die(number_of_rolls: int, number_of_sides: int):
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


def create_rancor() -> dict:
    """Creates a Rancor monster

    POSTCONDITION: A Rancor dictionary is created
    RETURN: A dictionary representing a Rancor
    """
    monster_dictionary = {'Name': 'Rancor', 'Class': 'Monster', 'HP': 5,
                          'Strength': 15, 'Dexterity': 6,
                          'Constitution:': 14, 'Intelligence': 2, 'Wisdom': 1,
                          'Charisma': 1, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def create_rathtar() -> dict:
    """Creates a Rathtar monster

    POSTCONDITION: A Rathtar dictionary is created
    RETURN: A dictionary representing a Rathtar
    """
    monster_dictionary = {'Name': 'Rathtar', 'Class': 'Monster', 'HP': 5,
                          'Strength': 14, 'Dexterity': 17,
                          'Constitution:': 10, 'Intelligence': 10, 'Wisdom': 1,
                          'Charisma': 1, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def create_dianoga() -> dict:
    """Creates a Dianoga monster

    POSTCONDITION: A Dianoga dictionary is created
    RETURN: A dictionary representing a Dianoga
    """
    monster_dictionary = {'Name': 'Dianoga', 'Class': 'Monster', 'HP': 5,
                          'Strength': 12, 'Dexterity': 13,
                          'Constitution:': 12, 'Intelligence': 14, 'Wisdom': 5,
                          'Charisma': 1, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def create_krayt_dragon() -> dict:
    """Creates a Krayt Dragon monster

    POSTCONDITION: A Krayt Dragon dictionary is created
    RETURN: A dictionary representing a Krayt Dragon
    """
    monster_dictionary = {'Name': 'Krayt Dragon', 'Class': 'Monster', 'HP': 5,
                          'Strength': 18, 'Dexterity': 8,
                          'Constitution:': 16, 'Intelligence': 6, 'Wisdom': 8,
                          'Charisma': 3, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def create_night_beast() -> dict:
    """Creates a Night Beast monster

    POSTCONDITION: A Night Beast dictionary is created
    RETURN: A dictionary representing a Night Beast
    """
    monster_dictionary = {'Name': 'Night Beast', 'Class': 'Monster', 'HP': 5,
                          'Strength': 8, 'Dexterity': 16,
                          'Constitution:': 8, 'Intelligence': 16, 'Wisdom': 5,
                          'Charisma': 5, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def create_corrupted_jedi() -> dict:
    """Creates a Corrupted Jedi monster

    POSTCONDITION: A Corrupted Jedi dictionary is created
    RETURN: A dictionary representing a Corrupted Jedi
    """
    monster_dictionary = {'Name': 'Corrupted Jedi', 'Class': 'Monster', 'HP': 5,
                          'Strength': 8, 'Dexterity': 14,
                          'Constitution:': 15, 'Intelligence': 16, 'Wisdom': 16,
                          'Charisma': 15, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def create_bounty_hunter() -> dict:
    """Creates a Bounty Hunter monster

    POSTCONDITION: A Bounty Hunter dictionary is created
    RETURN: A dictionary representing a Bounty Hunter
    """
    monster_dictionary = {'Name': 'Bounty Hunter', 'Class': 'Monster', 'HP': 5,
                          'Strength': 6, 'Dexterity': 16,
                          'Constitution:': 10, 'Intelligence': 17, 'Wisdom': 13,
                          'Charisma': 18, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def create_tusken_raider() -> dict:
    """Creates a Tusken Raider monster

    POSTCONDITION: A Tusken Raider dictionary is created
    RETURN: A dictionary representing a Tusken Raider
    """
    monster_dictionary = {'Name': 'Tusken Raider', 'Class': 'Monster', 'HP': 5,
                          'Strength': 5, 'Dexterity': 10,
                          'Constitution:': 12, 'Intelligence': 12, 'Wisdom': 5,
                          'Charisma': 2, 'XP': 0, 'Inventory': []}

    return monster_dictionary


def select_a_monster() -> dict:
    """Randomly selects a monster to be created

    POSTCONDITION: A random monster is selected to be created based on the number generated from randint(1, 8)
    RETURN: A dictionary representing a monster
    """
    random_monster_number = random.randint(1, 8)
    if random_monster_number == 1:
        return create_rancor()
    elif random_monster_number == 2:
        return create_rathtar()
    elif random_monster_number == 3:
        return create_dianoga()
    elif random_monster_number == 4:
        return create_krayt_dragon()
    elif random_monster_number == 5:
        return create_night_beast()
    elif random_monster_number == 6:
        return create_corrupted_jedi()
    elif random_monster_number == 7:
        return create_bounty_hunter()
    elif random_monster_number == 8:
        return create_tusken_raider()


def monster_combat(user_character: dict):
    """Simulates combat with a monster

    PARAM: user_character, a dictionary representing a character
    PRECONDITION: user_character is a properly formed character dictionary
    POSTCONDITION: A character either fights a monster to death or runs away and takes no damage or takes 1-4 damage
    """
    new_monster = select_a_monster()
    print("You've encountered a %s!\n" % new_monster['Name'])
    combat_loop = True
    while combat_loop is True:
        user_input = input("Would you like to fight or run? Type 'y' for yes or 'n' for no\n")
        if user_input == 'y':
            character.combat_to_death(user_character, new_monster)
            combat_loop = False
        elif user_input == 'n':
            run_away_chance = random.randint(1, 10)
            if run_away_chance == 1:
                damage = roll_die(1, 4)
                user_character['HP'] -= damage
                print("You ran away, but took %d damage" % damage)
                combat_loop = False
            else:
                print("You successfully ran away without taking damage!")
                combat_loop = False


def main():
    pass


if __name__ == "__main__":
    doctest.testmod()