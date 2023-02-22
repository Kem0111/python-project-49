from random import randint


def br_prime():
    number = randint(1, 100)
    cursor = to_figure_out_is_prime_num(number)
    if cursor == 0:
        return number, 'yes'
    return number, 'no'


def to_figure_out_is_prime_num(number):
    cursor = 0
    if number == 1:
        cursor += 1
    for i in range(2, number):
        if number % i == 0 and i < number:
            cursor += 1
            break
    return cursor


def rules_br_prime():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
