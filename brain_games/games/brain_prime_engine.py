import prompt
from random import randint


def is_br_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number = 3
    num = 0
    if number == 1:
        num += 1
    for i in range(2, number):
        if number % i == 0 and i < number:
            num += 1
            break
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
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
