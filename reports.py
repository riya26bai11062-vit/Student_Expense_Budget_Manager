from expense_manager import expenses
from budget_manager import budget


def monthly_summary():
    print("\n----- Monthly Summary -----")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    remaining = budget - total

    print("Total Expenses: ₹", total)
    print("Monthly Budget: ₹", budget)
    print("Remaining Budget: ₹", remaining)

    print("\nCategory-wise Spending:")

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    for category in categories:
        print(category, ": ₹", categories[category])

    highest_category = max(categories, key=categories.get)

    print("\nHighest Spending Category:", highest_category)
    print("Amount Spent: ₹", categories[highest_category])