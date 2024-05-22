from utils import generate_number,  get_valid_num_within_range


def compare_results(num1, num2):
    return num1 == num2


def get_guess_from_user(difficulty):
    return get_valid_num_within_range(difficulty, 0)


def play(difficulty):
    print('\n welcome to the guess game!! \n')
    rand_num = generate_number(difficulty)
    user_num = get_guess_from_user(difficulty)
    print(f'\n you chose number {user_num}, the secret number was {rand_num} \n')
    return compare_results(rand_num, int(user_num))
