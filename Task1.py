import pandas as pd

# Step 1: Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Explore the structure
print("\nDataset Information:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())


df = df.dropna()  # drop rows with missing values

print("\nAfter cleaning, missing values:")
print(df.isnull().sum())