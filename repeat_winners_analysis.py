# repeat_winners.py

# Import necessary libraries
import pandas as pd
import os

# --- 1. Load Data ---
print("="*50)
print("LOADING DATA FOR REPEAT WINNERS ANALYSIS")
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
    print(f"An unexpected error occurred while loading  {e}")
    exit()

# --- 2. Analyze Repeat Winners ---
print("\n" + "="*50)
print("REPEAT WINNERS ANALYSIS")
print("="*50)

try:
    # Check if 'Name' column exists
    if 'Name' not in df.columns:
        raise KeyError("Column 'Name' not found in the dataset. Please check the column names.")

    # Find actors who won multiple times
    winner_counts = df['Name'].value_counts()
    repeat_winners = winner_counts[winner_counts > 1]

    if not repeat_winners.empty:
        print("Actors Who Won Multiple Oscars for Best Actor:")
        print(repeat_winners)
        print("-" * 40)

        # Display details for repeat winners
        print("Details of Repeat Winners:")
        repeat_names = repeat_winners.index.tolist()
        # Filter the original dataframe for repeat winners and sort for better presentation
        df_repeats = df[df['Name'].isin(repeat_names)].sort_values(by=['Name', 'Year']).reset_index(drop=True)
        # Select relevant columns to display
        print(df_repeats[['Name', 'Year', 'Age', 'Movie']])
        
        # Optional: Highlight the actor with the most wins
        max_wins = repeat_winners.max()
        top_winners = repeat_winners[repeat_winners == max_wins].index.tolist()
        if len(top_winners) == 1:
            print(f"\n{top_winners[0]} has the most wins with {max_wins} Oscars.")
        else:
            print(f"\nActors tied for the most wins ({max_wins} Oscars): {', '.join(top_winners)}")

    else:
        print("No actors won the Best Actor Oscar more than once in this dataset.")

except KeyError as e:
    print(f"Error: {e}")
    exit()
except Exception as e:
    print(f"An error occurred during repeat winners analysis: {e}")
    exit()

print("\nRepeat winners analysis complete.")
