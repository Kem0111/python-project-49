from brain_games.random_number import get_random_number


INITIAL_TERM_INTERVAL = (1, 30)
FINIT_ARITHMETIC_PROGRESSION_INTERVAL = (70, 100)
COMMON_DIFF_INTERVAL = (2, 10)
progression_length = 10


def get_game_round_data():
    initial_term = get_random_number(INITIAL_TERM_INTERVAL)
    final_term = get_random_number(
        FINIT_ARITHMETIC_PROGRESSION_INTERVAL
    )
    common_diff = get_random_number(COMMON_DIFF_INTERVAL)
    progression = generate_arithmetic_progression(
        initial_term,
        final_term,
        common_diff,
        progression_length
    )
    index = get_random_number((0, len(progression) - 1))
    number = progression[index]
    string_progression = stringify(progression, index)
    return string_progression, number


def stringify(progression, hidden_term_index):
    progression[hidden_term_index] = '..'
    return ' '.join(str(i) for i in progression)


def generate_arithmetic_progression(initial_term, final_term, common_diff, progression_length):
    return list(range(
        initial_term, final_term, common_diff)[:progression_length]
    )


RULES = 'What number is missing in the progression?'
