#!/usr/bin/env python3
from brain_games.logic import questions
from brain_games.games.br_calc_engine import br_calc, rules, true_answer


def main():
    questions(br_calc, rules, true_answer)


if __name__ == '__main__':
    main()
