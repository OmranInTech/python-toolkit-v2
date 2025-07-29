import time
import sys

def print_slow(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_hint(word, guessed):
    for char in word:
        if char not in guessed:
            return f"Hint: The word contains the letter '{char}'"
    return "No hints available."
