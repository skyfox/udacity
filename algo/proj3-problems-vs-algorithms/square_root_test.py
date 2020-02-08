import unittest

from .square_root import sqrt


class TestSqrt(unittest.TestCase):
    def test_zero(self) -> None:
        """Tests 0 as input."""
        self.assertFalse(sqrt(0))

    def test_usual(self) -> None:
        """Tests usual inputs."""
        self.assertEqual(3, sqrt(9))
        self.assertEqual(4, sqrt(16))
        self.assertEqual(1, sqrt(1))
        self.assertEqual(5, sqrt(27))

    def test_interval_bound(self):
        """Tests when the result is on the interval bound."""
        # In: math.sqrt(420)
        # Out: 20.493901531919196
        self.assertEqual(20, sqrt(420))
        # In: math.sqrt(421)
        # Out: 20.518284528683193
        self.assertEqual(21, sqrt(421))


if __name__ == '__main__':
    unittest.main()
