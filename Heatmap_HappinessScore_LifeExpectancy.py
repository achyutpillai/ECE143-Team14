#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\riyaj\Downloads\__life.csv")

# Predict missing values using Linear Regression
predicted_values = []
for continent, group in df.groupby('Continent'):
    X_train = group[['Year']]
    y_train = group[['Healthy life expectancy', 'Happiness score']]
    X_predict = pd.DataFrame({'Year': range(2014, 2024)})
   
    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
   
    # Predict missing values
    predictions = model.predict(X_predict)
   
    # Create DataFrame of predictions
    predicted_df = pd.DataFrame({
        'Continent': [continent] * len(X_predict),
        'Year': range(2014, 2024),
        'Healthy life expectancy': predictions[:, 0],
        'Happiness score': predictions[:, 1]
    })
   
    predicted_values.append(predicted_df)

# Concatenate predictions for all continents
predicted_df = pd.concat(predicted_values, ignore_index=True)

pivot_predicted_df = predicted_df.pivot_table(index='Year', columns='Continent', values=['Healthy life expectancy', 'Happiness score'])

#print(pivot_predicted_df)

# Select only the numeric columns
numeric_columns = df.select_dtypes(include='number')

# Round the numeric columns to integers
rounded_numeric_columns = numeric_columns.round().astype(int)

# Combine the rounded numeric columns with the non-numeric columns
rounded_df = pd.concat([df.drop(columns=numeric_columns.columns), rounded_numeric_columns], axis=1)




# Pivot the DataFrame for the heatmap
#heatmap_data  = predicted_df.pivot_table(index='Continent', columns='Healthy life expectancy', values=['Happiness score'])
#heatmap_data_filled = heatmap_data.bfill(axis=1)

rotated_matrix = np.transpose(heatmap_data_filled)
#print(rounded_df)
#print(rotated_matrix)

#pivot_df_happiness = df.pivot_table(index='Year', columns='Healthy life expectancy', values='Happiness score')
#pivot_df_access = df.pivot_table(index='Continent', columns='Year', values='Healthy life expectancy', aggfunc='mean')

# Plotting the heatmap for Happiness Score
plt.figure(figsize=(28, 7))
plt.style.use('ggplot')
plt.subplot(1, 2, 1)
sns.heatmap(rotated_matrix,  annot=True,  fmt='.1f',cmap="crest", cbar_kws={'label': 'Healthy life expectancy'},linewidth=.2)


#plt.title('Happiness Score by Continent Over Years')
plt.xlabel('Happiness Score')
# Plotting the heatmap for Healthcare Access
#plt.subplot(1, 2, 2)
#sns.heatmap(pivot_df_access, cmap='YlGnBu', annot=True, fmt=".2f", cbar_kws={'label': 'Healthcare Access'})
#plt.title('Healthcare Access by Continent Over Years')

plt.tight_layout()
plt.show()


# In[ ]:




