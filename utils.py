import re
import random

AVAILABLE_GAMES = [
    {
        "id": 1,
        "name": "Memory Game",
        "description": "a sequence of numbers will appear for 1 second and you have to \n "
                       "guess it back."
     },
    {
        "id": 2,
        "name": "Guess Game",
        "description": "guess a number and see if you chose like the computer."
    },
    {
        "id": 3,
        "name": "Currency Roulette",
        "description": "try and guess the value of a random amount of USD in ILS"
    }
]

DIFFICULTY_RANGE = 5


def get_valid_num_input(user_input):
    regex = r"^[0-9]+$"
    is_valid_input = bool(re.match(regex, user_input))
    while not is_valid_input:
        user_input = input("\n please enter a valid number: ")
        is_valid_input = bool(re.match(regex, user_input))
    return user_input


def get_valid_num_within_range(mx_rng, min_rng=1):
    is_valid = False
    level = None
    while not is_valid:
        level = get_valid_num_input(input(f'please choose a number between {min_rng}-{mx_rng}: \n'))
        if min_rng <= int(level) <= mx_rng:
            is_valid = True
    return int(level)


def generate_number(rng, min_rng=0):
    return random.randint(min_rng, rng)

