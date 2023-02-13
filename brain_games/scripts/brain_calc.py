#!/usr/bin/env python3
from brain_games.logic import questions
from brain_games.games.br_calc_engine import\
    br_calc, rules_br_calc, get_true_answer_br_calc


def main_br_calc():
    questions(br_calc, rules_br_calc, get_true_answer_br_calc)


if __name__ == '__main__':
    main_br_calc()
