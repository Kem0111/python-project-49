#!/usr/bin/env python3
from brain_games.logic import questions
from brain_games.games.br_even_engine import\
    br_even, rules_br_even, get_true_answer_br_even


def main_br_even():
    questions(br_even, rules_br_even, get_true_answer_br_even)


if __name__ == '__main__':
    main_br_even()
