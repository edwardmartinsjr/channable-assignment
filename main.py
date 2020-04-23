import sys
import argparse
import logging
import csv

# create logger
logger = logging.getLogger("channable-assignment")
logger.setLevel(logging.INFO)

def parse_args(args):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("path_to_before_csv", type=str)
        parser.add_argument("path_to_after_csv", type=str)
        return parser.parse_args(args)
    except SystemExit as err:
        logger.error(f"Can't find all arguments: Error code [{err}]")
        raise SystemExit()

def open_file(path_to_open):
    try:
        return open(path_to_open, "r")
    except IOError as err:
        logger.error(f"Can't find file or read data: {err}")
        raise SystemExit()

"""
Create: the product wasn’t imported from the eCommerce system yesterday (before), 
but it was imported today (after). This means we have to send a create operation 
to the eCommerce platform
"""
def get_create_operations_list(before = [], after = []):
    row_before = [row_before["id"] for row_before in before]
    row_after = [
        dict(row_after)
        for row_after in after
        if row_after["id"] not in row_before]    
    return row_after


if __name__ == "__main__":

    # Get args
    args = parse_args(sys.argv[1:])

    # open before and after csv file
    before_csv = open_file(args.path_to_before_csv)
    after_csv = open_file(args.path_to_after_csv)

    # transform csv to dictionary
    before_dict = csv.DictReader(before_csv, delimiter=",")
    after_dict = csv.DictReader(after_csv, delimiter=",")

    # Get create operations list
    create_operations_list = get_create_operations_list(before_dict, after_dict)
    # TODO: Implement channel integration
    print(f"Create operations (type: List of dictionaries):\n{create_operations_list}")


    before_csv.close()
    after_csv.close()


