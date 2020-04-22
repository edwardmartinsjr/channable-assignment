import sys
import argparse
from argparse import RawTextHelpFormatter

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_before_csv', type=str)
    parser.add_argument('path_to_after_csv', type=str)

    return parser.parse_args(args)


if __name__ == '__main__':
    parse_args(sys.argv[1:])
