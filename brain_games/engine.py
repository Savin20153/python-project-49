from brain_games import cli


def game_play(QUESTION, game):
    name = cli.welcome_user()
    print(QUESTION)
    score = 0
    for _ in range(3):
        ques_num, right_ans = game.ques_num_and_ans()
        print(f'Question: {ques_num}')
        user_ans = input('Your answer: ')
        if user_ans == right_ans:
            print('Correct!')
            score += 1
        else:
            print(
                f"'{user_ans}' is wrong answer ;(. "
                f"Correct answer was '{right_ans}'."
            )
            print(f"Let's try again, {name}!")
            break
    if score == 3:
        print(f'Congratulations, {name}!')