from random import randint
import prompt


def br_gcd():
    print('Find the greatest common divisor of given numbers.')
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    min_values = min(first_number, second_number)
    counter = 1
    common_divider = []
    for i in range(1, min_values + 1):
        if (first_number % counter) == 0 == (second_number % counter):
            common_divider.append(counter)
        counter += 1
    print(f'Question: {first_number} {second_number}')
    answer = prompt.string('Your answer: ')
    if str(answer) == str(common_divider[-1]):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(.\
Correct answer was '{str(common_divider[-1])}'.")
        return False
