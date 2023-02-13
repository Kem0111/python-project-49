from random import randint


def br_even():
    random_number = randint(1, 100)
    return random_number


def rules_br_even():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_true_answer_br_even(random_numbers, answer):
    random_number = random_numbers
    if random_number % 2 == 0 and answer == 'yes':
        return True
    elif random_number % 2 != 0 and answer == 'no':
        return True
    elif random_number % 2 == 0 and answer != 'yes':
        return f"'{answer}' is wrong answer ;(. Correct answer was 'yes'."
    elif random_number % 2 != 0 and answer != 'no':
        return f"'{answer}' is wrong answer ;(. Correct answer was 'no'."
