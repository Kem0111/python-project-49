from random import randint


def is_br_prime(number):
    num = 0
    if number == 1:
        num += 1
    for i in range(2, number):
        if number % i == 0 and i < number:
            num += 1
            break
    return num


def br_prime():
    number = randint(1, 100)
    return number


def get_true_answer_br_prime(integer):
    num = is_br_prime(integer)
    if num == 0:
        return 'yes'
    else:
        return 'no'


def rules_br_prime():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
