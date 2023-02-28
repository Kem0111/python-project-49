from random import randint, choice
from operator import add, sub, mul


def get_game_round_data():
    FIRST_NUM = randint(1, 100)
    SECOND_NUM = randint(1, 100)
    OPERATOR = choice(('+', '-', '*'))
    expression = f'{FIRST_NUM} {OPERATOR} {SECOND_NUM}'
    result = get_result(FIRST_NUM, SECOND_NUM, OPERATOR)
    return expression, result


def get_result(first_num, second_num, operator):
    OPERATION_MAP = {'+': add, '-': sub, '*': mul}.get
    operator = OPERATION_MAP(operator)
    result = operator(first_num, second_num)
    return result


def RULSE():
    return 'What is the result of the expression?'
