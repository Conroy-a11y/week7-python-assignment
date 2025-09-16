import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# 1. Compute basic statistics
print("Basic statistics of numerical columns:")
print(df.describe())

# 2. Grouping: Mean measurements per species
grouped = df.groupby("species").mean(numeric_only=True)
print("\nMean values of numerical columns grouped by species:")
print(grouped)

# 3. Identify patterns / interesting findings
print("\nObservations:")
for col in grouped.columns:
    print(f"- {col}:")
    print(grouped[col])
    print()