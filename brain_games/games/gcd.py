import math
from brain_games.get_random_number import get_random_number


FIRST_NUMBER_INTERVAL = (1, 100)
SECOND_NUMBER_INTERVAL = (1, 100)


def get_game_round_data():
    first_num = get_random_number(FIRST_NUMBER_INTERVAL)
    second_num = get_random_number(SECOND_NUMBER_INTERVAL)
    max_common_divider = math.gcd(first_num, second_num)
    return f'{first_num} {second_num}', max_common_divider


RULSE = 'Find the greatest common divisor of given numbers.'
