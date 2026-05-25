"""Mini Budget Tracker

This command-line program uses Python fundamentals to track expenses,
calculate totals, and warn when spending approaches a budget limit.

Concepts included:
- Variables and numeric types
- Strings for prompts and formatted output
- Lists to store expense records
- Dictionaries to summarize totals by category
- Tuples for fixed category options
- Sets to deduplicate tags
- Conditionals to detect over-budget and low-budget warnings
- Loops to gather repeated input
- Functions to structure program logic 
"""

from collections import defaultdict
from typing import Dict, List, Set, Tuple

ExpenseEntry = Dict[str, object]
CategoryTotals = Dict[str, float]

DEFAULT_CATEGORIES: Tuple[str, ...] = (
    "Food",
    "Transport",
    "Bills",
    "Entertainment",
    "Health",
    "Other",
)


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("That is not a valid number. Try again.")


def collect_expense(categories: Tuple[str, ...]) -> ExpenseEntry:
    print("\nEnter a new expense. Leave the description blank to finish.")
    description = input("Description: ").strip()
    if not description:
        return {}

    print("Available categories:")
    print(", ".join(categories))
    category = input("Category: ").strip().title()
    if category not in categories:
        print(f"Category '{category}' not recognized; saving as 'Other'.")
        category = "Other"

    amount = get_positive_float("Amount spent: ")
    raw_tags = input("Tags (comma-separated, optional): ").strip()
    tags: Set[str] = {
        tag.strip().lower() for tag in raw_tags.split(",") if tag.strip()
    }

    return {
        "description": description,
        "category": category,
        "amount": amount,
        "tags": tags,
    }


def summarize_expenses(expenses: List[ExpenseEntry]) -> Tuple[CategoryTotals, float, int]:
    totals: CategoryTotals = defaultdict(float)
    total_amount = 0.0

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        totals[category] += amount
        total_amount += amount

    average = total_amount / len(expenses) if expenses else 0.0
    return totals, total_amount, int(average) if expenses else 0


def display_summary(expenses: List[ExpenseEntry], budget: float) -> None:
    totals, total_amount, average_amount = summarize_expenses(expenses)

    print("\n=== Expense Summary ===")
    print(f"Budget target: ${budget:.2f}")
    print(f"Total spent:   ${total_amount:.2f}")
    print(f"Average expense amount: ${average_amount:.2f}")

    if not expenses:
        print("No expenses recorded.")
        return

    for category, amount in sorted(totals.items()):
        print(f"- {category}: ${amount:.2f}")

    if total_amount > budget:
        print("WARNING: You have exceeded your budget.")
    elif total_amount >= budget * 0.8:
        print("Notice: Spending is at or above 80% of the budget.")
    else:
        print("Good job! You are below your budget.")

    unique_tags = sorted({tag for expense in expenses for tag in expense["tags"]})
    if unique_tags:
        print(f"Tags used: {', '.join(unique_tags)}")


def run_budget_tracker() -> None:
    print("Welcome to the Mini Budget Tracker")
    print("This tool uses lists, dictionaries, loops, and conditionals.")
    budget = get_positive_float("Enter your budget amount: ")

    expenses: List[ExpenseEntry] = []
    while True:
        expense = collect_expense(DEFAULT_CATEGORIES)
        if not expense:
            break
        expenses.append(expense)
        print(f"Added expense: {expense['description']} (${expense['amount']:.2f})")

    display_summary(expenses, budget)
    print("Thank you for using the budget tracker.")


def main() -> None:
    run_budget_tracker()


if __name__ == "__main__":
    main()
