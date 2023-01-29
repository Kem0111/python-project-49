import prompt
from random import randint


def question():
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


def questions():
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no"''')
    a = 0
    for i in range(3):
        if question() is False:
            a += 1
            print(f"Let's try again, {name}")
            break
    if a == 0:
        print(f'Congratulations, {name}')
