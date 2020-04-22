# Channable Assignment
1. This program is a single .py file
2. This program is written in python 3.7, using only python’s built-in libraries.
3. This program contains a main() method that:
    a. Takes `path_to_before_csv` and `path_to_after_csv` as input parameters (as a string and in this order).
    b. Returns 3 sets of operations (in this order):
        i create_operations (type: List of dictionaries)
        ii. update_operations (type: List of dictionaries)
        iii. delete_operations (type: Set of ids)
4. The dictionaries for the `create_operations` and `update_operations` should contain the full data of the products. The ids for the `delete_operation` should be the `id` columns of the products that should be deleted.
