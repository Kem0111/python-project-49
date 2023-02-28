from random import randint


NUMBER = (1, 100)


def get_game_round_data():
    random_number = get_random_number(NUMBER)
    if is_even(random_number):
        return random_number, 'yes'
    return random_number, 'no'


def is_even(integer):
    return integer % 2 == 0


def get_random_number(range_):
    return randint(*range_)


def RULSE():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
