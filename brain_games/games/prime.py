from random import randint


def get_game_round_data():
    NUMBER = randint(1, 100)
    if is_prime(NUMBER):
        return NUMBER, 'yes'
    return NUMBER, 'no'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def RULSE():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
