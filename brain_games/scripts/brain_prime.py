#!/usr/bin/env python3
from brain_games.games.brain_prime_engine import is_br_prime
from brain_games.logic import questions


def main():
    questions(is_br_prime)


if __name__ == '__main__':
    main()
