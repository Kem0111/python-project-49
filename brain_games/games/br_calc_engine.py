from random import randint, choice
from operator import add, sub, mul


def br_calc():
    a = randint(1, 100)
    b = randint(1, 100)
    operator = choice(('+', '-', '*'))
    expression = f'{a} {operator} {b}'
    return expression


def true_answer(integer, answer):
    get_operator = {'+': add, '-': sub, '*': mul}.get
    integer = integer.split(' ')
    operator = get_operator(integer[1])
    result = operator(int(integer[0]), int(integer[2]))
    if answer == str(result):
        return True
    else:
        return f"'{answer}' is wrong answer ;(. Correct answer was '{result}'."


def rules():
    return 'What is the result of the expression?'
