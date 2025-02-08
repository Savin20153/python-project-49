from brain_games import engine
from brain_games.games import progression


def main():
    engine.game_play(progression.QUESTION, progression)


if __name__ == '__main__':
    main()