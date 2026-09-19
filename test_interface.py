"""End-to-end checks for the calculator's keyboard interface."""

import subprocess
import sys
import unittest
from pathlib import Path


CALCULATOR = Path(__file__).with_name("calculator.py")


class CalculatorInterfaceTests(unittest.TestCase):
    def run_calculator(self, inputs):
        result = subprocess.run(
            [sys.executable, str(CALCULATOR)],
            input="\n".join(inputs) + "\n",
            text=True,
            capture_output=True,
            timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_invalid_number_retries_same_field(self):
        output = self.run_calculator(["1", "oops", "10", "5", "n"])
        self.assertIn("Please enter a number", output)
        self.assertIn("Result: 10.0 + 5.0 = 15.0", output)

    def test_cancel_from_second_field_then_start_another_calculation(self):
        output = self.run_calculator(["4", "10", "n", "3", "2", "5", "n"])
        self.assertIn("Calculation canceled. Returning to menu.", output)
        self.assertIn("Result: 2.0 * 5.0 = 10.0", output)

    def test_zero_division_shows_message_and_returns_to_menu(self):
        output = self.run_calculator(["4", "10", "0", "n"])
        self.assertIn("Cannot calculate: Division by zero is not allowed.", output)
        self.assertIn("Calculator closed.", output)

    def test_invalid_choice_and_keyboard_exit(self):
        output = self.run_calculator(["9", "N"])
        self.assertIn("Please choose 1, 2, 3, 4, or n.", output)
        self.assertIn("Calculator closed.", output)


if __name__ == "__main__":
    unittest.main()
