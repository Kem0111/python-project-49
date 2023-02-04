from random import randint
import prompt
import math


def br_gcd():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    max_common_divider = math.gcd(first_number, second_number)
    print(f'Question: {first_number} {second_number}')
    answer = prompt.string('Your answer: ')
    if answer == str(max_common_divider):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(.\
Correct answer was '{str(max_common_divider)}'.")
        return False
