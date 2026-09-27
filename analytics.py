from expense_manager import expenses


def total_spending():
    print("\n----- Total Spending -----")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Spending: ₹", total)


def category_wise_spending():
    print("\n----- Category-wise Spending -----")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

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


def highest_spending_category():
    print("\n----- Highest Spending Category -----")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    highest_category = max(categories, key=categories.get)

    print("Highest Spending Category:", highest_category)
    print("Amount Spent: ₹", categories[highest_category])


def average_daily_spending():
    print("\n----- Average Daily Spending -----")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    total = 0
    dates = []

    for expense in expenses:
        total = total + expense["amount"]

        if expense["date"] not in dates:
            dates.append(expense["date"])

    average = total / len(dates)

    print("Total Spending: ₹", total)
    print("Number of Days:", len(dates))
    print("Average Daily Spending: ₹", average)
    print("5. Monthly Summary")
    print("6. Back to Main Menu")
    
