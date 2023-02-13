from random import randint
import math


def br_gcd():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    return f'{first_number} {second_number}'


def rules():
    return 'Find the greatest common divisor of given numbers.'


def true_answer(integer, answer):
    integer = integer.split(' ')
    max_common_divider = math.gcd(int(integer[0]), int(integer[1]))
    if answer == str(max_common_divider):
        return True
    else:
        return f"'{answer}' is wrong answer ;(.\
Correct answer was '{str(max_common_divider)}'."
