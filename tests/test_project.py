import unittest
from storage import save_expenses, load_expenses


class TestExpenseStorage(unittest.TestCase):

    def test_save_and_load_expenses(self):
        test_expenses = [
            {
                "id": 1,
                "date": "24-09-2026",
                "category": "Food",
                "description": "Lunch",
                "amount": 150
            }
        ]

        save_expenses(test_expenses)

        loaded_expenses = load_expenses()

        self.assertEqual(loaded_expenses, test_expenses)


if __name__ == "__main__":
    unittest.main()