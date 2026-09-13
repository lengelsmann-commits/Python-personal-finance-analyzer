from src.data_loader import load_transactions
from src.analysis import (
    calculate_income,
    calculate_expenses,
    calculate_savings,
    calculate_savings_rate,
    spending_by_category,
    monthly_summary,
)
from src.visualisation import plot_monthly_income_expenses


transactions = load_transactions("data/transactions.csv")

monthly = monthly_summary(transactions)

plot_monthly_income_expenses(monthly)