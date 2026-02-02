from src.load_data import load_data
from src.cleaning import clean_data
from src.features import (
    create_age_group,
    create_balance_category,
    create_risk_level,
)
from src.visuals import (
    churn_distribution,
    churn_by_geography,
    age_distribution,
)


def main():
    print("Loading data...")
    df = load_data('data/Churn_Modeling.csv')
    print("Cleaning data...")
    df = clean_data(df)
    print("Creating features...")
    df = create_age_group(df)
    df = create_balance_category(df)
    df = create_risk_level(df)
    print('Running visualizations...')
    churn_distribution(df)
    churn_by_geography(df)
    age_distribution(df)
    print("Pipeline completed.")


if __name__ == "__main__":
    main()
