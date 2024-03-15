import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/healthcare/_hap.csv')
print(df.head())

plt.figure(figsize=(12, 8))
sns.scatterplot(data = df, x = "Happiness score", y = "Healthcare Access", hue = 'Country name')
plt.show()