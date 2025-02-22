import pandas as pd

# Load the dataset
df = pd.read_csv("train.csv")

# Display first few rows
print(df.head())

# Check column names
print("\nColumns:", df.columns)

# Check the number of categories
print("\nUnique Categories:", df["Category"].nunique())

# Display the top 10 categories
print("\nTop 10 Categories:")
print(df["Category"].value_counts().all )

