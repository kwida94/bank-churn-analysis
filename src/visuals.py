import matplotlib.pyplot as plt


def churn_distribution(df):
    churn_counts = df['Exited'].value_counts()
    churn_counts.plot(kind='bar', color=['skyblue', 'salmon'])
    plt.title('Churn Distribution')
    plt.xlabel('Exited')
    plt.ylabel('Count')
    plt.show()


def churn_by_geography(df):
    geography_churn = df.groupby('Geography')['Exited'].mean()
    geography_churn.plot(kind='bar', color='lightgreen')
    plt.title('Churn Rate by Geography')
    plt.xlabel('Geography')
    plt.ylabel('Churn Rate')
    plt.show()


def age_distribution(df):
    plt.hist(df['Age'], bins=20, color='orchid', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()
