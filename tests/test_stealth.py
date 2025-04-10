import unittest
import time
from modules.stealth import random_delay, limit_applications

class TestStealth(unittest.TestCase):

    def test_random_delay_range(self):
        start = time.time()
        random_delay(0.1, 0.2)
        elapsed = time.time() - start
        self.assertGreaterEqual(elapsed, 0.1)
        self.assertLessEqual(elapsed, 0.25)

    def test_limit_applications(self):
        limiter = limit_applications(3, 1)
        counts = []
        for _ in range(5):
            counts.append(next(limiter))
        self.assertEqual(counts[:3], [0,1,2])
        # After cooldown, count resets
        self.assertEqual(counts[3], 0)
        self.assertEqual(counts[4], 1)

if __name__ == "__main__":
    unittest.main()