import csv
import os

# File to store expenses
FILE_NAME = "expenses.csv"

# Ensure the file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    """Function to add a new expense"""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter expense category (Food, Transport, Shopping, etc.): ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print(" Expense added successfully!\n")

def view_expenses():
    """Function to display all expenses"""
    print("\n Your Expenses:\n")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)

        if len(data) <= 1:
            print("No expenses recorded yet.")
            return

        for row in data:
            print(f"{row[0]:<12} | {row[1]:<15} | ${row[2]:<8}")

def get_total_expenses():
    
    total = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[2])

    print(f"\n Total Expenses: ${total:.2f}\n")

def main():
    while True:
        print("\n Expense Tracker CLI")
        print("1️ Add Expense")
        print("2️ View Expenses")
        print("3️ Show Total Expenses")
        print("4️ Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            get_total_expenses()
        elif choice == "4":
            print("🔚 Exiting... Have a great day!")
            break
        else:
            print(" Invalid choice! Try again.")


