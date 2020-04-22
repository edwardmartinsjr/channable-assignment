import unittest
import main

# START TESTS
class Test(unittest.TestCase):

    def test_parse_args(self):
        args = main.parse_args(["path_to_before_csv","path_to_after_csv"])
        self.assertEqual(args.path_to_before_csv, "path_to_before_csv")
        self.assertEqual(args.path_to_after_csv, "path_to_after_csv")

unittest.main()
