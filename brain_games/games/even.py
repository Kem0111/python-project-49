from random import randint
from brain_games.get_random_number import get_random_number

NUMBER_INTERVAL = (1, 100)


def get_game_round_data():
    random_number = get_random_number(NUMBER_INTERVAL)
    if is_even(random_number):
        return random_number, 'yes'
    return random_number, 'no'


def is_even(integer):
    return integer % 2 == 0



RULSE = 'Answer "yes" if the number is even, otherwise answer "no".'
