# Student Expense & Budget Manager

## 1. Project Overview

Student Expense & Budget Manager is a Python-based application designed to help college students manage their daily expenses and monthly budget.

The system allows users to record, view, search, update, and delete expenses. It also helps users set a monthly budget and analyze their spending.

## 2. Objectives

- Record and manage daily expenses.
- Set and monitor a monthly budget.
- Calculate total spending and remaining budget.
- Analyze spending based on categories.
- Generate a monthly summary report.
- Store expense and budget data permanently.

## 3. Main Features

### Expense Management
- Add expenses
- View all expenses
- Search expenses by ID
- Update expenses
- Delete expenses

### Budget Management
- Set monthly budget
- View current budget
- Check total spending
- Check remaining budget
- Check whether the budget has been exceeded

### Analytics & Reports
- Calculate total spending
- Calculate category-wise spending
- Find highest spending category
- Calculate average daily spending
- Generate monthly summary

## 4. Technologies Used

- Python
- JSON
- File Handling
- Python unittest

## 5. Project Structure

```text
Student_Expense_Budget_Manager/
├── main.py
├── expense_manager.py
├── budget_manager.py
├── analytics.py
├── reports.py
├── validation.py
├── storage.py
├── README.md
├── data/
│   ├── expenses.json
│   └── budget.json
└── tests/
    └── test_project.py