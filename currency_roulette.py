from currency_converter import CurrencyConverter
from utils import generate_number, get_valid_num_input


def get_money_interval(difficulty, rnd_num):
    converter = CurrencyConverter()
    ils_num = converter.convert(rnd_num, 'USD', 'ILS')
    guess_range = 10 - int(difficulty)
    min_good_guess = ils_num - guess_range
    max_good_guess = ils_num + guess_range
    return ils_num, min_good_guess, max_good_guess


def get_guess_from_user(generated_num):
    return get_valid_num_input(input(f'''Now you need to guess the ILS value of ${generated_num}.
     insert your guess: '''))


def compare_results(user_guess, min_interval, max_interval):
    return min_interval <= user_guess <= max_interval


def play(difficulty):
    rnd_num = generate_number(100, 1)
    ils_num, min_good_guess, max_good_guess = get_money_interval(difficulty, rnd_num)
    user_guess = get_guess_from_user(rnd_num)
    print(f'\n as of today, the ILS value of ${rnd_num} is {round(ils_num, 2)} '
          f'your wining range was {round(min_good_guess, 2)}-{round(max_good_guess,2)} '
          f'you guessed {user_guess} .....  \n')
    return compare_results(user_guess, min_good_guess, max_good_guess)