from random import randint
import math


def br_gcd():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    max_common_divider = math.gcd(first_number, second_number)
    return f'{first_number} {second_number}', max_common_divider


def rules_br_gcd():
    return 'Find the greatest common divisor of given numbers.'
