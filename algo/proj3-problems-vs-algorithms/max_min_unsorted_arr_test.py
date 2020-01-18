import random
import unittest

from .max_min_unsorted_arr import get_min_max


class TestGetMaxMin(unittest.TestCase):
    def test_empty_input(self):
        """Tests empty array as input."""
        min_num, max_num =  get_min_max([])
        self.assertEqual(float("inf"), min_num)
        self.assertEqual(float("-inf"), max_num)

    def test_1_element_in_arr(self):
        """Tests an array with one element as input."""
        min_num, max_num = get_min_max([42])
        self.assertEqual(42, min_num)
        self.assertEqual(42, max_num)

    def test_typical_arr(self):
        """Tests an array with >2 elements as input."""
        min_num, max_num = get_min_max([1, 2, 3, 4, 5, -10, 8, 42, -6])
        self.assertEqual(-10, min_num)
        self.assertEqual(42, max_num)

    def test_rand_arr(self):
        """Tests an array with >2 elements, randomly shuffled as input."""
        l = [i for i in range(0, 10)]  # a list containing 0 - 9
        random.shuffle(l)
        min_num, max_num = get_min_max(l)
        self.assertEqual(0, min_num)
        self.assertEqual(9, max_num)


if __name__ == '__main__':
    unittest.main()
