import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import seaborn as sns
import plotly.graph_objects as go


df = pd.read_csv('data/WHR/WHR2023.csv')
df1=pd.read_csv('data/WHR/world-happiness-report.csv')
import warnings
warnings.filterwarnings("ignore")

df.head()
df1.head()
color=["#f94144","#f3722c","#f8961e","#f9c74f","#90be6d","#43aa8b","#577590"]
sns.palplot(color)
fig = plt.figure(figsize=(15, 8))
g = gs.GridSpec(ncols=1, nrows=2, figure=fig)
plt.suptitle("Top 10 and Bottom 10 Countries in Happiness Index 2023", family='Serif', weight='bold', size=20)

# Plot for Top 10 Countries
ax1 = plt.subplot(g[0, 0])
top_10 = df.head(10)
sns.barplot(data=top_10, x='Ladder score', y='Country name', color=color[4], ax=ax1)
ax1.xaxis.set_visible(False)
ax1.annotate("Top 10 countries in Happiness index", xy=(8, 2), family='Serif', weight='bold', size=12)
for index, value in enumerate(top_10['Ladder score']):
    ax1.text(value, index, str(value), color='black', ha="left", va="center")

# Plot for Bottom 10 Countries
ax2 = plt.subplot(g[1, 0], sharex=ax1)
bot_10 = df.tail(10)
sns.barplot(data=bot_10, x='Ladder score', y='Country name', color=color[0], ax=ax2)
ax2.annotate("Bottom 10 countries in Happiness index", xy=(8, 2), family='Serif', weight='bold', size=12)
for index, value in enumerate(bot_10['Ladder score']):
    ax2.text(value, index, str(value), color='black', ha="left", va="center")

for s in ['left', 'right', 'top', 'bottom']:
    ax1.spines[s].set_visible(False)
    ax2.spines[s].set_visible(False)

# Save the figure
plt.savefig("top_and_bottom_countries_happiness_2023.png", dpi=300, bbox_inches='tight')

plt.show()

df.rename(columns={'Generosity': 'Air Quality Index'}, inplace=True)
df1.rename(columns={'Generosity': 'Air Quality Index'}, inplace=True)



categories = ['Ladder score','Logged GDP per capita','Social support','Healthy life expectancy', 'Freedom to make life choices', 'Air Quality Index', 'Perceptions of corruption']

r1=[df[each][df["Country name"]=="Afghanistan"].mean()/df[each].max()  for each in categories]
r2=[df[each][df["Country name"]=="Finland"].mean()/df[each].max()  for each in categories]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=r1,
      theta=categories,
      fill='toself',
      name='Afghanistan'
))
fig.add_trace(go.Scatterpolar(
      r=r2,
      theta=categories,
      fill='toself',
      name='Finland'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 1]
    )),
  showlegend=True
)

fig.write_image("radar_comparison_plot.png")
fig.show()





