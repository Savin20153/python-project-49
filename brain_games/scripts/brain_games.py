import sys

sys.path.append('/home/fedorpc/projects/python-project-49/brain_games')
from cli import greet, welcome_user


def main():
    greet()
    welcome_user()


if __name__ == "__main__":
    main()
