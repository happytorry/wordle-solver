"""
Main entry point for Wordle Solver.
Provides interactive CLI to test the solver.
"""

import sys
from game import WordleGame
from solver import WordleSolver
from word_list import load_word_list


def main_menu() -> None:
    """Display and handle main menu."""
    while True:
        print("\n" + "="*50)
        print("WORDLE SOLVER")
        print("="*50)
        print("1. Interactive Mode (You play, solver suggests)")
        print("2. Auto Solver Mode (Solver plays automatically)")
        print("3. Test Solver (Solve all words in dictionary)")
        print("4. Exit")
        print("="*50)
        
        choice = input("Choose mode (1-4): ").strip()
        
        if choice == '1':
            interactive_mode()
        elif choice == '2':
            auto_solver_mode()
        elif choice == '3':
            test_solver()
        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


def interactive_mode() -> None:
    """User plays, solver provides suggestions."""
    print("\nInteractive Mode: Enter your guesses and feedback")
    print("Feedback codes: R=Correct (green), Y=Wrong position (yellow), G=Not in word (gray)")
    
    game = WordleGame()
    game.play_interactive()
    
    stats = game.get_statistics()
    print(f"\nGame Statistics:")
    print(f"  Attempts: {stats['attempts']}/{stats['max_attempts']}")
    print(f"  Remaining candidates: {stats['remaining_candidates']}")


def auto_solver_mode() -> None:
    """Solver automatically solves a word."""
    print("\nAuto Solver Mode")
    
    word_list = load_word_list()
    test_word = input("Enter a 5-letter word to solve (or leave blank for random): ").strip().upper()
    
    if not test_word:
        import random
        test_word = random.choice(list(word_list))
        print(f"Using random word: {test_word}")
    elif len(test_word) != 5:
        print("Word must be 5 letters.")
        return
    
    game = WordleGame(target_word=test_word)
    game.play_auto()
    
    stats = game.get_statistics()
    print(f"\nGame Statistics:")
    print(f"  Attempts: {stats['attempts']}/{stats['max_attempts']}")


def test_solver() -> None:
    """Test solver on sample words from dictionary."""
    print("\nTesting Solver on Dictionary Words...")
    
    word_list = load_word_list()
    test_sample = input("How many words to test (default: 10, max: 100)? ").strip()
    
    try:
        num_tests = int(test_sample) if test_sample else 10
        num_tests = min(max(num_tests, 1), 100)
    except ValueError:
        num_tests = 10
    
    import random
    test_words = random.sample(sorted(word_list), min(num_tests, len(word_list)))
    
    total_attempts = 0
    successes = 0
    
    for i, word in enumerate(test_words, 1):
        game = WordleGame(target_word=word)
        solved = game.play_auto()
        
        if solved:
            successes += 1
            total_attempts += game.attempts
        
        if i < len(test_words):
            input("Press Enter for next word...")
    
    print(f"\n" + "="*50)
    print("TEST RESULTS")
    print("="*50)
    print(f"Words tested: {num_tests}")
    print(f"Successful: {successes}/{num_tests}")
    print(f"Success rate: {100*successes/num_tests:.1f}%")
    if successes > 0:
        print(f"Average attempts: {total_attempts/successes:.2f}")
    print("="*50)


def demo() -> None:
    """Run a quick demo."""
    print("\n" + "="*50)
    print("WORDLE SOLVER DEMO")
    print("="*50)
    
    word_list = load_word_list()
    solver = WordleSolver(word_list)
    
    print(f"\nLoaded {len(word_list)} words")
    print(f"Example words: {', '.join(sorted(word_list)[:5])}...")
    
    # Demo: simulate a solve
    print("\n--- Demo Solve ---")
    print("Let's solve for 'SLATE':")
    
    # Simulate guesses and feedback
    demo_sequence = [
        ('STARE', 'RGYGG'),  # S correct, T yellow, rest gray
        ('SHALE', 'RGRGG'),  # S and A correct
        ('SLATE', 'RRRRR'),  # All correct!
    ]
    
    for guess, feedback in demo_sequence:
        print(f"\nGuess: {guess}")
        print(f"Feedback: {feedback}")
        solver.filter_by_feedback(guess, feedback)
        print(f"Remaining candidates: {solver.get_remaining_count()}")
        if solver.get_remaining_count() <= 5:
            print(f"Candidates: {solver.get_candidates()}")


if __name__ == '__main__':
    # Show demo first
    demo()
    
    # Then show menu
    print("\n")
    input("Press Enter to continue to main menu...")
    main_menu()
