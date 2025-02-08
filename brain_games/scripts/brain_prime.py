from brain_games import engine
from brain_games.games import prime


def main():
    engine.game_play(prime.QUESTION, prime)


if __name__ == '__main__':
    main()