import json
import character
import doctest


def get_stored_username():
    """Returns a username from the username.json file, if file is not found then return error

    PRECONDITION: username.json already exists and is used to hold a character
    POSTCONDITION: a username is returned or None is returned if file does not exist
    RETURN: A username saved in a JSON file
    """
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def store_new_character(player_character: dict):
    """Stores a new character

    PRECONDITION: player_character is a properly formed dictionary for the game
    POSTCONDITION: The player_character is stored in username.json file
    RETURN: A character is stored in username.json
    >>> store_new_character({'Name': 'Dustin'})
    Thanks for playing! We'll remember you when you come back, Dustin
    >>> store_new_character({'Name': 'Jango Fett'})
    Thanks for playing! We'll remember you when you come back, Jango Fett
    """
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(player_character, f_obj)
    print("Thanks for playing! We'll remember you when you come back, " + player_character['Name'])


def new_or_old_character():
    """Asks the user if they are a new player (creates new character) or if they have played before (loads a character)

    POSTCONDITION: a username is returned or None is returned if file does not exist
    RETURN: A new character or a username saved from a JSON file
    """
    sentinel_value = True
    while sentinel_value is True:
        user_input = input("Are you a new player? Type 'y' for yes and to create a new character,"
                           " or 'n' for no to load an old character from file\n")
        if user_input == 'y':
            # If user is a new player, create a new character
            new_character = character.create_character()
            return new_character
        elif user_input == 'n':
            # If user is not a new player, load a previously saved character
            new_character = get_stored_username()
            print("Welcome back,", new_character['Name'])
            return new_character
        else:
            print("Please enter y or n")


def main():
    pass


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    main()