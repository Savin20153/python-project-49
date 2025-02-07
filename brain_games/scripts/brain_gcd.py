from brain_games import cli, engine
from brain_games.games import gcd

question_prev = 'Find the greatest common divisor of given numbers.'


def main():
    name = cli.welcome_user()
    engine.game_play(name, question_prev, gcd)


if __name__ == '__main__':
    main()