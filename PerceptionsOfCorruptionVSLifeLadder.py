import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Read the data
data = pd.read_csv('data/WHR/clean2023HappinessData.csv')
data_clean = data.dropna(subset=['Life Ladder', 'Perceptions of corruption'])




corr = round(data_clean['Perceptions of corruption'].corr(data_clean['Life Ladder']), 3)

# Fit the trend line on cleaned data
x = data_clean['Life Ladder']
y = data_clean['Perceptions of corruption']
m, b = np.polyfit(x, y, 1)

# Create x values for the trend line: from min to max of 'Life Ladder' in the cleaned data
x_trend = np.linspace(x.min(), x.max(), 100)
y_trend = m*x_trend + b



# Create the scatter plot
plt.figure(figsize=(12, 8))
for continent in data_clean['Continent'].unique():
    continent_data = data_clean[data_clean['Continent'] == continent]
    # Add the trend line and its label for the legend
    plt.scatter(continent_data['Life Ladder'], continent_data['Perceptions of corruption'], label=continent)

# Label axes, add title
plt.plot(x_trend, y_trend, color='black', linestyle='-', label='Overall Trendline')  # Dashed black trend line
plt.xlabel('Happiness')
plt.ylabel('Perceptions of Corruption')
plt.text(.85, .95, f'Correlation: {corr}', transform=plt.gca().transAxes, fontsize=9)
plt.legend()
plt.tight_layout()
plt.show()

