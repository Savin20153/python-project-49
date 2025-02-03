import sys

sys.path.append('/home/fedorpc/projects/python-project-49/brain_games')
from cli import greet, is_this_calculated_correctly, welcome_user


def main():
    greet()
    name = welcome_user()
    is_this_calculated_correctly(name)


if __name__ == '__main__':
    main()