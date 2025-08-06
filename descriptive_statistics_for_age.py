# descriptive_statistics_for_age.py

# Import necessary libraries
import pandas as pd
import os

# --- 1. Load Data ---
print("="*50)
print("LOADING DATA FOR DESCRIPTIVE STATISTICS")
print("="*50)

# Define the path to the data file (relative to the script location)
file_path = os.path.join('..', 'data', 'oscar_age_male.csv')

try:
    # Load the data with skipinitialspace to handle column names correctly
    df = pd.read_csv(file_path, skipinitialspace=True)
    print(f"Data loaded successfully from {file_path}!")
    print(f"Dataset shape: {df.shape}")

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
    print("Please make sure the file 'oscar_age_male.csv' exists in the '../data' folder.")
    exit() # Stop the script if data can't be loaded
except Exception as e:
    print(f"An unexpected error occurred while loading data: {e}")
    exit()

# --- 2. Calculate and Display Descriptive Statistics for Age ---
print("\n" + "="*50)
print("DESCRIPTIVE STATISTICS FOR AGE")
print("="*50)

try:
    # Check if 'Age' column exists
    if 'Age' not in df.columns:
        raise KeyError("Column 'Age' not found in the dataset. Please check the column names.")

    # Calculate key statistics for Age
    mean_age = df['Age'].mean()
    median_age = df['Age'].median()
    # Mode can return multiple values, take the first one
    mode_age_series = df['Age'].mode()
    mode_age = mode_age_series.iloc[0] if not mode_age_series.empty else "No Mode"
    std_age = df['Age'].std()
    min_age = df['Age'].min()
    max_age = df['Age'].max()

    # Find the names of the youngest and oldest winners
    youngest_winner_name = df[df['Age'] == min_age]['Name'].iloc[0]
    oldest_winner_name = df[df['Age'] == max_age]['Name'].iloc[0]
    youngest_winner_movie = df[df['Age'] == min_age]['Movie'].iloc[0]
    oldest_winner_movie = df[df['Age'] == max_age]['Movie'].iloc[0]

    # Print the results
    print(f"Mean Age: {mean_age:.2f} years")
    print(f"Median Age: {median_age:.2f} years")
    print(f"Mode Age: {mode_age} years")
    print(f"Standard Deviation: {std_age:.2f} years")
    print("-" * 30)
    print(f"Youngest Winner: {youngest_winner_name} ({min_age} years old) - Movie(s): {youngest_winner_movie}")
    print(f"Oldest Winner: {oldest_winner_name} ({max_age} years old) - Movie(s): {oldest_winner_movie}")

except KeyError as e:
    print(f"Error: {e}")
    exit()
except Exception as e:
    print(f"An error occurred during descriptive statistics calculation: {e}")
    exit()

print("\nDescriptive statistics calculation complete.")
