# tic_tac_toe.py

import random

# Constants
PLAYER = "X"
COMPUTER = "O"
EMPTY = " "

# Game board
board = [EMPTY for _ in range(9)]

def print_board():
    """Display the current state of the board."""
    print("\nCurrent board:")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---+---+---")
    print()

def check_win(symbol: str) -> bool:
    """Check if the given symbol has a winning combination."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in win_conditions)

def board_full() -> bool:
    """Check if the board is full."""
    return EMPTY not in board

def player_move():
    """Prompt the player to make a move."""
    while True:
        try:
            move = int(input("🔢 Enter your move (1–9): ")) - 1
            if move not in range(9):
                print("❌ Please enter a number between 1 and 9.")
            elif board[move] != EMPTY:
                print("❌ Cell already occupied. Try again.")
            else:
                board[move] = PLAYER
                break
        except ValueError:
            print("❌ Invalid input. Enter a number between 1 and 9.")

def computer_move():
    """Let the computer choose a move."""
    empty_cells = [i for i, cell in enumerate(board) if cell == EMPTY]
    move = random.choice(empty_cells)
    board[move] = COMPUTER
    print(f"🤖 Computer chose position {move + 1}")

def play_game():
    """Main game loop."""
    global board
    board = [EMPTY for _ in range(9)]
    print("🎮 Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()
        if check_win(PLAYER):
            print("🎉 You win!")
            break
        if board_full():
            print("🤝 It's a tie!")
            break

        # Computer's turn
        computer_move()
        print_board()
        if check_win(COMPUTER):
            print("💻 Computer wins!")
            break
        if board_full():
            print("🤝 It's a tie!")
            break

def main():
    """Game entry point with replay option."""
    while True:
        play_game()
        again = input("🔁 Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
