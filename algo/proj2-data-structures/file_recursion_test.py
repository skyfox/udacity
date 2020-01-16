import os
import unittest

from .file_recursion import find_files


class TestFilesFinder(unittest.TestCase):
    def test_find_files(self) -> None:
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

    def test_path_is_file_found(self) -> None:
        """Tests the case where path is a file and it exists."""
        result = find_files(".c", os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdir/t1.c"))
        self.assertEqual([os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdir/t1.c")], result)

    def test_path_is_file_not_found(self) -> None:
        """Tests the case where path is a file and it does not exist."""
        result = find_files(".c", os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdir/t1.h"))
        self.assertFalse(result)

    def test_find_empty(self) -> None:
        """Tests empty result return."""
        result = find_files(".bla",
                            os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdir"))
        self.assertFalse(result)

    def test_invalid_path(self) -> None:
        """Tests accessing non-existing path.

        If the is no such directory it is better to raise an exception. Function user decides what to do with it.
        """
        with self.assertRaises(FileNotFoundError):
            find_files(".bla", "/invalid/path")


if __name__ == '__main__':
    unittest.main()
