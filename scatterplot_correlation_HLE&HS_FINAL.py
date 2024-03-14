#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\riyaj\Downloads\_life.csv")
#df = df.columns = df.columns.str.strip()
#print(df)
#df = pd.DataFrame(data)

# Calculate mean happiness score
mean_happiness_score = df['Happiness score'].mean()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Happiness score', y='Healthy life expectancy', hue='continents')
correlation_score = (df['Healthy life expectancy']).corr(df['Happiness score'])
#print(correlation_score)

#plt.text(0.02, 0.95, 'Hi Michigan', color='red', fontsize=30, fontweight='bold', transform=plt.gca().transAxes, verticalalignment='top')
#2 text
#plt.text(0.05, 0.80, round(correlation_score,5), color='red', fontsize=10, transform=plt.gca().transAxes, verticalalignment='top')


# Plot diagonal mean line
plt.plot([df['Happiness score'].min(), df['Happiness score'].max()],
         [df['Healthy life expectancy'].min(), df['Healthy life expectancy'].max()],
         color='black')

#plt.legend()
plt.legend(loc='upper left')
plt.xlabel('Happiness Score')
plt.ylabel('Healthy life expectancy')

plt.show()


# In[ ]:




