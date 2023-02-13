#!/usr/bin/env python3
from brain_games.logic import questions
from brain_games.games.br_even_engine import br_even, rules, true_answer


def main():
    questions(br_even, rules, true_answer)


if __name__ == '__main__':
    main()
