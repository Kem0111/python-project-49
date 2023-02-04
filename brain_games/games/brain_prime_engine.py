import prompt
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
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    num = is_br_prime(number)
    if num == 0 and answer == 'yes' or \
       num != 0 and answer == 'no':
        print('Correct!')
        return True
    elif num == 0 and answer != 'yes':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
        return False
