import random
import unittest

class TestGuessingGame(unittest.TestCase):
    def setUp(self):
        self.number = random.randint(1, 100)  # random number for each test

    def test_correct_guess_first_try(self):
        self.assertEqual(self.check_guess(self.number), "Correct! You guessed the number.")

    def test_multiple_guesses(self):
        guesses = [self.number - 1, self.number + 1, self.number]
        results = [self.check_guess(guess) for guess in guesses]
        self.assertIn("Correct! You guessed the number.", results)

    def test_many_attempts(self):
        attempts = 0
        for _ in range(50):  # Simulate 50 attempts
            guess = random.randint(1, 100)
            attempts += 1
            if self.check_guess(guess) == "Correct! You guessed the number.":
                break
        self.assertLessEqual(attempts, 50)

    def test_boundary_values(self):
        self.assertEqual(self.check_guess(1), "Too low! Try again.")
        self.assertEqual(self.check_guess(100), "Too high! Try again.")

    def test_invalid_input_handling(self):
        with self.assertRaises(ValueError):
            self.check_guess("invalid")

    def check_guess(self, guess):
        if not isinstance(guess, int):
            raise ValueError("Input must be an integer.")
        if guess < 1:
            return "Too low! Try again."
        elif guess > 100:
            return "Too high! Try again."
        elif guess == self.number:
            return "Correct! You guessed the number."
        else:
            return "Try again."

if __name__ == '__main__':
    unittest.main()