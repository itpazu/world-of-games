from utils import SCORES_FILE_NAME
from pathlib import Path
from enum import Enum
import re

Games= Enum('Games', ['GUESS', 'MEMORY', 'CURRENCY'])

POINTS_OF_WINNING = lambda difficulty: difficulty * 3 + 5
def read_from_score_file():
    file = Path(SCORES_FILE_NAME)
    file.touch(exist_ok=True)
    with open(SCORES_FILE_NAME, 'r') as f:
        return f.readlines()

def write_scores_to_file(scores):
    with open(SCORES_FILE_NAME, 'w+') as f:
        for score in scores:
            f.write(score)
def get_current_score_for_game(game_num, lines):
    for line in lines:
        if Games(game_num).name in line:
            return lines.pop(lines.index(line))
    # lines.append(f'{Games(game_num).name} = 0')
    return f'{Games(game_num).name} = 0\n'


def replace_score_in_line(current_score, difficulty):
    score = re.search(r'\d+', current_score).group()
    new_score = int(score) + POINTS_OF_WINNING(difficulty)
    return re.sub(r'\d+', str(new_score), current_score)


def calc_total_score(scores):
    scores = re.findall(r'\d+', ' '.join(scores))
    return sum([int(score) for score in scores])


def add_score(game, difficulty):
    scores = read_from_score_file()
    current_scores = get_current_score_for_game(game, scores)
    new_score = replace_score_in_line(current_scores, difficulty)
    scores.append(new_score)
    write_scores_to_file(scores)
    calc_total_score(scores)
    return calc_total_score(scores)


print(add_score(2, 5))