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

def plot_monthly_savings_rate(monthly):
    savings_rate = (monthly["savings"] / monthly["income"]) * 100

    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.bar(
        monthly.index.astype(str),
        monthly["savings"],
        width=0.65,
        alpha=0.7,
        color="steelblue",
        label="Savings (€)",
    )

    ax1.set_xlabel("Month")
    ax1.set_ylabel("Savings (€)")
    ax1.set_title("Monthly Savings and Savings Rate")

    ax2 = ax1.twinx()

    ax2.plot(
        monthly.index.astype(str),
        savings_rate,
        marker="o",
        linewidth=2.5,
        color="orange",
        label="Savings Rate (%)",
    )

    ax2.set_ylabel("Savings Rate (%)")
    ax2.set_ylim(0, 100)

    ax1.set_ylim(0, max(monthly["savings"]) * 1.2)

    ax1.grid(axis="y", linestyle="--", alpha=0.4)

    fig.legend(
        loc="upper right",
        bbox_to_anchor=(0.9, 0.9),
    )

    plt.xticks(rotation=45)
    fig.tight_layout()

    plt.savefig("output/monthly_savings_rate.png")
    plt.close()