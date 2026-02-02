def clean_data(df):
    """Clean the input DataFrame by handling missing values and duplicates."""

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Drop non-analytical columns
    df = df.drop(columns=['RowNumber', 'CustomerId',
                 'Surname'], errors='ignore')

    return df
