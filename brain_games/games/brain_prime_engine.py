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


def true_answer(integer, answer):
    num = is_br_prime(integer)
    if num == 0 and answer == 'yes' or \
       num != 0 and answer == 'no':
        return True
    elif num == 0 and answer != 'yes':
        return f"'{answer}' is wrong answer ;(. Correct answer was 'yes'."
    else:
        return f"'{answer}' is wrong answer ;(. Correct answer was 'no'."


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
