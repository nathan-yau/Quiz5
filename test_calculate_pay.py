from unittest import TestCase
import calculate_pay


class TestCalculatePay(TestCase):
    def test_calculate_pay(self):
        actual = calculate_pay.calculate_pay(30.00, 20.00)
        expected = 600.00
        self.assertEqual(actual, expected)
