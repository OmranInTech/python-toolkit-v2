#expense 

import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    date TEXT
)
''')
conn.commit()

# Function to add an expense
def add_expense(amount, category, description, date):
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                   (amount, category, description, date))
    conn.commit()
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    print("\nID | Amount | Category | Description | Date")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]} | ${row[1]} | {row[2]} | {row[3]} | {row[4]}")
    print("\n")

# Function to delete an expense by ID
def delete_expense(expense_id):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    print("Expense deleted successfully!\n")

# Function to view total expenses
def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print(f"Total Expenses: ${total if total else 0.0}\n")

# Main menu
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. View Total Expenses")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food, Travel, Rent, etc.): ")
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(amount, category, description, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
        elif choice == "4":
            total_expense()
        elif choice == "5":
            print("Exiting...\n")
            conn.close()
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
