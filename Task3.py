import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# --- 1. Line chart (simulated time series) ---
# Let's pretend each row = a day of flower measurement (just for trend demo)
df["day"] = range(1, len(df) + 1)
plt.figure(figsize=(8, 4))
plt.plot(df["day"], df["sepal_length"], label="Sepal Length", color="blue")
plt.plot(df["day"], df["petal_length"], label="Petal Length", color="green")
plt.title("Line Chart: Sepal vs Petal Length Over Time")
plt.xlabel("Day")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# --- 2. Bar chart: average petal length per species ---
plt.figure(figsize=(6, 4))
sns.barplot(x="species", y="petal_length", data=df, estimator="mean", palette="viridis")
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# --- 3. Histogram: distribution of sepal length ---
plt.figure(figsize=(6, 4))
plt.hist(df["sepal_length"], bins=20, color="orange", edgecolor="black", alpha=0.7)
plt.title("Histogram: Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# --- 4. Scatter plot: sepal length vs petal length ---
plt.figure(figsize=(6, 4))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()