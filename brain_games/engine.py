import prompt

from brain_games import cli

NUMBER_OF_GAME_LAUNCERS = 3


def game_play(game_module):
    name = cli.welcome_user()
    print(game_module.QUESTION)
    for game_launch in range(NUMBER_OF_GAME_LAUNCERS):
        ques_num, right_ans = game_module.question_number_and_answer()
        print(f'Question: {ques_num}')
        user_ans = prompt.string('Your answer: ')
        if user_ans == right_ans:
            print('Correct!')
        else:
            print(
                f"'{user_ans}' is wrong answer ;(\n"
                f"Correct answer was '{right_ans}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')



