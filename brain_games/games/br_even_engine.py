from random import randint
import prompt


def br_even():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0 and answer == 'yes' or \
       random_number % 2 != 0 and answer == 'no':
        print('Correct!')
        return True
    elif random_number % 2 == 0 and answer != 'yes':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
        return False
    elif random_number % 2 != 0 and answer != 'no':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
        return False
