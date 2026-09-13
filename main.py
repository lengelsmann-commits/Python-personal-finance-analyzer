from src.data_loader import load_transactions
from src.analysis import (
    spending_by_category,
    monthly_summary,
    spending_by_category_monthly,
    fixed_vs_variable_spending,
)
from src.visualisation import (
    plot_monthly_income_expenses,
    plot_spending_by_category,
    plot_monthly_savings_rate,
    plot_income_expenses_savings,
    plot_spending_evolution,
    plot_fixed_vs_variable_spending,
)


transactions = load_transactions("data/transactions.csv")

monthly = monthly_summary(transactions)

plot_monthly_income_expenses(monthly)

category_spending = spending_by_category(transactions)
plot_spending_by_category(category_spending)

plot_monthly_savings_rate(monthly)

plot_income_expenses_savings(monthly)

monthly_category = spending_by_category_monthly(transactions)
plot_spending_evolution(monthly_category)

fixed_variable = fixed_vs_variable_spending(transactions)
plot_fixed_vs_variable_spending(fixed_variable)