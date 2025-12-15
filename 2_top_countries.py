import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar', color='#E50914')
plt.title('Top 10 Countries on Netflix')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.savefig('chart_bar.png', bbox_inches='tight')
print(" Saved: chart_bar.png")
plt.show()