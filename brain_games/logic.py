import prompt
from brain_games.games.br_even_engine import br_even
from brain_games.games.br_calc_engine import br_calc
from brain_games.games.br_gcd_engine import br_gcd
from brain_games.games.brain_prime_engine import br_prime


def questions(funk):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(greeting(funk))
    a = 0
    for i in range(3):
        if funk() is False:
            a += 1
            print(f"Let's try again, {name}!")
            break
    if a == 0:
        print(f'Congratulations, {name}!')


def greeting(argument):
    if argument == br_even:
        return 'Answer "yes" if the number is even, otherwise answer "no".'
    elif argument == br_calc:
        return 'What is the result of the expression?'
    elif argument == br_gcd:
        return 'Find the greatest common divisor of given numbers.'
    elif argument == br_prime:
        return 'Answer "yes" if given number is prime. Otherwise answer "no".'
    else:
        return 'What number is missing in the progression?'
