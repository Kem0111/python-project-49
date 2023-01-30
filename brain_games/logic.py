import prompt
from random import randint, choice
from operator import add, sub, mul


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


def question_for_calc():
    a = randint(1, 100)
    b = randint(1,100)
    get_operator = {'+': add, '-': sub, '*': mul}.get
    operator = choice(('+', '-', '*'))
    result = get_operator(operator)
    expression = [a, operator, b]
    string = ''
    integer = result(a, b)
    for i in expression:
        string += str(i) + ' '   
    print(f'Question: {string}')
    answer = prompt.string('Your answer: ')
    if str(answer) == str(integer):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{integer}'")
        return False





