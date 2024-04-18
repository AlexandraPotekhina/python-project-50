import argparse
from gendiff import generate_diff


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def parse_arguments():
    parser = argparse.ArgumentParser(DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
