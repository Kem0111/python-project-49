import prompt


def general_engine(game_data_func, game_rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rules())
    points = 0
    for _ in range(3):
        question, correct_answer = game_data_func()
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
