from utils import get_valid_num_input, get_valid_num_within_range, AVAILABLE_GAMES, DIFFICULTY_RANGE, \
    clean_screen
from guess_game import play as play_guess
from currency_roulette import play as play_roulette
from memory_game import play as play_memory
from time import sleep


def get_game_by_id(game_id):
    is_valid_id = False
    res = None
    while not is_valid_id:
        res = list(filter(lambda x: x.get("id") == int(game_id), AVAILABLE_GAMES))
        if len(res) > 0:
            is_valid_id = True
        else:
            game_id = get_valid_num_input(input("Requested game number doesn't exist! enter a valid game number: "))
    return res


def switch_game(game_number, difficulty):
    if game_number == 1:
        return play_memory(difficulty)
    elif game_number == 2:
        return play_guess(difficulty)
    elif game_number == 3:
        return play_roulette(difficulty)
    return None


def welcome():
    name = input('what is your name? ')
    message = f'Hi {name} and welcome to the World of Games: The Epic Journey'
    print(message, '\n')


def start_play():
    print('please choose a game to play: \n')
    for game in AVAILABLE_GAMES:
        print(f'''
        {game.get("id")}: {game.get("name")}
        game description: 
        {game.get("description")}''')
    # getting a valid number from user
    game_number = get_valid_num_input(input("\n enter a game number: "))
    # checking that game is in range of existing games
    game_choice = get_game_by_id(game_number)
    # getting a difficulty level in range 1-5
    print("great! now let's pick difficulty level \n")
    difficulty_level = get_valid_num_within_range(DIFFICULTY_RANGE)
    print(f'\n you chose to play {game_choice[0].get("name")} at a difficulty level {difficulty_level} \n')
    sleep(2)
    clean_screen()
    result = switch_game(int(game_number), difficulty_level)
    # printing the user choice
    if result:
        print('\n you got it right!!')
        # return result1
    else:
        print(''' you were wrong :( 
                \n would you like to keep playing? ... you know you do ;)
        ''')
    should_continue = int(get_valid_num_input(input('type 1 to continue, 0 to exit: '),
                                          'please type 1 to continue, 0 to exit '))
    if should_continue:
        clean_screen()
        sleep(2)
        start_play()
    return

