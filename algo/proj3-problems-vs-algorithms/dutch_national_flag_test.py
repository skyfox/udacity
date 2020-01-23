import unittest

from .dutch_national_flag import sort_012


class TestSort021(unittest.TestCase):
    def test_empty_input(self) -> None:
        """Tests empty array as input."""
        result = sort_012([])
        self.assertFalse(result)

    def test_1_element_in_arr(self) -> None:
        """Tests an array with one element as input."""
        result = sort_012([1])
        self.assertEqual([1], result)

    def test_sorted_arr(self) -> None:
        """Tests a presorted array with >2 elements."""
        arr = [0, 0, 0, 1, 2, 2, 2, 2, 2]
        result = sort_012(arr)
        self.assertEqual(arr, result)

    def test_typical_use(self) -> None:
        """Tests an array with >2 elements."""
        arr1 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        self.assertEqual(sorted(arr1), sort_012(arr1))
        arr2 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        self.assertEqual(sorted(arr2), sort_012(arr2))
        arr3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(sorted(arr3), sort_012(arr3))


if __name__ == '__main__':
    unittest.main()
