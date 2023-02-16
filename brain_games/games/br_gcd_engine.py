from random import randint
import math


def br_gcd():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    return f'{first_number} {second_number}'


def rules_br_gcd():
    return 'Find the greatest common divisor of given numbers.'


def get_true_answer_br_gcd(integer):
    integer = integer.split(' ')
    max_common_divider = math.gcd(int(integer[0]), int(integer[1]))
    return max_common_divider
