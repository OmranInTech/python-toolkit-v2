import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import random

CARD_FILE = "flashcards.json"

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Flashcard App")
        self.root.geometry("400x300")
        self.flashcards = self.load_cards()
        self.current_card = None
        self.showing_answer = False

        self.label = tk.Label(root, text="Welcome to Flashcard App", font=("Arial", 16), wraplength=350, justify="center")
        self.label.pack(pady=30)

        tk.Button(root, text="➕ Add Flashcard", command=self.add_card, width=20).pack(pady=5)
        tk.Button(root, text="📖 Start Quiz", command=self.start_quiz, width=20).pack(pady=5)
        tk.Button(root, text="❌ Exit", command=root.quit, width=20).pack(pady=5)

    def add_card(self):
        front = simpledialog.askstring("Question", "Enter the question:")
        if not front:
            return
        back = simpledialog.askstring("Answer", "Enter the answer:")
        if not back:
            return
        self.flashcards.append({"front": front, "back": back})
        self.save_cards()
        messagebox.showinfo("Saved", "Flashcard saved!")

    def start_quiz(self):
        if not self.flashcards:
            messagebox.showwarning("No Cards", "No flashcards to quiz.")
            return
        self.quiz_window()

    def quiz_window(self):
        self.quiz = tk.Toplevel(self.root)
        self.quiz.title("Flashcard Quiz")
        self.quiz.geometry("400x300")

        self.card_label = tk.Label(self.quiz, text="", font=("Arial", 16), wraplength=350, justify="center")
        self.card_label.pack(pady=40)

        self.flip_button = tk.Button(self.quiz, text="🔄 Flip", command=self.flip_card)
        self.flip_button.pack(pady=5)

        tk.Button(self.quiz, text="⏭ Next", command=self.next_card).pack(pady=5)
        tk.Button(self.quiz, text="❌ Close", command=self.quiz.destroy).pack(pady=5)

        self.next_card()

    def flip_card(self):
        if not self.current_card:
            return
        if not self.showing_answer:
            self.card_label.config(text=self.current_card['back'])
        else:
            self.card_label.config(text=self.current_card['front'])
        self.showing_answer = not self.showing_answer

    def next_card(self):
        self.current_card = random.choice(self.flashcards)
        self.card_label.config(text=self.current_card['front'])
        self.showing_answer = False

    def load_cards(self):
        if os.path.exists(CARD_FILE):
            with open(CARD_FILE, "r") as f:
                return json.load(f)
        return []

    def save_cards(self):
        with open(CARD_FILE, "w") as f:
            json.dump(self.flashcards, f, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
