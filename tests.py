import unittest

from utils import sum_divs2


class TestSum(unittest.TestCase):
    def test_div_sum(self):
        """
        Test sum of divisors of a number
        """
        inputs, expectedOutputs = [1, 4, 6, 7, 24, 25], [1, 3, 6, 1, 36, 6]
        results = []
        for elem in inputs:
            results.append(sum_divs2(elem))

        for ex1, res1 in zip(expectedOutputs, results):
            self.assertEqual(ex1, res1)


if __name__ == "__main__":
    unittest.main()
