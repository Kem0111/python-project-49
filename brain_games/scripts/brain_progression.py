#!/usr/bin/env python3
from brain_games.logic import questions
from brain_games.games.brain_progression_engine import br_progression,\
    rules_br_progression,\
    get_true_answer_br_progression


def main_br_progression():
    questions(
        br_progression, rules_br_progression,
        get_true_answer_br_progression
    )


if __name__ == '__main__':
    main_br_progression()
