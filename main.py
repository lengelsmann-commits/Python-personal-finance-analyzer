from src.data_loader import load_transactions
from src.analysis import spending_by_category, monthly_summary
from src.visualisation import (
    plot_monthly_income_expenses,
    plot_spending_by_category,
    plot_monthly_savings_rate,
    plot_income_expenses_savings,
)


transactions = load_transactions("data/transactions.csv")

monthly = monthly_summary(transactions)

plot_monthly_income_expenses(monthly)

category_spending = spending_by_category(transactions)
plot_spending_by_category(category_spending)

plot_monthly_savings_rate(monthly)

plot_income_expenses_savings(monthly)