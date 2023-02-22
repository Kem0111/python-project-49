from random import randint, choice
from operator import add, sub, mul


def br_calc():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    operator = choice(('+', '-', '*'))
    expression = f'{first_num} {operator} {second_num}'
    result = get_result(first_num, second_num, operator)
    return expression, result


def get_result(first_num, second_num, operator):
    get_operator = {'+': add, '-': sub, '*': mul}.get
    operator = get_operator(operator)
    result = operator(first_num, second_num)
    return result


def rules_br_calc():
    return 'What is the result of the expression?'
