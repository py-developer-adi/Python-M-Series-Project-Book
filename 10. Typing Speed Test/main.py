'''PYCODE | @_py.code'''

# ? 10. Typing Speed Test
# ? Features: Measure typing speed and accuracy.

# * Source Code
import time
import random

# Sample texts for testing
TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and easy to learn programming language.",
    "Practice makes perfect, and persistence is the key to success.",
    "Typing is an essential skill in the modern digital age."
]

def get_random_text():
    """Select a random text from the list."""
    return random.choice(TEXTS)

def calculate_speed_accuracy(start_time, end_time, given_text, user_input):
    """Calculate typing speed and accuracy."""
    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    words_per_minute = (words_typed / elapsed_time) * 60

    # Calculate accuracy
    given_words = given_text.split()
    user_words = user_input.split()
    correct_words = sum(1 for gw, uw in zip(given_words, user_words) if gw == uw)
    total_words = len(given_words)
    accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0

    return round(words_per_minute, 2), round(accuracy, 2)

def typing_test():
    print("\n--- Typing Speed and Accuracy Test ---")
    given_text = get_random_text()
    print("\nType the following text:")
    print(f"\n\"{given_text}\"\n")

    input("Press Enter to start...")

    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()

    wpm, accuracy = calculate_speed_accuracy(start_time, end_time, given_text, user_input)
    print("\n--- Test Results ---")
    print(f"Typing Speed: {wpm} words per minute (WPM)")
    print(f"Accuracy: {accuracy}%")
    print("\nThank you for taking the test!")

def main():
    while True:
        print("\n1. Start Typing Test")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            typing_test()
        elif choice == '2':
            print("Exiting Typing Speed Checker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
