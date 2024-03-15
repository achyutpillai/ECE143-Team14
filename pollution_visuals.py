import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

df = pd.read_csv('data/pollution/pollution_dataset.csv')
columns_to_keep = ['Country', 'AQI Value']
df = df[columns_to_keep]
df = df.sort_values(by='AQI Value', ascending=False)
df = df.drop_duplicates(subset=['Country'], keep='first')
df1 = df.head(10)
df2 = df.tail(10)

# Set up subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Use 'RdYlGn_r' colormap for the bar graphs (reverse the color mapping)
cmap = cm.get_cmap('RdYlGn_r')

# Create a custom normalization function to make the lowest values change faster
min_value = df['AQI Value'].min()
max_value = df['AQI Value'].max()

def custom_normalize(value):
    normalized_value = (value - min_value) / (max_value - min_value)
    return normalized_value**0.75  # Adjust the exponent to control how quickly the colors change

# Normalize AQI values using the custom normalization function
norm1 = Normalize(vmin=min_value, vmax=max_value)
norm1_custom = custom_normalize(df1['AQI Value'])
colors1 = cmap(norm1_custom)

# Plotting the first DataFrame (worst AQI values) with the reversed 'RdYlGn' colormap
df1.plot(x='Country', y='AQI Value', kind='bar', ax=ax1, color=colors1, legend=False)
ax1.set_ylim([300, 520])
ax1.set_title('Worst 10 Country')

# Annotate each bar with its value
for index, value in enumerate(df1['AQI Value']):
    ax1.text(index, value, str(value), ha='center', va='bottom', fontsize=10, color='black')

# Normalize AQI values using the custom normalization function for the second DataFrame
norm2_custom = custom_normalize(df2['AQI Value'])
colors2 = cmap(norm2_custom)

# Plotting the second DataFrame (best AQI values) with the reversed 'RdYlGn' colormap
df2.plot(x='Country', y='AQI Value', kind='bar', ax=ax2, color=colors2, legend=False)
ax2.set_title('Top 10 Countries')

# Annotate each bar with its value
for index, value in enumerate(df2['AQI Value']):
    ax2.text(index, value, str(value), ha='center', va='bottom', fontsize=10, color='black')

# Adding labels and title
fig.suptitle('Ranked Countries by AQI Value', fontsize=14)
ax1.set_xlabel('Country', fontsize=12)
ax1.set_ylabel('AQI Value', fontsize=12)
ax2.set_xlabel('Country', fontsize=12)
ax2.set_ylabel('AQI Value', fontsize=12)

# Change font for all text in the bar graph
font_properties = {'family': 'serif', 'color':  'darkred', 'weight': 'normal', 'size': 10}
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams.update({'text.color': 'darkred'})
plt.rcParams.update({'axes.labelcolor': 'darkred'})
plt.rcParams.update({'xtick.color': 'darkred'})
plt.rcParams.update({'ytick.color': 'darkred'})
plt.rcParams.update({'axes.labelsize': 10})

# Show the plot
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout for title
plt.show()