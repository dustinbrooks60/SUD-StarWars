import character
import monster
import load_character
import random
import doctest


def print_intro():
    print(""" 
                   ________________.  ___     .______
                  /                | /   \    |   _  |
                 |   (-----|  |----`/  ^  \   |  |_)  |
                  \   \    |  |    /  /_\  \  |      /
             .-----)   |   |  |   /  _____  \ |  |\  \ ------.
             |________/    |__|  /__/     \__\| _| `.________|
            ____    __    ____  ___     .______    ________.
            \   \  /  \  /   / /   \    |   _  \  /        |
             \   \/    \/   / /  ^  \   |  |_)  ||   (-----`
              \            / /  /_\  \  |      /  \   |
               \    /\    / /  _____  \ |  |\  \---)   |
                \__/  \__/ /__/     \__\|__| `._______/
""")
    print("The year is 10 BBY (Before the Battle of Yavin). The Empire rules over almost every known planet in the"
          " galaxy.\nYou awaken in a stupor. "
          "You can't remember what your name is or how you got here.\n")
    print("Last you remember, your ship had docked in Tatooine for supplies. You and your crew decided\n"
          "to go to the Cantina for a glass of Corellian spiced rum. The night was filled with laughter as you all"
          " drank your fill.\nAs the night went on, you became severely inebriated and decided to head back to the ship"
          " for some sleep.\nThe next thing you knew, you awoke in a black pit with over a hundred spectators "
          "chanting obscenities at you.\nYou think to yourself: A Hutt's dungeon no doubt. Your crew must have drugged "
          "and sold you to a Hutt for his entertainment.\n"
          "The large worm yells at his translator, the translator tells you: 'survive until the top floor and you'll be"
          " set free'\n")


def create_game_board() -> dict:
    """Creates a 9x9 game board

    POSTCONDITION: produces a 9x9 dictionary with keys as coordinate pair and value as '*' character
    RETURN: returns a dictionary with keys (0-8) as coordinates and all values as '*'
    """
    game_board = {}
    for row in range(9):
        for col in range(9):
            game_board[(row, col)] = '*'
    return game_board


def set_border(game_board: dict) -> dict:
    """Sets a border for a game board

    PARAM: game_board, a dictionary
    PRECONDITION: game_board is a proper dictionary of keys (coordinates) and values ('*' character)
    POSTCONDITION: Sets the border of the game board as X's
    RETURN: returns a game board with a set border
    """
    for keys, values in game_board.items():
        if keys[0] == 0:
            game_board[keys] = 'X'
            game_board[(0, 4)] = ' '
        if keys[0] == 8:
            game_board[keys] = 'X'
        if keys[1] == 0:
            game_board[keys] = 'X'
        if keys[1] == 8:
            game_board[keys] = 'X'
    return game_board


def print_game_board(game_dictionary: dict):
    """Prints a game board

    PARAM: board, a dictionary
    PRECONDITION: board is a proper dictionary of keys (coordinates) and values ('*' character)
    POSTCONDITION: The dictionary game board is printed
    RETURN: prints a game board
    """
    for x in range(9):
        for y in range(9):
            print(game_dictionary[x, y], end=' ')
        print()


def find_character(board: dict) -> tuple:
    """Finds a character from a given board

    PARAM: board, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' character)
    POSTCONDITION: returns a coordinate (key) of the characters current location
    RETURN: returns a coordinate pair of the characters location
    >>> find_character({(1, 4): '@'})
    (1, 4)
    >>> find_character({(7, 4): '@'})
    (7, 4)
    """
    character_position = ()
    for key, value in board.items():
        if value[0] == "@":
            character_position = key
    return character_position


def starting_position(board: dict):
    """Sets the starting position of a character

    PARAM: player_character, a dictionary
    PARAM: board, a dictionary
    PRECONDITION: game_board is a proper dictionary of coordinates (keys) and values ('*' character)
    POSTCONDITION: sets a characters position as (7, 4) and then prints the board
    """
    board[(7, 4)] = "@"
    print("Your starting position is: ")
    print_game_board(board)


def set_position(board: dict, player_character: dict) -> dict:
    """Sets the position of a character

    PARAM: board, a dictionary
    PARAM: player_character, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' character)
    PRECONDITION: player_character is a proper dictionary containing a 'Position' key and a list value
    POSTCONDITION: sets a characters 'Position' key depending on where the @ symbol is on the board
    RETURN: a player_character dictionary with it's 'Position' key set to where the '@' symbol is currently located
    """
    character_position = find_character(board)
    player_character['Position'] = list(character_position)
    return player_character


def place_character(board: dict, player_character: dict) -> dict:
    """Places a character on the board depending on where their 'Position' key points to

    PARAM: board, a dictionary
    PARAM: player_character, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' character)
    PRECONDITION: player_character is a proper dictionary containing a 'Position' key and a list value
    POSTCONDITION: sets a characters position on a board as the '@' character
    RETURN: a board with the characters position set as @ on the board
    """
    previous_position = player_character['Position']
    new_position = tuple(previous_position)
    board[new_position] = '@'
    return board


def move_north(board: dict):
    """Moves a character north by 1 place

    PARAM: board, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' or 'X')
    POSTCONDITION: moves the '@' character position north by 1 by subtracting 1 from the rows
    POSTCONDITION: if they reach [0, 4] then they enter the next level
    RETURN: None, if they hit the north border
    """
    new_location = list(find_character(board))
    new_location_temp = find_character(board)
    new_location[0] = new_location[0] - 1
    if new_location == [0, 4]:
        # If the next location is [0, 4] then we move to the next level
        board[(7, 4)] = "@"
        board[(1, 4)] = "*"
        next_level(board)
    elif new_location[0] == 0:
        print("You've hit the border! Please select another direction")
        return
    else:
        new_location = tuple(new_location)
        board[new_location] = "@"
        board[new_location_temp] = "*"
        print("You moved north by 1: ")
        print_game_board(board)


