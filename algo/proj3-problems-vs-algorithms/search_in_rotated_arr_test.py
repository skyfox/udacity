import unittest

from .search_in_rotated_arr import find_pivot, rotated_array_search


class TestFindPivot(unittest.TestCase):
    def test_zero(self) -> None:
        """Tests no rotation array."""
        self.assertEqual(0, find_pivot([0, 2, 4, 6, 8, 10]))

    def test_one(self) -> None:
        """Tests 1 element rotation."""
        self.assertEqual(1, find_pivot([10, 0, 2, 4, 6, 8]))

    def test_max(self) -> None:
        """Tests fully rotation array - pivot is the last element."""
        self.assertEqual(5, find_pivot([2, 4, 6, 8, 10, 1]))

    def test_usual(self):
        """Tests multiple regular rotations."""
        self.assertEqual(3, find_pivot([6, 8, 10, 1, 2, 3, 4]))
        self.assertEqual(4, find_pivot([4, 6, 8, 10, 1, 2, 3]))


class TestRotatedArraySearch(unittest.TestCase):
    def test_zero_rotation(self):
        """Tests search in 0-rotated array."""
        self.assertEqual(0, rotated_array_search([2, 4, 6, 8, 10, 12], 2))
        self.assertEqual(0, rotated_array_search([2, 4, 6, 8, 10, 12, 14], 2))
        self.assertEqual(4, rotated_array_search([2, 4, 6, 8, 10, 12], 10))
        self.assertEqual(4, rotated_array_search([2, 4, 6, 8, 10, 12, 14], 10))
        self.assertEqual(5, rotated_array_search([2, 4, 6, 8, 10, 12], 12))
        self.assertEqual(6, rotated_array_search([2, 4, 6, 8, 10, 12, 14], 14))

    def test_max_rotation(self):
        """Tests search in len-1 rotated array."""
        self.assertEqual(5, rotated_array_search([4, 6, 8, 10, 12, 2], 2))
        self.assertEqual(6, rotated_array_search([4, 6, 8, 10, 12, 14, 2], 2))
        self.assertEqual(3, rotated_array_search([4, 6, 8, 10, 12, 2], 10))
        self.assertEqual(3, rotated_array_search([4, 6, 8, 10, 12, 14, 2], 10))
        self.assertEqual(4, rotated_array_search([4, 6, 8, 10, 12, 2], 12))
        self.assertEqual(5, rotated_array_search([4, 6, 8, 10, 12, 14, 2], 14))

    def test_usual_rotation(self):
        """Tests search in a few elements rotated array."""
        self.assertEqual(4, rotated_array_search([4, 5, 6, 7, 1, 2, 3], 1))
        self.assertEqual(5, rotated_array_search([4, 5, 6, 7, 8, 1, 2, 3], 1))
        self.assertEqual(1, rotated_array_search([4, 5, 6, 7, 1, 2, 3], 5))
        self.assertEqual(1, rotated_array_search([4, 5, 6, 7, 8, 1, 2, 3], 5))
        self.assertEqual(3, rotated_array_search([4, 5, 6, 7, 1, 2, 3], 7))
        self.assertEqual(4, rotated_array_search([4, 5, 6, 7, 8, 1, 2, 3], 8))


if __name__ == '__main__':
    unittest.main()
