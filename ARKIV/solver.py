"""
Core solver logic for Wordle.
Filters word lists based on game feedback.
"""

from collections import Counter
from typing import Set, Tuple, Optional
from enum import Enum


class LetterStatus(Enum):
    """Feedback status for each letter."""
    CORRECT = 'green'      # Letter in correct position
    WRONG_POS = 'yellow'   # Letter in word, wrong position
    NOT_FOUND = 'gray'     # Letter not in word


class WordleSolver:
    """Main solver for Wordle puzzles."""
    
    def __init__(self, word_list: Set[str]):
        """
        Initialize solver with a word list.
        
        Args:
            word_list: Set of valid 5-letter words
        """
        self.word_list = word_list
        self.candidates = word_list.copy()
        self.excluded_letters = set()
        self.correct_positions = {}  # {position: letter}
        self.wrong_positions = {}   # {letter: set of positions}
        
    def filter_by_feedback(self, guess: str, feedback: str) -> None:
        """
        Filter candidates based on feedback.
        
        Args:
            guess: The 5-letter word guessed (uppercase)
            feedback: String of feedback, e.g., 'GYGYG'
                     G = gray (not in word)
                     Y = yellow (wrong position)
                     R = green (correct position) - using R instead of G for clarity
        """
        guess = guess.upper()
        feedback = feedback.upper()
        
        if len(guess) != 5 or len(feedback) != 5:
            raise ValueError("Guess and feedback must be exactly 5 characters")
        
        new_candidates = set()
        
        for candidate in self.candidates:
            is_valid = True
            
            for i, (letter, status) in enumerate(zip(guess, feedback)):
                if status == 'R':  # Correct position
                    if candidate[i] != letter:
                        is_valid = False
                        break
                        
                elif status == 'Y':  # Wrong position
                    if candidate[i] == letter or letter not in candidate:
                        is_valid = False
                        break
                    # Mark that this letter shouldn't be in this position
                    
                elif status == 'G':  # Not in word
                    if letter in candidate:
                        is_valid = False
                        break
            
            if is_valid:
                new_candidates.add(candidate)
        
        self.candidates = new_candidates
    
    def get_best_guess(self, num_suggestions: int = 1) -> list:
        """
        Get the best word(s) to guess next using frequency analysis.
        
        Args:
            num_suggestions: Number of suggestions to return
            
        Returns:
            List of suggested words ranked by expected information gain
        """
        if not self.candidates:
            return []
        
        if len(self.candidates) == 1:
            return list(self.candidates)
        
        # Calculate letter frequencies in remaining candidates
        letter_freq = Counter()
        position_freq = [Counter() for _ in range(5)]
        
        for word in self.candidates:
            for i, letter in enumerate(word):
                letter_freq[letter] += 1
                position_freq[i][letter] += 1
        
        # Score each candidate word
        word_scores = []
        for word in self.candidates:
            # Avoid duplicate letters in one guess
            unique_letters = set(word)
            score = sum(letter_freq[letter] for letter in unique_letters)
            word_scores.append((score, word))
        
        # Sort by score (descending) and return top suggestions
        word_scores.sort(reverse=True)
        return [word for _, word in word_scores[:num_suggestions]]
    
    def reset(self) -> None:
        """Reset solver to initial state."""
        self.candidates = self.word_list.copy()
        self.excluded_letters = set()
        self.correct_positions = {}
        self.wrong_positions = {}
    
    def get_remaining_count(self) -> int:
        """Get number of remaining candidate words."""
        return len(self.candidates)
    
    def get_candidates(self, limit: int = 10) -> list:
        """Get list of remaining candidates."""
        return sorted(list(self.candidates))[:limit]
