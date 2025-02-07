from brain_games import cli, engine
from brain_games.games import prime

question_prev = 'What number is missing in the progression?'


def main():
    name = cli.welcome_user()
    engine.game_play(name, question_prev, prime)


if __name__ == '__main__':
    main()