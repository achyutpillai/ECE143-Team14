import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/lifeExpectancy/_life.csv")

# Calculate mean happiness score
mean_happiness_score = df['Happiness score'].mean()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Happiness score', y='Healthy life expectancy', hue='continents')
correlation_score = (df['Healthy life expectancy']).corr(df['Happiness score'])
#print(correlation_score)

# Plot diagonal mean line
plt.plot([df['Happiness score'].min(), df['Happiness score'].max()],
         [df['Healthy life expectancy'].min(), df['Healthy life expectancy'].max()],
         color='black')

#plt.legend()
plt.legend(loc='upper left')
plt.xlabel('Happiness Score')
plt.ylabel('Healthy life expectancy')

plt.show()