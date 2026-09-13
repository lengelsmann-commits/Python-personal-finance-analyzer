def calculate_income(df):
    return df[df["type"] == "income"]["amount"].sum()


def calculate_expenses(df):
    return abs(df[df["type"] == "expense"]["amount"].sum())


def calculate_savings(df):
    income = calculate_income(df)
    expenses = calculate_expenses(df)
    return income - expenses


def calculate_savings_rate(df):
    income = calculate_income(df)
    savings = calculate_savings(df)

    if income == 0:
        return 0

    return (savings / income) * 100

def spending_by_category(df):
    expenses = df[df["type"] == "expense"]

    return (
        expenses.groupby("category")["amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )