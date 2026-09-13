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
    fig, ax = plt.subplots(figsize=(10, 8))

    wedges, texts, autotexts = ax.pie(
        category_spending,
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=1.15,
    )

    ax.set_title("Spending by Category")

    ax.legend(
        wedges,
        category_spending.index,
        title="Category",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
    )

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

def plot_income_expenses_savings(monthly):
    ax = monthly.plot(
        y=["income", "expenses", "savings"],
        kind="bar",
        figsize=(10, 6),
        width=0.75,
    )

    ax.set_title("Monthly Income, Expenses and Savings")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (€)")

    ax.grid(axis="y", linestyle="--", alpha=0.4)

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("output/income_expenses_savings.png")
    plt.close()

def plot_spending_evolution(monthly_category):
    ax = monthly_category.plot(
        kind="area",
        stacked=True,
        figsize=(10, 6),
        alpha=0.8,
    )

    ax.set_title("Spending Evolution by Category")
    ax.set_xlabel("Month")
    ax.set_ylabel("Spending (€)")

    ax.set_yticks(range(0, 2501, 250))
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.8,
        alpha=0.6,
    )

    plt.xticks(rotation=45)

    plt.legend(
        title="Category",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
    )

    plt.tight_layout()

    plt.savefig("output/spending_evolution.png")
    plt.close()

def plot_fixed_vs_variable_spending(monthly):
    ax = monthly.plot(
        kind="bar",
        stacked=False,
        figsize=(10, 6),
        width=0.75,
    )

    ax.set_title("Fixed vs Variable Spending")
    ax.set_xlabel("Month")
    ax.set_ylabel("Spending (€)")

    ax.set_yticks(range(0, 2501, 250))
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.8,
        alpha=0.6,
    )

    plt.xticks(rotation=45)

    plt.legend(
        title="Spending Type",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
    )

    plt.tight_layout()

    plt.savefig("output/fixed_vs_variable_spending.png")
    plt.close()