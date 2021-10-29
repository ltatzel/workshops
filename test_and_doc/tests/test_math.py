import random
import time
from unittest import TestCase
from unittest.mock import patch

from my_project.math import arithmetic_mean, geometric_mean, harmonic_mean


class TestMath(TestCase):
    """Class testing the math functions."""

    def setUp(self):

        current_time = time.time()
        random.seed(current_time)
        print("RNG seed is current time = {}".format(current_time))

    def test_calculate_amean(self):

        x = arithmetic_mean([7])
        self.assertEqual(x, 7)
        y = arithmetic_mean((2, 2))
        self.assertEqual(y, 2)
        z = arithmetic_mean({1, 2, 7})
        self.assertEqual(z, 10 / 3)

    def test_random(self):

        num_elements = random.randrange(10) + 1
        seq = []
        for _ in range(num_elements):
            seq.append(random.randrange(10))
        a_mean = arithmetic_mean(seq)

        # Check w.r.t. geo mean
        g_mean = geometric_mean(seq)
        self.assertLessEqual(g_mean, a_mean)

    def test_harm_uses_arithm(self):

        seq = [1, 2, 3]
        with patch('my_project.math.arithmetic_mean') as amean_mocked:

            _ = harmonic_mean(seq)
            amean_mocked.assert_called_once()
            args = [1 / x for x in seq]
            amean_mocked.assert_called_with(args)