def move_west(board: dict):
    """Moves a character west by 1 place

    PARAM: board, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' or 'X')
    POSTCONDITION: moves the '@' character position west by 1 by subtracting 1 from the columns
    RETURN: None, if they hit the west border
    """
    new_location = list(find_character(board))
    new_location_temp = find_character(board)
    new_location[1] = new_location[1] - 1
    if new_location[1] == 0:
        print("You've hit the border! Please select another direction")
        return None
    new_location = tuple(new_location)
    board[new_location] = "@"
    board[new_location_temp] = "*"
    print("You moved west by 1: ")
    print_game_board(board)


def move_south(board: dict):
    """Moves a character south by 1 place

    PARAM: board, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' or 'X')
    POSTCONDITION: moves the '@' character position south by 1 by adding 1 to the rows
    RETURN: None, if they hit the south border
    """
    new_location = list(find_character(board))
    new_location_temp = find_character(board)
    new_location[0] = new_location[0] + 1
    if new_location[0] == 8:
        print("You've hit the border! Please select another direction")
        return None
    new_location = tuple(new_location)
    board[new_location] = "@"
    board[new_location_temp] = "*"
    print("You moved south by 1: ")
    print_game_board(board)


def move_east(board: dict):
    """Moves a character east by 1 place

    PARAM: board, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' or 'X')
    POSTCONDITION: moves the '@' character position east by 1 by adding 1 to the columns
    RETURN: None, if they hit the east border
    """
    new_location = list(find_character(board))
    new_location_temp = find_character(board)
    new_location[1] = new_location[1] + 1
    if new_location[1] == 8:
        print("You've hit the border! Please select another direction")
        return None
    new_location = tuple(new_location)
    board[new_location] = "@"
    board[new_location_temp] = "*"
    print("You moved east by 1: ")
    print_game_board(board)


def next_level(board):
    """Pretends to move the character to a new board by printing a message and resetting the top space

    PARAM: board, a dictionary
    PRECONDITION: board is a proper dictionary of coordinates (keys) and values ('*' or 'X')
    POSTCONDITION: The spot (0, 4) on the board is set to an open space
    RETURN: A dictionary representing a game board
    """
    print("---------------                 You've made it to the next floor                           ---------------\n"
          "---------------    The door behind you slams shut. You hear laughter behind it             ---------------")
    board[(0, 4)] = " "
    print_game_board(board)
    return board


def main():
    # Prints intro then sets up the game board
    print_intro()
    new_board = create_game_board()
    new_board = set_border(new_board)
    # Determines if user needs to create a new character or not
    new_character = load_character.new_or_old_character()
    # Places the character on the board depending on their 'Position' key
    if new_character['Position'] == (7, 4):
        starting_position(new_board)
    else:
        place_character(new_board, new_character)
        print_game_board(new_board)

    # Begins the game loop
    continue_game = True
    while continue_game is True:
        user_input = input("Type n, s, w, e to move north, south, west, or east. Type 'h' to see your health"
                           " or type 'quit' to exit\n")
        # If the user enters 'n' - call move_north function and set their position
        if user_input == "n":
            move_north(new_board)
            set_position(new_board, new_character)
            # Call randint(1, 10) to determine if they have encountered a monster
            monster_chance = random.randint(1, 10)
            if monster_chance == 1:
                monster.monster_combat(new_character)
            # If characters 'HP' equals 0 or goes below 0 then end the game
            if new_character['HP'] <= 0:
                print("Your character has died, game over")
                continue_game = False
            # Increase character's health by 1
            if monster_chance != 1:
                character.increase_character_health(new_character)

        # If the user enters 's' - call move_south function and set their position
        elif user_input == "s":
            move_south(new_board)
            set_position(new_board, new_character)
            monster_chance = random.randint(1, 10)
            if monster_chance == 1:
                monster.monster_combat(new_character)
            if new_character['HP'] <= 0:
                print("Your character has died, game over")
                continue_game = False
            if monster_chance != 1:
                character.increase_character_health(new_character)

        # If the user enters 'w' - call move_west function and set their position
        elif user_input == "w":
            move_west(new_board)
            set_position(new_board, new_character)
            monster_chance = random.randint(1, 10)
            if monster_chance == 1:
                monster.monster_combat(new_character)
            if new_character['HP'] <= 0:
                print("Your character has died, game over")
                continue_game = False
            if monster_chance != 1:
                character.increase_character_health(new_character)

        # If the user enters 'e' - call move_east function and set their position
        elif user_input == "e":
            move_east(new_board)
            set_position(new_board, new_character)
            monster_chance = random.randint(1, 10)
            if monster_chance == 1:
                monster.monster_combat(new_character)
            if new_character['HP'] <= 0:
                print("Your character has died, game over")
                continue_game = False
            if monster_chance != 1:
                character.increase_character_health(new_character)

        # If the user enters 'h' - call get_character_health function
        elif user_input == "h":
            character.get_character_health(new_character)

        # If the user enters 'quit' - store the character and end the game
        elif user_input == "quit":
            load_character.store_new_character(new_character)
            continue_game = False
        else:
            print("That was not correct input, try again")


if __name__ == "__main__":
    doctest.testmod()
    main()