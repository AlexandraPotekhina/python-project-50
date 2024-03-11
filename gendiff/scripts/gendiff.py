import argparse


def print_help_message():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(args)


def main():
    print_help_message()


if __name__ == '__main__':
    main()