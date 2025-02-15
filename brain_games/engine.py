import prompt

from brain_games import cli

NUMBER_OF_GAME_LAUNCERS = 3


def game_play(run_game):
    name = cli.welcome_user()
    print(run_game.QUESTION)
    for game_launch in range(NUMBER_OF_GAME_LAUNCERS):
        question_number, right_answer = run_game.question_and_answer()
        print(f'Question: {question_number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(")
            print(f"Connect answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

