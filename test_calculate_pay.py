from unittest import TestCase
import calculate_pay


class TestCalculatePay(TestCase):
    def test_calculate_pay_with_less_than_40_hours_and_positive_wage(self):
        actual = calculate_pay.calculate_pay(30.00, 20.00)
        expected = 600.00
        self.assertEqual(actual, expected)

    def test_calculate_pay_with_more_than_40_hours_and_positive_wage(self):
        actual = calculate_pay.calculate_pay(60.00, 20.00)
        expected = 1600.00
        self.assertEqual(actual, expected)

    def test_calculate_pay_with_positive_hours_and_negative_wage(self):
        actual = calculate_pay.calculate_pay(30.00, -20.00)
        expected = 0.00
        self.assertEqual(actual, expected)

    def test_calculate_pay_with_negative_hours_and_negative_wage(self):
        actual = calculate_pay.calculate_pay(-30.00, -20.00)
        expected = 0.00
        self.assertEqual(actual, expected)

    def test_calculate_pay_with_zero_hours_and_positive_wage(self):
        actual = calculate_pay.calculate_pay(0.00, 20.00)
        expected = 0.00
        self.assertEqual(actual, expected)

    def test_calculate_pay_with_zero_hours_and_negative_wage(self):
        actual = calculate_pay.calculate_pay(0.00, -20.00)
        expected = 0.00
        self.assertEqual(actual, expected)

    def test_calculate_pay_with_zero_hours_and_zero_wage(self):
        actual = calculate_pay.calculate_pay(0.00, 0.00)
        expected = 0.00
        self.assertEqual(actual, expected)

    def test_calculate_pay_with_zero_hours_and_negative_wage(self):
        actual = calculate_pay.calculate_pay(0.00, -20.00)
        expected = 0.00
        self.assertEqual(actual, expected)
