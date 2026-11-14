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
