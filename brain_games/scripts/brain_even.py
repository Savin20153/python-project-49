from brain_games import cli, engine
from brain_games.games import even  # Исправлена ошибка с запятой

question_prev = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    name = cli.welcome_user()
    engine.game_play(name, question_prev, even)  # Передаем модуль even в game_play


if __name__ == '__main__':
    main()