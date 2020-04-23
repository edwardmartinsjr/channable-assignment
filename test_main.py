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
            self.assertEqual(main.open_file(path_to_open), "data")
            m.assert_called_with(path_to_open, "r")

    def test_open_patch_error(self):
        with self.assertRaises(SystemExit): main.open_file(path_to_open)


unittest.main()
