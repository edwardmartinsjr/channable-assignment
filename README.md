# Channable Assignment

[![CircleCI](https://circleci.com/gh/edwardmartinsjr/channable-assignment/tree/master.svg?style=shield)](https://circleci.com/gh/edwardmartinsjr/channable-assignment/tree/master)

1. This program is a single .py file.

2. This program is written in python 3.7, using only python’s built-in libraries.

3. This program contains a main() method that:
	
    a. Takes `path_to_before_csv` and `path_to_after_csv` as input parameters (as a string and in this order).
	
    b. Returns 3 sets of operations (in this order):
	
    - create_operations (type: List of dictionaries)
	
    - update_operations (type: List of dictionaries)
	
    - delete_operations (type: Set of ids)

4. The dictionaries for the `create_operations` and `update_operations` contains the full data of the products. The ids for the `delete_operation` is the `id` columns of the products that should be deleted.

5. Test:
```
python test_main.py -v
```

6. Run:
```
python main.py product_inventory_before.csv product_inventory_after.csv
```
