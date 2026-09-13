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

def monthly_summary(df):
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M")

    monthly = df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)

    monthly["expenses"] = monthly.get("expense", 0).abs()
    monthly["income"] = monthly.get("income", 0)
    monthly["savings"] = monthly["income"] - monthly["expenses"]

    return monthly[["income", "expenses", "savings"]]

def spending_by_category_monthly(df):
    expenses = df[df["type"] == "expense"].copy()

    expenses["month"] = expenses["date"].dt.to_period("M")

    monthly = (
        expenses.groupby(["month", "category"])["amount"]
        .sum()
        .abs()
        .unstack(fill_value=0)
    )

    return monthly