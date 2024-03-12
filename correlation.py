import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
import pycountry
from pycountry_convert import country_name_to_country_alpha2, country_alpha2_to_continent_code, convert_continent_code_to_continent_name

df = pd.read_csv('C:/Users/alexi/Documents/ECE 143/Final Project/pollution_dataset.csv')
columns_to_keep = ['Country', 'AQI Value']
df = df[columns_to_keep]
df = df.sort_values(by='AQI Value', ascending=False)
df = df.drop_duplicates(subset=['Country'], keep='first')

df1 = pd.read_csv('C:/Users/alexi/Documents/ECE 143/Final Project/happinessindex.csv')
columns_to_keep = ['Country name', 'Ladder score']
df1 = df1[columns_to_keep]

# Merge data frames based on the 'Country' column
merged_df = pd.merge(df, df1, left_on='Country', right_on='Country name', how='inner')

def get_continent_for_country(row):
    try:
        country_alpha2 = country_name_to_country_alpha2(row['Country'])
        country_continent_code = country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except (ValueError, KeyError) as e:
        print(f"Error getting continent for {row['Country']}: {e}")
        return None
    
# Add a new column 'Continent' to the merged dataframe
merged_df['Continent'] = merged_df.apply(get_continent_for_country, axis=1)
merged_df = merged_df.dropna(subset=['Continent'])
# Display the updated dataframe
print(merged_df.head())

# Scatterplot
fig, ax = plt.subplots()

# Scatter plot with color coordination based on continent
scatter = ax.scatter(merged_df['AQI Value'], merged_df['Ladder score'], c=merged_df['Continent'].astype('category').cat.codes, cmap='tab10', alpha=0.7)

# Create a legend
legend_labels = merged_df['Continent'].unique()
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=plt.cm.tab10(i), markersize=10) for i in range(len(legend_labels))]
ax.legend(legend_handles, legend_labels, title='Continent', loc='best')

# Set labels and title
ax.set_xlabel('AQI Value')
ax.set_ylabel('Happiness Index')
ax.set_title('AQI Score vs Happiness Index')

# Show the plot
plt.show()