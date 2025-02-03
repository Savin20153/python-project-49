import sys

sys.path.append('/home/fedorpc/projects/python-project-49/brain_games')
from cli import greet, it_is_an_even_number, welcome_user


def main():
    greet()
    name = welcome_user()
    it_is_an_even_number(name)


if __name__ == '__main__':
    main()
