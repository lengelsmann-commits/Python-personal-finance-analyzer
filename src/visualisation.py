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