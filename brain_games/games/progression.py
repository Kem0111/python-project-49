from brain_games.games.even import get_random_number


INITIAL_TERM = (1, 30)
FINIT_ARTITHMETIC_PROGRESSION = (70, 100)
COMMON_DIFF = (2, 10)


def get_game_round_data():
    progression = arithmetic_progression(
        INITIAL_TERM,
        FINIT_ARTITHMETIC_PROGRESSION,
        COMMON_DIFF
    )
    index = get_random_number((0, len(progression)-1))
    number = progression[index]
    progression[index] = '..'
    string_progression = string_representation(progression)
    return string_progression, number


def string_representation(progression):
    return ' '.join([str(i) for i in progression])


def arithmetic_progression(start, end, delimiter):
    a = get_random_number(start)
    m = get_random_number(end)
    d = get_random_number(delimiter)
    return list(range(a, m, d)[:10])


def RULSE():
    return 'What number is missing in the progression?'
