from utils import generate_number, get_valid_num_input, clean_screen
from time import sleep


def generate_sequence(difficulty):
    return [generate_number(101, 1) for i in range(difficulty)]


def get_list_from_user(difficulty):
    user_number = []
    for i in range(difficulty):
        num = get_valid_num_input(input(f'\n insert number {i+1}: '))
        user_number.append(int(num))
    return user_number


def is_lists_equal(list_a, list_b):
    return list_a == list_b


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print('\n \n get ready! \n')
    sleep(2)
    print(", ".join([str(i) for i in sequence]))
    sleep(0.7)
    clean_screen()
    print(f'\n now insert the {difficulty} numbers as you remember: ')
    user_guess = get_list_from_user(difficulty)
    print(f'\n your numbers are: {user_guess}, the numbers you saw were: {sequence}')
    return is_lists_equal(sequence, user_guess)
