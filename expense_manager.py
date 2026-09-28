from validation import get_positive_number, get_valid_id
from storage import save_expenses, load_expenses

expenses = load_expenses()


def add_expense():
    print("\n----- Add Expense -----")

    date = input("Enter date: ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = get_positive_number("Enter amount: ")

    expense = {
        "id": len(expenses) + 1,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses():
    print("\n----- All Expenses -----")

    if not expenses:
        print("No expenses recorded yet.")
        return
    for expense in expenses:
        print("\nExpense ID:", expense["id"])
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("Amount: ₹", expense["amount"])


def search_expense():
    print("\n----- Search Expense -----")

    expense_id = get_valid_id("Enter Expense ID: ")

    for expense in expenses:
        if expense["id"] == expense_id:
            print("\nExpense Found!")
            print("Expense ID:", expense["id"])
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Amount: ₹", expense["amount"])
            return

    print("Expense not found.")


def update_expense():
    print("\n----- Update Expense -----")

    expense_id = get_valid_id("Enter Expense ID: ")

    for expense in expenses:
        if expense["id"] == expense_id:

            print("\nCurrent Expense Details:")
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Amount: ₹", expense["amount"])

            expense["category"] = input("Enter new category: ")
            expense["description"] = input("Enter new description: ")
            expense["amount"] = get_positive_number("Enter new amount: ")

            save_expenses(expenses)

            print("Expense updated successfully!")

    print("Expense not found.")


def delete_expense():
    print("\n----- Delete Expense -----")

    expense_id = get_valid_id("Enter Expense ID: ")

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            print("Expense deleted successfully!")
            return

    print("Expense not found.")