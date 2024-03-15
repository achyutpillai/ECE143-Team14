import pandas as pd   #importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/lifeExpectancy/_life.csv")
#print(df)

# Select only the numeric columns
numeric_columns = df.select_dtypes(include='number')

# Round the numeric columns to integers
rounded_numeric_columns = numeric_columns.round().astype(int)

# Combine the rounded numeric columns with the non-numeric columns
rounded_df = pd.concat([df.drop(columns=numeric_columns.columns), rounded_numeric_columns], axis=1)

# Pivot the DataFrame for the heatmap
heatmap_data  = rounded_df.pivot_table(index='continents', columns='Happiness score', values='Healthy life expectancy')
heatmap_data_filled = heatmap_data.bfill(axis=1)
heatmap_data_filled = heatmap_data_filled.reindex(columns=heatmap_data.columns[::-1])

# Plotting the heatmap for Happiness Score
plt.figure(figsize=(25, 5))
plt.style.use('ggplot')
plt.subplot(1, 2, 1)
sns.heatmap(heatmap_data_filled.T,  annot=False,  fmt='.1f',cmap="crest", cbar_kws={'label': 'Healthy life expectancy'},linewidth=.5)
plt.tight_layout()
plt.show()