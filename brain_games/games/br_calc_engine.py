from random import randint, choice
from operator import add, sub, mul


def br_calc():
    a = randint(1, 100)
    b = randint(1, 100)
    operator = choice(('+', '-', '*'))
    expression = f'{a} {operator} {b}'
    return expression


def get_true_answer_br_calc(integer):
    get_operator = {'+': add, '-': sub, '*': mul}.get
    integer = integer.split(' ')
    operator = get_operator(integer[1])
    result = operator(int(integer[0]), int(integer[2]))
    return result


def rules_br_calc():
    return 'What is the result of the expression?'
