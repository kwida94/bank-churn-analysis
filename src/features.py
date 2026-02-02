import numpy as np


def create_age_group(df):
    df['AgeGroup'] = np.where(
        df['Age'] <= 30,
        'Young',
        np.where(df['Age'] <= 50, 'Adult', 'Senior')
    )
    return df


def create_balance_category(df):
    df['BalanceCategory'] = np.where(
        df['Balance'] == 0,
        'No Balance',
        np.where(
            (df['Balance'] > 0) & (df['Balance'] <= 50000),
            'Low Balance',
            np.where(
                (df['Balance'] > 50000) & (df['Balance'] <= 100000),
                'Medium Balance',
                'High Balance'
            )
        )
    )
    return df


def create_risk_level(df):
    df['RiskLevel'] = np.where(
        (df['CreditScore'] < 600) & (
            df['IsActiveMember'] == 0) & (df['Balance'] > 100000),
        'High Risk',
        np.where(
            (df['CreditScore'] < 700) | (df['IsActiveMember'] == 0),
            'Medium Risk',
            'Low Risk'
        )
    )
    return df
