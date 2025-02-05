from brain_games import cli, engine
from brain_games.games import calc

question_prev = 'What is the result of the expression?'


def main():
    name = cli.welcome_user()
    engine.game_play(name, question_prev, calc)


if __name__ == '__main__':
    main()