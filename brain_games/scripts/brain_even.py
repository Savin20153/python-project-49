from brain_games import engine
from brain_games.games import even


def main():
    engine.game_play(even.QUESTION, even)


if __name__ == '__main__':
    main()
