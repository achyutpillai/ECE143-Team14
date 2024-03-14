#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\riyaj\Downloads\_hap.csv")
#df = df.columns = df.columns.str.strip()
#print(df)
#df = pd.DataFrame(data)

# Calculate mean happiness score
mean_happiness_score = df['Happiness score'].mean()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Happiness score', y='Healthcare Access', hue='Continent')
correlation_score = (df['Healthcare Access']).corr(df['Happiness score'])
print(correlation_score)

#plt.text(df['Happiness score'].min(), df['Healthcare Access'].max(), 'Hi Michigan', fontsize=27, fontweight='bold')

#plt.text(0.02, 0.95, 'Hi Michigan', color='red', fontsize=30, fontweight='bold', transform=plt.gca().transAxes, verticalalignment='top')
#2 text 
#plt.text(0.05, 0.80, round(correlation_score,5), color='red', fontsize=10, transform=plt.gca().transAxes, verticalalignment='top')


# Plot diagonal mean line.  Black is line colour
plt.plot([df['Happiness score'].min(), df['Happiness score'].max()], 
         [df['Healthcare Access'].min(), df['Healthcare Access'].max()],
         color='black')

#plt.legend()
#to Move Location if you want to move to  right just replace left with right 
plt.legend(loc='upper left')
plt.xlabel('Happiness Score')
plt.ylabel('Healthcare Access')

plt.show()


# In[ ]:




