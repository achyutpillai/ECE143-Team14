import pandas as pd 
import plotly.express as px #for making plots
import country_converter as coco #for country codes

cc = coco.CountryConverter()

#reads in happiness report, pollution, and healthcare access datasets
happiness = pd.read_csv('data/happinessReport2023/cleanData/clean2023HappinessData.csv')
pollution = pd.read_csv('data/pollution/pollution_dataset.csv')
healthcare = pd.read_csv('data/healthcare/_hap.csv')

healthcare = healthcare.rename(columns={'Year': 'year'}) # renames year column to match year column in happiness df
happiness.dropna(inplace=True) # drops any NaN values



# only saves country name and pollution value
pollution = pollution[['Country', 'AQI Value']]
# only saves country name, year and healthcare value
healthcare = healthcare[['Country name', 'year', 'Healthcare Access']]

pollution = pollution.groupby('Country')['AQI Value'].mean().reset_index() #averages out aqi value for all entries with same country

# adds country codes to pollution and healthcare as another column using country converter
pollution['Country Code'] = pollution['Country'].apply(lambda x: cc.convert(x, to='ISO3', not_found=None))
healthcare['Country Code'] = healthcare['Country name'].apply(lambda x: cc.convert(x, to='ISO3', not_found=None))


merged = pd.merge(happiness, pollution, on='Country Code', how='left') # merges happiness dataframe with pollution dataframe on country codes
merged = pd.merge(merged, healthcare, on=['Country Code', 'year'], how='left') # merges healthcare access df to all categories df on country codes
# merged = merged.dropna(subset=['AQI Value']) # drops any NaN values

# only takes values of all categories that we want to see correlation of
correlation = merged[['Life Ladder', 'Log GDP per capita', 'Healthy life expectancy at birth', 'Social support', 'Freedom to make life choices',
                       'Perceptions of corruption', 'AQI Value', 'Healthcare Access']]

# calculates correlation between each category and squares it
corr_matrix = round(correlation.corr()**2, 4)

print(corr_matrix) # prints correlation matrix

# creates 2d squared correlation heatmap
fig = px.imshow(corr_matrix,
                labels=dict(x='Categories', y='Categories', color='Squared Correlation Coefficient'),
                x=corr_matrix.columns,
                y=corr_matrix.index,
                title='Squared Correlation Coefficients of Happiness Report Categories(2005-2022)')

# Show the plot
fig.show()
