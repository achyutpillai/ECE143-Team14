import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pycountry_convert import country_name_to_country_alpha2, country_alpha2_to_continent_code, convert_continent_code_to_continent_name

# Read pollution dataset
df_pollution = pd.read_csv('data/pollution/pollution_dataset.csv')
df_pollution = df_pollution[['Country', 'AQI Value']]
df_pollution = df_pollution.sort_values(by='AQI Value', ascending=False)
df_pollution = df_pollution.drop_duplicates(subset=['Country'], keep='first')

# Read happiness index dataset
df_happiness = pd.read_csv('C:/Users/alexi/Documents/ECE 143/Final Project/happinessindex.csv')
df_happiness = df_happiness[['Country name', 'Ladder score']]

# Merge datasets
merged_df = pd.merge(df_pollution, df_happiness, left_on='Country', right_on='Country name', how='inner')

# Function to get continent for a country
def get_continent_for_country(row):
    try:
        country_alpha2 = country_name_to_country_alpha2(row['Country'])
        country_continent_code = country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except (ValueError, KeyError) as e:
        print(f"Error getting continent for {row['Country']}: {e}")
        return None

# Add continent column
merged_df['Continent'] = merged_df.apply(get_continent_for_country, axis=1)

# Scatter plot with color coordination based on continent
fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the width by changing the first value in figsize

# Scatter plot with color coordination based on continent
scatter = ax.scatter(merged_df['AQI Value'], merged_df['Ladder score'], c=merged_df['Continent'].astype('category').cat.codes, cmap='tab10', alpha=0.7)

# Calculate the trend line
x = merged_df['AQI Value']
y = merged_df['Ladder score']
m, b = np.polyfit(x, y, 1)

# Plot the trend line as solid
sorted_indices = np.argsort(x)
ax.plot(x[sorted_indices], m*x[sorted_indices] + b, color='black', linestyle='-', linewidth=2)

# Create legend
legend_labels = merged_df['Continent'].unique()
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.tab10(i), markersize=10) for i in range(len(legend_labels))]
legend_labels = np.append(legend_labels, 'Trend line')
legend_handles.append(plt.Line2D([0], [0], color='black', linestyle='-', linewidth=2))
ax.legend(legend_handles, legend_labels, title='Continent', loc='best')

# Set labels and title
ax.set_xlabel('AQI Value')
ax.set_ylabel('Happiness Index')
ax.set_title('AQI Score vs Happiness Index')

# Show the plot
plt.show()
