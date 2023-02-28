from random import choice
from operator import add, sub, mul
from brain_games.games.even import get_random_number


FIRST_NUMBER = (1, 100)
SECOND_NUMBER = (1, 100)
operation_map = {'+': add, '-': sub, '*': mul}.get


def get_game_round_data():
    x = get_random_number(FIRST_NUMBER)
    y = get_random_number(SECOND_NUMBER)
    operator = choice(('+', '-', '*'))
    expression = f'{x} {operator} {y}'
    result = get_result(x, y, operator, operation_map)
    return expression, result


def get_result(first_num, second_num, operator, map):
    sign = map(operator)
    result = sign(first_num, second_num)
    return result


def RULSE():
    return 'What is the result of the expression?'
