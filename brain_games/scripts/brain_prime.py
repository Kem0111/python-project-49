#!/usr/bin/env python3
from brain_games.games.brain_prime_engine import br_prime,\
    rules_br_prime, get_true_answer_br_prime
from brain_games.logic import questions


def main():
    questions(br_prime, rules_br_prime, get_true_answer_br_prime)


if __name__ == '__main__':
    main()
