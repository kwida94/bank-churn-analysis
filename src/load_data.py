import pandas as pd


def load_data(path):
    """Load data from a CSV file into a pandas DataFrame."""

    df = pd.read_csv(path)
    return df
