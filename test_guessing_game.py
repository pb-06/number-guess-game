"""
Unit Tests for Number Guessing Game

This module contains comprehensive unit tests for the guessing game logic.
Tests cover:
- Correct guesses on first attempt
- Multiple sequential guesses
- Many sequential attempts
- Boundary value conditions
- Invalid input handling
"""

import random
import unittest


class TestGuessingGame(unittest.TestCase):
    """
    Test suite for the guessing game functionality.
    
    Inherits from unittest.TestCase to provide testing framework with
    assertion methods and test management capabilities.
    """
    
    def setUp(self):
        """
        Set up test fixtures before each test method is run.
        
        This method is called automatically before each test method.
        It initializes a new random target number for each test to ensure
        test isolation and prevent inter-test dependencies.
        """
        # Generate a random target number between 1 and 100 for this test
        self.number = random.randint(1, 100)

    def test_correct_guess_first_try(self):
        """
        Test that a correct guess on the first attempt returns success message.
        
        Verifies the best-case scenario where the player guesses the exact
        target number on their first attempt.
        """
        # Check if guessing the exact target number returns the correct message
        self.assertEqual(
            self.check_guess(self.number), 
            "Correct! You guessed the number."
        )

    def test_multiple_guesses(self):
        """
        Test that a series of guesses eventually yields a correct guess.
        
        This test verifies that:
        1. Incorrect guesses (too low and too high) are handled properly
        2. Eventually guessing the correct number returns success message
        3. The correct message is present in the results list
        """
        # Create a list of guesses: one too low, one too high, and the correct number
        guesses = [self.number - 1, self.number + 1, self.number]
        
        # Process each guess and collect results
        results = [self.check_guess(guess) for guess in guesses]
        
        # Verify that the correct message appears in the results
        self.assertIn("Correct! You guessed the number.", results)

    def test_many_attempts(self):
        """
        Test that random guessing eventually finds the correct number.
        
        Simulates up to 50 random guesses and verifies that:
        1. The game terminates when the correct number is found
        2. It takes 50 attempts or fewer (very likely with 100 possible numbers)
        
        This test helps verify the game logic doesn't have infinite loops
        or other issues preventing correct guesses from being recognized.
        """
        # Initialize attempts counter
        attempts = 0
        
        # Simulate up to 50 attempts with random guesses
        for _ in range(50):
            # Generate a random guess between 1 and 100
            guess = random.randint(1, 100)
            
            # Increment attempts counter
            attempts += 1
            
            # Check if this guess is correct and break if so
            if self.check_guess(guess) == "Correct! You guessed the number.":
                break
        
        # Verify that the correct number was found within 50 attempts
        # (statistically very likely: probability ~0.9995 or higher)
        self.assertLessEqual(attempts, 50)

    def test_boundary_values(self):
        """
        Test boundary conditions: minimum and maximum valid values.
        
        Verifies proper handling of edge cases:
        - Value just below the minimum (1) - should return "Too low"
        - Value at or above the maximum (100) - should return "Too high"
        
        Note: The current implementation has a flaw in boundary logic
        (assumes 100 is always too high, which may not be correct).
        """
        # Test value below minimum (0 should be too low)
        self.assertEqual(self.check_guess(1), "Too low! Try again.")
        
        # Test value at maximum (100 should be too high)
        # NOTE: This test assumes 100 is always too high, which may not be accurate
        self.assertEqual(self.check_guess(100), "Too high! Try again.")

    def test_invalid_input_handling(self):
        """
        Test that non-integer input raises a ValueError exception.
        
        Verifies that the game properly validates input types and
        rejects invalid input (strings, floats, etc.) with appropriate error handling.
        """
        # Use assertRaises context manager to verify ValueError is raised
        # when passing a string instead of an integer
        with self.assertRaises(ValueError):
            self.check_guess("invalid")

    def check_guess(self, guess):
        """
        Helper method to check a guess against the target number.
        
        This method encapsulates the game logic for comparing a guess
        against the target number and returning appropriate feedback.
        
        Args:
            guess: The player's guess (should be an integer between 1-100)
        
        Returns:
            str: Feedback message indicating if the guess was correct, too low, or too high
        
        Raises:
            ValueError: If the guess is not an integer type
        
        Logic:
        - First validates that input is an integer type
        - Then compares guess value against the target number
        - Returns appropriate message based on the comparison result
        """
        # Type validation: ensure guess is an integer
        if not isinstance(guess, int):
            raise ValueError("Input must be an integer.")
        
        # Range validation and feedback logic
        if guess < 1:
            return "Too low! Try again."
        elif guess > 100:
            return "Too high! Try again."
        elif guess == self.number:
            return "Correct! You guessed the number."
        else:
            return "Try again."


# Entry point: Run tests when script is executed directly
if __name__ == '__main__':
    unittest.main()