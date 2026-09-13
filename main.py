from src.data_loader import load_transactions
from src.analysis import (
    calculate_income,
    calculate_expenses,
    calculate_savings,
    calculate_savings_rate,
    spending_by_category,
)

transactions = load_transactions("data/transactions.csv")

income = calculate_income(transactions)
expenses = calculate_expenses(transactions)
savings = calculate_savings(transactions)
savings_rate = calculate_savings_rate(transactions)

print(f"Total income: €{income:.2f}")
print(f"Total expenses: €{expenses:.2f}")
print(f"Total savings: €{savings:.2f}")
print(f"Savings rate: {savings_rate:.2f}%")
print("\nSpending by category:")

category_spending = spending_by_category(transactions)

print(category_spending)