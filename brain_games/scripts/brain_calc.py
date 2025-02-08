from brain_games import engine
from brain_games.games import calc


def main():
    engine.game_play(calc.QUESTION, calc)


if __name__ == '__main__':
    main()