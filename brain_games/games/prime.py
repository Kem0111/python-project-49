from brain_games.games.even import get_random_number


NUMBER = (1, 100)


def get_game_round_data():
    number = get_random_number(NUMBER)
    if is_prime(number):
        return number, 'yes'
    return number, 'no'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def RULSE():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
