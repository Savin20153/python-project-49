import prompt

from brain_games import cli

GAMES_COUNT = 3


def game_play(run_game):
    name = cli.welcome_user()
    print(run_game.QUESTION)
    for _ in range(GAMES_COUNT):
        question, right_answer = run_game.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(")
            print(f"Connect answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

