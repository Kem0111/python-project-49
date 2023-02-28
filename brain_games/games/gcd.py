from random import randint
import math


def get_game_round_data():
    FIRST_NUMBER = randint(1, 100)
    SECOND_NUMBER = randint(1, 100)
    max_common_divider = math.gcd(FIRST_NUMBER, SECOND_NUMBER)
    return f'{FIRST_NUMBER} {SECOND_NUMBER}', max_common_divider


def RULSE():
    return 'Find the greatest common divisor of given numbers.'
