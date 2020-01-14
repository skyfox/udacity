import os
import unittest

from .file_recursion import find_files


class TestFilesFinder(unittest.TestCase):
    def test_find_files(self):
        """Tests the usual behaviour of the find_files."""
        result = find_files(".c",
                            os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdir"))
        expected_result = [
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testdir/subdir1/a.c'),
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testdir/subdir3/subsubdir1/b.c'),
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testdir/subdir5/a.c'),
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testdir/t1.c')
        ]
        self.assertCountEqual(expected_result, result)

    def test_find_empty(self):
        """Tests empty result return."""
        result = find_files(".bla",
                            os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdir"))
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
