import unittest
from monte_carlo_simulation import monte_carlo_pi

class TestMonteCarloPi(unittest.TestCase):

    def test_estimate_range(self):
        """Ensure π estimation is within a reasonable range."""
        for _ in range(10):  # Run multiple times to account for randomness
            estimate = monte_carlo_pi(10000)  # 10,000 samples as an example
            self.assertGreater(estimate, 2.5, "Estimated π is too low!")
            self.assertLess(estimate, 3.5, "Estimated π is too high!")

    def test_input_sizes(self):
        """Test different input sizes."""
        sizes = [10, 100, 1000, 10000, 100000]
        for s in sizes:
            estimate = monte_carlo_pi(s)
            self.assertIsNotNone(estimate, f"Failed to compute π for {s} samples")

if __name__ == '__main__':
    unittest.main()
