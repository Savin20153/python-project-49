from brain_games import cli, engine
from brain_games.games import prime

question_prev = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    name = cli.welcome_user()
    engine.game_play(name, question_prev, prime)


if __name__ == '__main__':
    main()