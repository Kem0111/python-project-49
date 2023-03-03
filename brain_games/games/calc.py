from random import choice
from operator import add, sub, mul
from brain_games.random_number import get_random_number


FIRST_NUMBER_INTERVAL = (1, 100)
SECOND_NUMBER_INTERVAL = (1, 100)
operation_map = {'+': add, '-': sub, '*': mul}.get


def get_game_round_data():
    x = get_random_number(FIRST_NUMBER_INTERVAL)
    y = get_random_number(SECOND_NUMBER_INTERVAL)
    operator = choice(('+', '-', '*'))
    expression = f'{x} {operator} {y}'
    result = get_result(x, y, operator, operation_map)
    return expression, result


def get_result(first_num, second_num, operator, map):
    sign = map(operator)
    result = sign(first_num, second_num)
    return result


RULES = 'What is the result of the expression?'
