import unittest

from .rearrange_arr_elements import merge, rearrange_digits


class TestMerge(unittest.TestCase):
    def test_merge_empty(self) -> None:
        """Tests the merge of 2 empty lists."""
        self.assertFalse(merge([], []))

    def test_merge_one_empty(self) -> None:
        """Tests the merge when one list is empty."""
        self.assertEqual([1], merge([1], []))
        self.assertEqual([1], merge([], [1]))

    def test_merge(self):
        """Tests the merge of 2 pre-sorted lists."""
        self.assertEqual([1, 2, 3, 4, 5], merge([1, 2, 3], [4, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], merge([1, 2, 3], [4, 5, 6]))
        self.assertEqual([1, 2, 3, 4, 5], merge([1, 3], [2, 4, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], merge([2, 3], [1, 4, 5, 6]))


class TestRearrangeDigits(unittest.TestCase):
    def test_empty_input(self) -> None:
        """Tests the error when the input is empty."""
        with self.assertRaises(ValueError):
            rearrange_digits([])

    def test_one_input(self) -> None:
        """Tests the errors when the input has only 1 digit."""
        with self.assertRaises(ValueError):
            rearrange_digits([1])

    def test_rearrange_digits(self) -> None:
        self.assertEqual([964, 852], rearrange_digits([4, 6, 2, 5, 9, 8]))
        self.assertEqual([531, 42],  rearrange_digits([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
