# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. Load Data (ensure this is at the top) ---
file_path = os.path.join('..', 'data', 'oscar_age_male.csv')
df = pd.read_csv(file_path, skipinitialspace=True) # Include skipinitialspace

# --- 2. Calculate Statistics Needed for Plotting (add this section) ---
# Calculate key statistics for Age
mean_age = df['Age'].mean()
median_age = df['Age'].median()
# Add any other stats you might need for this specific plot

# --- 3. Create Visualization (your existing plotting code) ---
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=15, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribution of Oscar Best Actor Winners\' Ages (1928-2016)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

# Add lines for mean and median (now mean_age and median_age are defined)
plt.axvline(mean_age, color='red', linestyle='--', linewidth=2, label=f'Mean ({mean_age:.2f})')
plt.axvline(median_age, color='green', linestyle='-.', linewidth=2, label=f'Median ({median_age:.2f})')

plt.legend()
plt.tight_layout()
plt.show()

print("Age distribution visualization complete.")
