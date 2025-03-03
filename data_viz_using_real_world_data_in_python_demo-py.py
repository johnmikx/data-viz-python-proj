# -*- coding: utf-8 -*-
"""Data Visualization Using Real World Data in Python (Demonstration).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10uPMUaquZpgXZ5zWGuekvuKK4HWyQtfG

##**Data Visualization Using Real World Data**
**Instructions:**
1. `Download the CSV file containing IMDB Movies data.`
2. `Clean the data, visualize and print the top 3 most popular movies of all time.`
3. `Categorize each movies using Bar Plots.`
4. `Compare and contrast the Movie Budget and Revenue using Scatter Plot.`
5. `Visualize the top movie production country using Pie Charts.`
6. `Additional Visualizations: Pairplot for Budget, Revenue, and Popularity`
"""

# Install matplotlib and seaborn on Google Colab
!pip install matplotlib
!pip install seaborn

# Install locally
# pip install matplotlib
# pip install seaborn

# Imports
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np

"""### **1. Download the CSV file containing IMDB Movies data.**"""

import gdown

# Convert the Google Drive "view" link to a "download" link
file_id = "1pJg8JRwmb4O5uo-diBgIWroHK9NtIQVk"
download_url = f"https://drive.google.com/uc?id={file_id}"

# Download the file
output = "data.csv"  # You can name it whatever you want
gdown.download(download_url, output, quiet=False)

# Read the CSV file
df = pd.read_csv(output)
df.head()

"""### **2. Clean the data, visualize and print the top 3 most popular movies of all time.**"""

df.info()
df.columns

df.columns = df.columns.str.strip()

df.info()
df.columns

# Convert 'Release Date' to datetime format
df['Release Date'] = pd.to_datetime(df['Release Date'], format="%m/%d/%Y", errors='coerce')

# Sort the DataFrame by 'Release Date' in ascending order
df = df.sort_values(by='Release Date')

# Generate Plot
plt.plot(df['Release Date'], df['Popularity'])

plt.show()

# Create the Line Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Release Date'], df['Popularity'], marker = 'o', linestyle = '-')

# Labels and Title
plt.xlabel('Release Date')
plt.ylabel('Popularity')
plt.grid()
plt.title('Popularity Over Time')

# Show the Plot
plt.show()

# Filter movies with popularity greater than 2000
popular_movies = df[df['Popularity'] > 2000]

# Print only the movie titles
print(popular_movies[['title', 'Popularity']])

"""### **3. Categorize each movies using Bar Plots.**"""

print(df['genres'].value_counts())

# Split genres by comma and expand into separate rows
df_exploded = df.assign(genres=df['genres'].str.split(', ')).explode('genres')

# Count occurrences of each individual genre
genre_counts = df_exploded['genres'].value_counts()

print(genre_counts)

genre_counts.plot(kind = 'bar')
plt.show()

# Resize
plt.figure(figsize=(12, 6))
genre_counts.plot(kind='bar', color = 'skyblue', edgecolor = 'black')

# x and y axis labels
plt.xlabel("Genres")
plt.ylabel("Count")

# Add a title
plt.title("Movie Genre Distribution")

# Other edits
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the Plot
plt.show()

"""### **4. Compare and contrast the Movie Budget and Revenue using Scatter Plot.**"""

df.head()

# Remove characters
df['bUDget'] = df['bUDget'].str.replace('[$,]', '', regex=True).str.strip()
df['REVENUE'] = df['REVENUE'].str.replace('[$,]', '', regex=True).str.strip()

# Convert to numeric
df['bUDget'] = pd.to_numeric(df['bUDget'], errors='coerce')
df['REVENUE'] = pd.to_numeric(df['REVENUE'], errors='coerce')
df.dropna(subset=['bUDget', 'REVENUE'], inplace=True)

#MINIMUM
print('$',np.min(df['bUDget']))
print('$',np.min(df['REVENUE']))

#MAXIMUM
print('$',np.max(df['bUDget']))
print('$',np.max(df['REVENUE']))

#AVERAGE
print('$',np.mean(df['bUDget']))
print('$',np.mean(df['REVENUE']))

# Create scatter plot
plt.scatter(df['bUDget'], df['REVENUE'])

# Labels and title
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.title("Budget vs Revenue Scatter Plot")

# Show plot
plt.show()

import matplotlib.ticker as mtick  # Import ticker module for formatting

# Create figure
plt.figure(figsize=(10, 6))

# Scatter plot
scatter = plt.scatter(
    df['bUDget'], df['REVENUE'],
    c=df['REVENUE'], cmap='coolwarm',
    s=50, alpha=0.7, edgecolors='black'
)

# Add color bar
cbar = plt.colorbar(scatter)
cbar.set_label("Revenue ($)", fontsize=12)

# Labels and title
plt.xlabel("Budget ($)")
plt.ylabel("Revenue ($)")
plt.title("Budget vs Revenue Scatter Plot")

# Format y-axis and x-axis to display in billions (B)
formatter = mtick.FuncFormatter(lambda x, _: f'{x/1e9:1.1f}B')  # Convert to B
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_major_formatter(formatter)

# Improve readability
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()

"""### **5. Visualize the top movie production country using Pie Charts.**"""

print(df['production_countries'].value_counts())

countries_exploded = df.assign(country=df['production_countries'].str.split(', ')).explode('country')

countries_exploded = countries_exploded.dropna(subset=['country'])

# Count occurrences of each individual country
country_counts = countries_exploded['country'].value_counts()

# Rename countries with less than 200 occurrences to "Others"
countries_exploded['country'] = countries_exploded['country'].apply(lambda x: x if country_counts[x] >= 200 else 'Others')

# Recount after renaming
final_country_counts = countries_exploded['country'].value_counts()

print(final_country_counts)

# Resize figure
plt.figure(figsize=(8, 8))

# Create pie chart
plt.pie(final_country_counts, labels = final_country_counts.index, autopct = '%1.1f%%', startangle = 140, colors = plt.cm.Paired.colors)

# Add title
plt.title("Movie Producer Country")

# Show plot
plt.show()

# Resize figure
plt.figure(figsize=(8, 8))

# Find the largest country count to explode it
explode = [0.1 if count == final_country_counts.max() else 0 for count in final_country_counts.values]

# Create pie chart
plt.pie(final_country_counts, labels=final_country_counts.index,
        autopct='%1.1f%%', startangle=140,
        colors=plt.cm.Paired.colors,
        explode=explode, shadow=True,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})

# Add title
plt.title("Movie Producer Country", fontsize=14, fontweight="bold")

# Improve layout
plt.tight_layout()

# Show plot
plt.show()

"""### **6. Additional Visualizations: Pairplot for Budget, Revenue, and Popularity**"""

# Pairplot: Budget, Revenue, and Popularity
plt.figure(figsize=(10, 10))
sns.pairplot(df[['bUDget', 'REVENUE', 'Popularity']], diag_kind="kde", plot_kws={'alpha': 0.6, 's': 50, 'edgecolor': "k"})

# Add title
plt.suptitle("Pairplot: Budget, Revenue, and Popularity", y=1.02, fontsize=14, fontweight="bold")

# Show plot
plt.show()