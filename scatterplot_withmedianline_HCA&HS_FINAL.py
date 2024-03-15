import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/healthcare/_hap.csv")

# Calculate mean happiness score
mean_happiness_score = df['Happiness score'].mean()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Happiness score', y='Healthcare Access', hue='Continent')
correlation_score = (df['Healthcare Access']).corr(df['Happiness score'])
print(correlation_score)


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