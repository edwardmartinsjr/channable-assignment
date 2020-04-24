import unittest
from unittest.mock import patch, mock_open
import main

path_to_open = "path/to/open"

# START TESTS
class Test(unittest.TestCase):

    def test_parse_args(self):
        args = main.parse_args(["path_to_before_csv","path_to_after_csv"])
        self.assertEqual(args.path_to_before_csv, "path_to_before_csv")
        self.assertEqual(args.path_to_after_csv, "path_to_after_csv")

    def test_parse_args_without_args(self):
        with self.assertRaises(SystemExit): main.parse_args([])

    def test_open_patch_success(self):
        with patch("builtins.open", mock_open(read_data="data"), create=True) as m:
            self.assertEqual(main.open_file(path_to_open).read(), "data")
            m.assert_called_with(path_to_open, "r")

    def test_open_patch_error(self):
        with self.assertRaises(SystemExit): main.open_file(path_to_open)

    def test_get_create_operations_list(self):
        create_operations_list = main.get_create_operations_list(
            [{"id":"1"}, {"id":"2"}, {"id":"3"}],
            [{"id":"3"}, {"id":"4"}, {"id":"5"}])
        self.assertEqual(create_operations_list, [{"id":"4"}, {"id":"5"}])

    def test_get_create_operations_list_with_empty_input(self):
        create_operations_list = main.get_create_operations_list()
        self.assertEqual(create_operations_list, [])

    def test_get_delete_operations_list(self):
        delete_operations_list = main.get_delete_operations_list(
            [{"id":"1"}, {"id":"2"}, {"id":"3"}],
            [{"id":"3"}, {"id":"4"}, {"id":"5"}])
        self.assertEqual(delete_operations_list, [{"id":"1"}, {"id":"2"}])

    def test_get_delete_operations_list_ids(self):
        delete_operations_list = main.get_delete_operations_list(
            [{"id":"1", "title":"test 1"}, {"id":"2", "title":"test 2"}, {"id":"3", "title":"test 3"}],
            [{"id":"3", "title":"test 3"}, {"id":"4", "title":"test 4"}, {"id":"5", "title":"test 5"}])
        self.assertEqual(delete_operations_list, [{"id":"1"}, {"id":"2"}])

    def test_get_delete_operations_list_with_empty_input(self):
        delete_operations_list = main.get_delete_operations_list()
        self.assertEqual(delete_operations_list, [])


unittest.main()
