from random import randint


def get_game_round_data():
    NUMBER = randint(1, 100)
    if is_even(NUMBER):
        return NUMBER, 'yes'
    return NUMBER, 'no'


def is_even(integer):
    return integer % 2 == 0


def RULSE():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
