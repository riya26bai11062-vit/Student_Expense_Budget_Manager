from reports import monthly_summary
from expense_manager import (
    add_expense,
    view_expenses,
    search_expense,
    update_expense,
    delete_expense
)
from budget_manager import (
    set_budget,
    view_budget,
    budget_status
)
from analytics import (
    total_spending,
    category_wise_spending,
    highest_spending_category,
    average_daily_spending
)


def main():
    print("======================================")
    print("   STUDENT EXPENSE & BUDGET MANAGER")
    print("======================================")

    while True:
        print("\nMain Menu")
        print("1. Expense Management")
        print("2. Budget Management")
        print("3. Analytics & Reports")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\n----- Expense Management -----")
                print("1. Add Expense")
                print("2. View Expenses")
                print("3. Search Expense")
                print("4. Update Expense")
                print("5. Delete Expense")
                print("6. Back to Main Menu")

                expense_choice = input("Enter your choice: ")

                if expense_choice == "1":
                    add_expense()

                elif expense_choice == "2":
                    view_expenses()

                elif expense_choice == "3":
                    search_expense()

                elif expense_choice == "4":
                    update_expense()

                elif expense_choice == "5":
                    delete_expense()

                elif expense_choice == "6":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
             while True:
                 print("\n----- Budget Management -----")
                 print("1. Set Monthly Budget")
                 print("2. View Budget")
                 print("3. Budget Status")
                 print("4. Back to Main Menu")

                 budget_choice = input("Enter your choice: ")

                 if budget_choice == "1":
                     set_budget()

                 elif budget_choice == "2":
                    view_budget()

                 elif budget_choice == "3":
                    budget_status()

                 elif budget_choice == "4":
                    break

                 else:
                     print("Invalid choice. Please try again.")

        elif choice == "3":
             while True:
                 print("\n----- Analytics & Reports -----")
                 print("1. Total Spending")
                 print("2. Category-wise Spending")
                 print("3. Highest Spending Category")
                 print("4. Average Daily Spending")
                 print("5. Monthly Summary")
                 print("6. Back to Main Menu")
                 analytics_choice = input("Enter your choice: ")

                 if analytics_choice == "1":
                     total_spending()

                 elif analytics_choice == "2":
                     category_wise_spending()

                 elif analytics_choice == "3":
                     highest_spending_category()

                 elif analytics_choice == "4":
                     average_daily_spending()

                 elif analytics_choice == "5":
                     monthly_summary()

                 elif analytics_choice == "6":
                     break

                 else:
                     print("Invalid choice. Please try again.")

        elif choice == "4":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()