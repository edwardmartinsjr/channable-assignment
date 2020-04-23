import sys
import argparse
from argparse import RawTextHelpFormatter
import logging

# create logger
logger = logging.getLogger("channable-assignment")
logger.setLevel(logging.DEBUG)

def parse_args(args):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("path_to_before_csv", type=str)
        parser.add_argument("path_to_after_csv", type=str)
        return parser.parse_args(args)
    except SystemExit as err:
        logger.error(f"Can\'t find all arguments: Error code [{err}]")
        raise SystemExit()

def open_file(path_to_open):
    try:
        with open(path_to_open, "r") as file:
            return file.read()
    except IOError as err:
        logger.error(f"Can\'t find file or read data: {err}")
        raise SystemExit()


if __name__ == "__main__":

    args = parse_args(sys.argv[1:])
    path_to_before_csv = open_file(args.path_to_before_csv)
    path_to_after_csv = open_file(args.path_to_after_csv)

