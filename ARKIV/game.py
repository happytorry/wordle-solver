"""
Interactive Wordle game and solver modes.
"""

from solver import WordleSolver, LetterStatus
from word_list import load_word_list
from typing import Optional


class WordleGame:
    """Interactive Wordle game with solver assistance."""
    
    def __init__(self, target_word: Optional[str] = None):
        """
        Initialize the game.
        
        Args:
            target_word: The word to solve for. If None, word list is used for suggestions only.
        """
        self.word_list = load_word_list()
        self.solver = WordleSolver(self.word_list)
        self.target_word = target_word.upper() if target_word else None
        self.attempts = 0
        self.max_attempts = 6
        self.guesses = []
        
    def get_feedback(self, guess: str) -> str:
        """
        Generate feedback for a guess.
        
        Args:
            guess: The guessed word
            
        Returns:
            Feedback string with R (green), Y (yellow), G (gray)
        """
        if not self.target_word:
            return None
        
        guess = guess.upper()
        feedback = ['G'] * 5
        target_letters = list(self.target_word)
        
        # First pass: mark correct positions (green)
        for i, letter in enumerate(guess):
            if letter == self.target_word[i]:
                feedback[i] = 'R'
                target_letters[i] = None
        
        # Second pass: mark wrong positions (yellow)
        for i, letter in enumerate(guess):
            if feedback[i] == 'G' and letter in target_letters:
                feedback[i] = 'Y'
                target_letters[target_letters.index(letter)] = None
        
        return ''.join(feedback)
    
    def play_interactive(self) -> None:
        """Play an interactive game where user enters guesses and feedback."""
        print("\n=== Wordle Solver - Interactive Mode ===")
        print(f"Remaining candidates: {self.solver.get_remaining_count()}")
        
        while self.attempts < self.max_attempts:
            print(f"\nAttempt {self.attempts + 1}/{self.max_attempts}")
            
            # Get suggestion
            suggestion = self.solver.get_best_guess(1)
            if suggestion:
                print(f"Suggested guess: {suggestion[0]}")
            
            # Get user input
            guess = input("Enter your guess (or 'q' to quit): ").strip().upper()
            if guess == 'Q':
                break
            
            if len(guess) != 5 or not guess.isalpha():
                print("Please enter a valid 5-letter word.")
                continue
            
            if guess not in self.word_list:
                print(f"'{guess}' is not in the word list.")
                continue
            
            # Get feedback
            feedback = input("Enter feedback (R=green, Y=yellow, G=gray): ").strip().upper()
            if len(feedback) != 5 or not all(c in 'RYG' for c in feedback):
                print("Feedback must be 5 characters: R, Y, or G")
                continue
            
            # Process feedback
            self.guesses.append((guess, feedback))
            self.solver.filter_by_feedback(guess, feedback)
            self.attempts += 1
            
            print(f"Remaining candidates: {self.solver.get_remaining_count()}")
            
            if self.solver.get_remaining_count() == 0:
                print("No valid candidates found. Check your feedback.")
                break
            
            if self.solver.get_remaining_count() == 1:
                print(f"Found it! The word is: {list(self.solver.candidates)[0]}")
                break
    
    def play_auto(self) -> bool:
        """
        Automatically solve a puzzle (requires target_word).
        
        Returns:
            True if solved, False if not solved within attempts
        """
        if not self.target_word:
            print("Auto mode requires a target word.")
            return False
        
        print(f"\n=== Wordle Solver - Auto Mode ===")
        print(f"Target: {self.target_word} (hidden)")
        
        while self.attempts < self.max_attempts:
            # Get best guess
            guess = self.solver.get_best_guess(1)[0] if self.solver.get_best_guess(1) else None
            
            if not guess:
                print("No valid candidates found.")
                return False
            
            self.attempts += 1
            print(f"\nAttempt {self.attempts}: {guess}")
            
            # Get feedback
            feedback = self.get_feedback(guess)
            print(f"Feedback: {feedback}")
            
            self.guesses.append((guess, feedback))
            
            if guess == self.target_word:
                print(f"\n✓ Solved in {self.attempts} attempts!")
                return True
            
            # Filter candidates
            self.solver.filter_by_feedback(guess, feedback)
            print(f"Remaining candidates: {self.solver.get_remaining_count()}")
        
        print(f"\n✗ Failed to solve in {self.max_attempts} attempts.")
        print(f"The word was: {self.target_word}")
        return False
    
    def get_statistics(self) -> dict:
        """Return game statistics."""
        return {
            'attempts': self.attempts,
            'max_attempts': self.max_attempts,
            'solved': self.target_word in [guess for guess, _ in self.guesses] if self.guesses else False,
            'guesses': self.guesses,
            'remaining_candidates': self.solver.get_remaining_count()
        }
