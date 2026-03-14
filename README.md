# Bank Customer Churn Analysis

## Project Overview
This project analyzes customer churn patterns in a retail banking dataset using Python. The goal is to identify high-risk customer segments, behavioral trends, and key factors associated with customer attrition.

## Business Problem
Customer churn directly impacts revenue and growth. Understanding which customers are likely to leave allows banks to:
- Improve retention strategies
- Target high-risk customers
- Reduce revenue loss
- Optimize customer engagement

## Dataset
Churn_Modelling.csv  
Contains demographic, financial, and behavioral customer data including:
- Geography
- Gender
- Age
- Credit score
- Balance
- Activity status
- Churn label (Exited)

## Tools Used
- Python
- pandas
- numpy
- matplotlib
- Git
- GitHub

## Data Processing
- Column cleaning
- Duplicate handling
- Data filtering
- Feature engineering

## Feature Engineering
- **AgeGroup**: Young, Adult, Senior
- **BalanceCategory**: No Balance, Low, Medium, High
- **RiskLevel**: Low Risk, Medium Risk, High Risk

## Analysis Questions
- Which customers are most likely to churn?
- How does geography affect churn?
- Does activity level influence churn?
- What balance levels are most associated with churn?
- Which risk segments show highest churn rates?

## Visualizations
- Churn distribution
- Churn by geography
- Age distribution
- Balance distribution
- Activity vs churn
- Risk category vs churn

## Key Insights
- Overall churn rate was 20.4% which roughly 1 in 5 Customers left.
- Customers in Germany had a churn rate of 32.4% which was almost double Spain (16.7%) and France (16.2%).
- Inactive members were significantly more likely to churn.
- Customers with high balances and low credit scores were frequently in the high-risk churn group.

## Future Improvements
- Add machine learning churn prediction model
- build an interactive dashboard with Tableau or Power BI
