from expense_manager import expenses
from validation import get_positive_number
from storage import save_budget, load_budget

budget = load_budget()


def set_budget():
    global budget

    print("\n----- Set Monthly Budget -----")

    budget = get_positive_number("Enter your monthly budget: ₹")
    save_budget(budget)

    print("Monthly budget set successfully!")


def view_budget():
    print("\n----- Budget Details -----")

    if budget == 0:
        print("No budget has been set yet.")
        return

    print("Monthly Budget: ₹", budget)


def budget_status():
    print("\n----- Budget Status -----")

    if budget == 0:
        print("No budget has been set yet.")
        return

    total_spent = 0

    for expense in expenses:
        total_spent = total_spent + expense["amount"]

    remaining = budget - total_spent

    print("Monthly Budget: ₹", budget)
    print("Total Spent: ₹", total_spent)
    print("Remaining Budget: ₹", remaining)

    if remaining > 0:
        print("You are within your budget.")

    elif remaining == 0:
        print("You have reached your budget.")

    else:
        print("You have exceeded your budget.")