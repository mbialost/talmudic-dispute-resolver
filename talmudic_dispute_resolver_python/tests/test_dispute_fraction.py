import unittest
from talmudic_dispute_resolver.src.models.dispute_fraction import DisputeFraction, validate_claim
from fractions import Fraction
from talmudic_dispute_resolver.src.exceptions.fraction_error import FractionRangeError




class TestDisputeFraction(unittest.TestCase):

    def test_valid_arithmetic_operations(self):
        # Test cases for valid operations within [0, 1] range
        cases = [
            (DisputeFraction(1, 4), DisputeFraction(1, 4), '+', DisputeFraction(1, 2)),
            (DisputeFraction(3, 4), DisputeFraction(1, 4), '-', DisputeFraction(1, 2)),
            (DisputeFraction(1, 2), DisputeFraction(1, 2), '*', DisputeFraction(1, 4)),
            (DisputeFraction(1, 2), DisputeFraction(1, 2), '/', DisputeFraction(1, 1)),
        ]

        for a, b, op, expected in cases:
            with self.subTest(a=a, b=b, op=op):
                if op == '+':
                    result = a + b
                elif op == '-':
                    result = a - b
                elif op == '*':
                    result = a * b
                elif op == '/':
                    result = a / b
                self.assertEqual(result, expected, f"Failed for {a} {op} {b}")

    def test_reflected_arithmetic_operations(self):
        # Test reflected operations with DisputeFraction on the right
        a = 0.5  # Using a float for the left-hand side
        b = DisputeFraction(1, 4)  # DisputeFraction on the right
        cases = [
            (a, b, '__radd__', DisputeFraction(3, 4)),
            (a, b, '__rsub__', DisputeFraction(1, 4)),
            (a, b, '__rmul__', DisputeFraction(1, 8)),
            (a, b, '__rtruediv__', FractionRangeError),  # This should raise an error due to result > 1
        ]

        for a, b, op, expected in cases:
            with self.subTest(a=a, b=b, op=op):
                if op == '__radd__':
                    result = b.__radd__(a)
                elif op == '__rsub__':
                    result = b.__rsub__(a)
                elif op == '__rmul__':
                    result = b.__rmul__(a)
                elif op == '__rtruediv__':
                    with self.assertRaises(expected):
                        result = b.__rtruediv__(a)
                    continue
                self.assertEqual(result, expected, f"Failed for {a} {op} {b}")
    
    def test_invalid_operations(self):
        # Test invalid operations that should raise exceptions
        a = DisputeFraction(1, 1)
        b = DisputeFraction(0, 1)
        with self.subTest(msg="Division by zero"):
            with self.assertRaises(ZeroDivisionError):
                _ = a / b

        with self.subTest(msg="Result out of range"):
            with self.assertRaises(FractionRangeError):
                _ = DisputeFraction(1, 2) + DisputeFraction(3, 4)

    def test_validate_claim(self):
        # Test validate_claim function with various inputs
        valid_inputs = [0.25, Fraction(1, 4), DisputeFraction(1, 4)]
        for input_val in valid_inputs:
            with self.subTest(input_val=input_val):
                result = validate_claim(input_val)
                self.assertIsInstance(result, DisputeFraction)
                self.assertTrue(0 <= result <= 1)

        invalid_inputs = [1.5, -0.1, 'invalid', 2, -1]
        for input_val in invalid_inputs:
            with self.subTest(input_val=input_val):
                with self.assertRaises((TypeError, FractionRangeError)):
                    validate_claim(input_val)


if __name__ == '__main__':
    unittest.main()
