# CLAUDE.md — Bank Churn Analysis

This file provides guidance for AI assistants working in this repository.

## Project Overview

A Python-based exploratory data analysis (EDA) project that analyzes customer churn patterns in a retail banking dataset. The goal is to identify high-risk customer segments, behavioral trends, and key drivers of attrition.

- **Dataset:** `data/Churn_Modeling.csv` — 10,000 customer records with 14 columns
- **Target variable:** `Exited` (1 = churned, 0 = retained)
- **Overall churn rate:** ~20.4%

## Repository Structure

```
bank-churn-analysis/
├── data/
│   └── Churn_Modeling.csv       # Raw dataset (do not modify)
├── notebooks/
│   └── Banking project.ipynb    # Exploratory Jupyter notebook
├── src/
│   ├── load_data.py             # Data loading
│   ├── cleaning.py              # Data cleaning (drop dupes, remove PII columns)
│   ├── features.py              # Feature engineering (derived columns)
│   └── visuals.py               # Matplotlib visualizations
├── main.py                       # Pipeline entry point
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview and key findings
```

## Setup & Running

```bash
# Install dependencies
pip install -r requirements.txt

# Run the full pipeline
python main.py
```

Dependencies: `pandas`, `numpy`, `matplotlib` — no pinned versions.

## Pipeline Flow

`main.py` orchestrates four sequential steps:

1. **Load** — `load_data.py`: reads CSV into a pandas DataFrame
2. **Clean** — `cleaning.py`: drops duplicates and removes non-analytical columns (`RowNumber`, `CustomerId`, `Surname`)
3. **Feature engineering** — `features.py`: creates derived columns using `np.where()`:
   - `AgeGroup`: Young / Adult / Senior
   - `BalanceCategory`: No Balance / Low / Medium / High
   - `RiskLevel`: Low / Medium / High (combines CreditScore, IsActiveMember, Balance)
4. **Visualize** — `visuals.py`: generates matplotlib bar charts and histograms

## Code Conventions

- **Naming:** snake_case for functions and variables throughout
- **Docstrings:** every function has a brief docstring — keep this practice when adding new functions
- **No type hints** are used in the existing codebase
- **No classes** — the project uses plain functions organized by module
- **Hardcoded thresholds** for feature binning (age brackets, balance tiers) are defined inline in `src/features.py`
- **Error handling:** minimal; `df.drop(..., errors='ignore')` is used defensively in cleaning

## Data Columns

| Column | Type | Notes |
|---|---|---|
| RowNumber | int | Drop — not analytical |
| CustomerId | int | Drop — PII |
| Surname | str | Drop — PII |
| CreditScore | int | Feature |
| Geography | str | France / Germany / Spain |
| Gender | str | Male / Female |
| Age | int | Binned into AgeGroup |
| Tenure | int | Years as customer |
| Balance | float | Binned into BalanceCategory |
| NumOfProducts | int | 1–4 |
| HasCrCard | int | 0/1 |
| IsActiveMember | int | 0/1 |
| EstimatedSalary | float | Feature |
| Exited | int | **Target** — 0/1 |

## Key Findings (from README)

- Germany: 32.4% churn vs Spain 16.7% and France 16.2%
- Inactive members and low-balance customers show higher churn
- Senior customers churn more than younger segments

## No Tests / No CI

There is currently no test suite, no linting configuration, and no CI/CD pipeline. When adding tests, use `pytest` and place test files under a `tests/` directory.

## Development Branches

Active development happens on feature branches. The `main`/`master` branch holds stable code. Use descriptive branch names for new features or experiments.
