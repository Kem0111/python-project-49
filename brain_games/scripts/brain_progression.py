#!/usr/bin/env python3
from brain_games.logic import questions
from brain_games.games.brain_progression_engine import br_progression, rules, true_answer


def main():
    questions(br_progression, rules, true_answer)


if __name__ == '__main__':
    main()
