# game_engine.py

import random
from utils import print_slow, get_hint
from word_list import word_bank

class HangmanGame:
    def __init__(self):
        self.total_score = 0

    def choose_category(self):
        while True:
            print("Categories:", ", ".join(word_bank.keys()))
            category = input("Choose a category: ").lower()
            if category in word_bank:
                return category
            print("❗ Invalid category. Please try again.")

    def choose_difficulty(self):
        while True:
            level = input("Difficulty (easy/medium/hard): ").lower()
            if level in ["easy", "medium", "hard"]:
                return level
            print("❗ Invalid difficulty. Please enter easy, medium, or hard.")

    def get_attempts(self, difficulty):
        return {"easy": 10, "medium": 7, "hard": 5}[difficulty]

    def display_word(self, word, guessed):
        return ' '.join([ch if ch in guessed else '_' for ch in word])

    def run_game(self):
        try:
            category = self.choose_category()
            difficulty = self.choose_difficulty()
            word = random.choice(word_bank[category]).lower()
            guessed = set()
            attempts = self.get_attempts(difficulty)
            score = 0

            print_slow(f"\nStarting game in '{category.title()}' category at '{difficulty}' level.")

            while attempts > 0:
                print("\nWord:", self.display_word(word, guessed))
                print("Guessed letters:", ' '.join(sorted(guessed)) if guessed else "None")
                print(f"Attempts left: {attempts}")
                choice = input("Guess a letter or type 'hint': ").lower().strip()

                if choice == 'hint':
                    print(get_hint(word, guessed))
                    attempts -= 1
                    continue

                if not choice.isalpha() or len(choice) != 1:
                    print("❗ Enter a valid single letter.")
                    continue

                if choice in guessed:
                    print("🔁 Already guessed that letter.")
                    continue

                guessed.add(choice)

                if choice in word:
                    print("✅ Good job!")
                else:
                    attempts -= 1
                    print("❌ Wrong guess!")

                if all(c in guessed for c in word):
                    print(f"\n🎉 You won! The word was: {word}")
                    score += 10
                    break
            else:
                print(f"\n💀 Game over. The word was: {word}")

            print(f"🏆 Your Score: {score}")
            self.total_score += score
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")

    def ask_replay(self):
        while True:
            answer = input("\n🔁 Do you want to play again? (yes/no): ").lower().strip()
            if answer in ['yes', 'y']:
                return True
            elif answer in ['no', 'n']:
                return False
            else:
                print("❗ Please answer 'yes' or 'no'.")

    def main(self):
        print("Welcome to the Hangman Game!")
        while True:
            self.run_game()
            print(f"🎯 Total Score so far: {self.total_score}")
            if not self.ask_replay():
                print("👋 Thanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    game = HangmanGame()
    game.main()
