from random import randint


def br_even():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        return random_number, 'yes'
    return random_number, 'no'


def rules_br_even():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
