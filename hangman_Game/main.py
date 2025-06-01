from game_engine import run_game

def main():
    print("🎮 Welcome to Hangman!")
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        run_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    print("👋 Thanks for playing Hangman!")

if __name__ == "__main__":
    main()
