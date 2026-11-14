# CDS4003 - Hotel Booking Cancellation Prediction
# Student 1 - Data Understanding

import pandas as pd

# Load hotel booking dataset
df = pd.read_csv("data/hotel_bookings.csv")

# Display first five records
print("First Five Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display dataset dimensions
print("\nDataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())


# =====================================
# 3.2 Missing Values Analysis
# =====================================

print("\nMissing Values Analysis:")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])

# Calculate missing values percentage
missing_percentage = (df.isnull().sum() / len(df)) * 100

print("\nMissing Values Percentage:")
print(missing_percentage[missing_percentage > 0])


# =====================================
# 3.3 Duplicate Records
# =====================================

print("\nDuplicate Records Analysis:")

duplicate_count = df.duplicated().sum()

print("Number of duplicate records:", duplicate_count)

