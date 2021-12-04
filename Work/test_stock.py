# test_stock.py

import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.shares, 100)
        s.sell(30)
        self.assertEqual(s.shares, 70)
        s.sell(70)
        self.assertEqual(s.shares, 0)

    def test_shares_immutable(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = "20"


if __name__ == "__main__":
    unittest.main()
