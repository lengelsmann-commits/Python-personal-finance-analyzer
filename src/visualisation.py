import matplotlib.pyplot as plt

def plot_monthly_income_expenses(monthly):
    ax = monthly.plot(
        y=["income", "expenses"],
        kind="line",
        marker="o",
    )

    ax.set_title("Monthly Income vs Expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (€)")

    ax.set_ylim(1000, 4000)
    ax.set_yticks(range(1000, 4001, 250))

    plt.xticks(rotation=45)
    plt.legend(["Income", "Expenses"])
    plt.tight_layout()

    plt.savefig("output/monthly_income_expenses.png")
    plt.close()

def plot_spending_by_category(category_spending):
    category_spending = category_spending.sort_values()

    ax = category_spending.plot(
        kind="barh",
        figsize=(8, 5),
    )

    ax.set_title("Spending by Category")
    ax.set_xlabel("Amount (€)")
    ax.set_ylabel("")

    ax.set_xlim(0, 2500)
    ax.set_xticks(range(0, 2501, 250))
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    plt.tight_layout()

    plt.savefig("output/spending_by_category.png")
    plt.close()