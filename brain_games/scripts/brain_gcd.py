#!/usr/bin/env python3
from brain_games.logic import questions
from brain_games.games.br_gcd_engine import br_gcd,\
    rules_br_gcd, get_true_answer_br_gcd


def main_br_gcd():
    questions(br_gcd, rules_br_gcd, get_true_answer_br_gcd)


if __name__ == '__main__':
    main_br_gcd()
