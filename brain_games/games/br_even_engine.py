from random import randint


def br_even():
    random_number = randint(1, 100)
    return random_number


def rules_br_even():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_true_answer_br_even(random_numbers):
    random_number = random_numbers
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'
