import prompt


NUM_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULSE)
    points = 0
    for _ in range(NUM_ROUNDS):
        question, correct_answer = game.get_game_round_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct')
            points += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(.\
Correct answerwas '{str(correct_answer)}'."
            )
            print(f"Let's try again, {name}!")
            break
    if points == 3:
        print(f'Congratulations, {name}!')
