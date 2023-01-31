import prompt
from random import randint, choice
from operator import add, sub, mul


def br_calc():
    print('What is the result of the expression?')
    a = randint(1, 100)
    b = randint(1, 100)
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
    if answer == str(integer):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{integer}'")
        return False
