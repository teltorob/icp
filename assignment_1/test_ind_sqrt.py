import unittest
import ind_sqrt
import math


class TestSqrt(unittest.TestCase):

    def test_root(self):
        for i in range(1000):
            result = ind_sqrt.main(i)
            self.assertEqual(result, math.isqrt(i), f'Test for {i}')


if __name__ == "__main__":
    unittest.main()
