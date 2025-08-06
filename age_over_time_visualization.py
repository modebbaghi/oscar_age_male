# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os # If you are using os.path.join for file paths

# Load the data
file_path = os.path.join('..', 'data', 'oscar_age_male.csv')
df = pd.read_csv(file_path, skipinitialspace=True) # Remember skipinitialspace

# Plot Age vs Year to see trends over time
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Year', y='Age', alpha=0.7, color='purple')
# Add a trend line
sns.regplot(data=df, x='Year', y='Age', scatter=False, color='orange', label='Trend Line')
plt.title('Age of Oscar Best Actor Winners Over Time (1928-2016)')
plt.xlabel('Year of Ceremony')
plt.ylabel('Winner\'s Age')
plt.legend()
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.show()

# Calculate correlation
correlation = df['Year'].corr(df['Age'])
print(f"\nCorrelation between Year and Age: {correlation:.4f}")
