import pandas as pd


def load_transactions(filepath):
    """Load and prepare transaction data."""
    df = pd.read_csv(filepath)

    df["date"] = pd.to_datetime(df["date"])

    return df