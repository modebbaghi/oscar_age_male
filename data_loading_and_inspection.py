# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. Data Loading and Inspection ---
print("="*50)
print("1. DATA LOADING AND INSPECTION")
print("="*50)

# Define the path to the data file (relative to the script location)
# Looks one directory up (..) then into 'data'
file_path = os.path.join('..', 'data', 'oscar_age_male.csv')

try:
    # Load the data
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully from {file_path}!")
    print(f"Dataset shape: {df.shape} (Rows, Columns)\n")

    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\n")

    # Display basic information about the DataFrame
    print("Dataset Info:")
    print(df.info())
    print("\n")

    # Display basic statistics for numerical columns
    print("Basic Statistics for numerical columns:")
    print(df.describe())
    print("\n")

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
    print("Please make sure the file 'oscar_age_male.csv' exists in the '../data' folder relative to this script.")
    exit()
except pd.errors.ParserError as e:
    print(f"Error parsing the CSV file: {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while loading data: {e}")
    exit()
