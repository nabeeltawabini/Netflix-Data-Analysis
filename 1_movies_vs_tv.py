import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('netflix_titles.csv')

# 2. Count Movies vs TV Shows
# We use value_counts() to count the occurrences in the 'type' column
counts = df['type'].value_counts()

# Print the numbers to the terminal for verification
print("--- Content Counts ---")
print(counts)

# 3. Create the Visualization (Pie Chart)
plt.figure(figsize=(6, 6))

# Plotting the pie chart
plt.pie(counts, 
        labels=counts.index, 
        autopct='%1.1f%%', 
        colors=['#E50914', '#564d4d'], # Netflix Red & Dark Grey
        startangle=90)

plt.title('Netflix Content Distribution: Movies vs. TV Shows')

# 4. Show the plot
plt.show()