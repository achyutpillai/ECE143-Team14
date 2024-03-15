import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("data/lifeExpectancy/Lifeexpectancyandhappinessscore.xlsx")
df.columns = df.columns.str.strip()
print(df.head())


plt.figure(figsize=(20, 12))
sns.scatterplot(data = df, x = "Happiness score", y = "Healthy life expectancy", hue = 'Country name')
plt.show()



