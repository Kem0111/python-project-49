import math
from brain_games.games.even import get_random_number


FIRST_NUMBER = (1, 100)
SECOND_NUMBER = (1, 100)


def get_game_round_data():
    first_num = get_random_number(FIRST_NUMBER)
    second_num = get_random_number(SECOND_NUMBER)
    max_common_divider = math.gcd(first_num, second_num)
    return f'{first_num} {second_num}', max_common_divider


def RULSE():
    return 'Find the greatest common divisor of given numbers.'
