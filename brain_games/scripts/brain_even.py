from brain_games import cli, engine
from brain_games.games import even

question_prev = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    name = cli.welcome_user()
    engine.game_play(name, question_prev, even)


if __name__ == '__main__':
    main()
