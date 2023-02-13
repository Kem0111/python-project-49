#!/usr/bin/env python3
from brain_games.games.brain_prime_engine import br_prime, rules, true_answer
from brain_games.logic import questions


def main():
    questions(br_prime, rules, true_answer)


if __name__ == '__main__':
    main()
