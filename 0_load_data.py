import pandas as pd

url = "https://raw.githubusercontent.com/SahilChachra/Netflix-Data-Visualization/master/netflix_titles.csv"
print("Downloading data...")
df = pd.read_csv(url)
df.to_csv('netflix_titles.csv', index=False)
print("✅ Data downloaded successfully!")