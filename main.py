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

"""
Delete: the product was imported yesterday (before), but was not imported today (after). 
This means we have to send a delete operation to the advertisement channel.
"""
def get_delete_operations_list(before = [], after = []):
    row_after = [row_after["id"] for row_after in after]

    # Get only ids comparison
    row_before = []
    for row in before:
        if row["id"] not in row_after:
            d = {}
            d["id"] = row["id"]
            row_before.append(d)
    return row_before

def get_update_operations_list(before = [], after = []):
    # Get list ids
    before_copy = []
    for row in before:
        before_copy.append(row)

    after_copy = []
    for row in after:
        after_copy.append(row)        

    before_list = [row_before["id"] for row_before in before_copy]
    after_list = [row_after["id"] for row_after in after_copy]

    """ 
    Get left and right lists that intersects by id 
    """ 
    # Before partitioning
    before_partitioning = [
        dict(row_before)
        for row_before in before_copy
        if row_before["id"] in after_list]

    # After partitioning
    after_partitioning = [
        dict(row_after)
        for row_after in after_copy
        if row_after["id"] in before_list]

    # Get difference (filds thas was updated) between lists
    row_after_partitioning = [row_after_partitioning for row_after_partitioning in after_partitioning
        if row_after_partitioning not in before_partitioning]
    
    # Return after product list that exists on before product list
    # and shows differences between fields
    return row_after_partitioning



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
    print(f"Create operations (type: List of dictionaries):\n{create_operations_list}\n")

    # Set file objects position to the beginning for the next data retrieval.
    before_csv.seek(0)
    after_csv.seek(0)

    # Get delete operations list
    delete_operations_list = get_delete_operations_list(before_dict, after_dict)
    # TODO: Implement channel integration
    print(f"Delete operations (type: Set of ids):\n{delete_operations_list}\n")

    # Set file objects position to the beginning for the next data retrieval.
    before_csv.seek(0)
    after_csv.seek(0)

    # Get update operations list
    update_operations_list = get_update_operations_list(before_dict, after_dict)
    # TODO: Implement channel integration
    print(f"Update operations (type: List of dictionaries):\n{update_operations_list}\n")

    before_csv.close()
    after_csv.close()
