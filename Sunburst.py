import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot
import warnings

happy_2023 = pd.read_csv("data/WHR/WHR2023.csv")
country_mapping = pd.read_csv("data/continents/continents.csv")

# Dropping irrelevant columns
country_mapping.drop('alpha-2', inplace=True, axis=1)

# Remove all columns between column name 'country-code' to 'iso_3166-2' 
country_mapping = country_mapping.drop(country_mapping.loc[:, 'country-code':'iso_3166-2'].columns, axis=1)

# Remove all columns between column name 'intermediate-region' to 'intermediate-region-code' 
country_mapping = country_mapping.drop(country_mapping.loc[:, 'intermediate-region':'intermediate-region-code'].columns, axis=1)
country_mapping.head()

#Rename the columns for consistency
country_mapping = country_mapping.rename({'name':'country','alpha-3':'iso_alpha','sub-region':'sub_region'}, axis =1)


happy_2023.loc[happy_2023.duplicated()]

# Remove all columns between column name 'Ladder score in Dystopia' to 'Dystopia + residual' 
happy_2023 = happy_2023.drop(happy_2023.loc[:, 'Ladder score in Dystopia':'Dystopia + residual'].columns, axis=1)

# Remove all columns between column name 'Standard error of ladder score' to 'lowerwhisker' 
happy_2023 = happy_2023.drop(happy_2023.loc[:, 'Standard error of ladder score':'lowerwhisker'].columns, axis=1)

happy_2023['rank'] = happy_2023['Ladder score'].rank(ascending=False)
happy_2023['rank'] = happy_2023['rank'].astype(int)


happy_df_2023 = happy_2023.rename({'Country name':'country','Standard error of ladder score':'standard_error_of_ladder_score'
                                   , 'Ladder score':'happiness_score','Happiness score':'happiness_score'
                                   , 'Logged GDP per capita':'gdp_per_capita','Social support':'social_support'
                                   , 'Healthy life expectancy':'healthy_life_expectancy'
                                   , 'Freedom to make life choices':'freedom_to_make_life_choices'
                                   , 'Generosity':'generosity','Perceptions of corruption':'perceptions_of_corruption'
                                   , 'Explained by: Freedom to make life choices':'freedom_to_make_life_choices'
                                   , 'Explained by: Generosity':'generosity'
                                   , 'Explained by: Perceptions of corruption':'perceptions_of_corruption'}, axis =1)
happy_df_2023.head()


#Lets change the names in the country_mapping df to match those of the happiness report where appropriate

#Turkey ----> Turkiye
country_mapping['country'] = country_mapping['country'].str.replace('Turkey', 'Turkiye', regex=True)
#Palestine, State of ----> State of Palestine
country_mapping['country'] = country_mapping['country'].str.replace('Palestine, State of', 'State of Palestine', regex=True)
#Côte D'Ivoire ----> Ivory Coast
country_mapping['country'] = country_mapping['country'].str.replace("Côte D'Ivoire", 'Ivory Coast', regex=True)
#Macedonia ----> North Macedonia
country_mapping['country'] = country_mapping['country'].str.replace('Macedonia', 'North Macedonia', regex=True)
#Hong Kong ----> Hong Kong S.A.R. of China
country_mapping['country'] = country_mapping['country'].str.replace('Hong Kong', 'Hong Kong S.A.R. of China', regex=True)
#Taiwan ----> Taiwan Province of China
country_mapping['country'] = country_mapping['country'].str.replace('Taiwan', 'Taiwan Province of China', regex=True)
#Czech Republic ----> Czechia
country_mapping['country'] = country_mapping['country'].str.replace('Czech Republic', 'Czechia', regex=True)


#Merge the dataframes again
happy_region_df = happy_df_2023.merge(country_mapping, on='country', how='left')


#Lets fix the nulls in the last four rows manually
nan_region_rows = happy_region_df[happy_region_df['region'].isnull()]
nan_region_rows


#Manually updating region, sub_region and iso code for Kosovo
happy_region_df.loc[33,'region'] = 'Europe'
happy_region_df.loc[33,'sub_region'] = 'Southern Europe'
happy_region_df.loc[33,'iso_alpha'] = 'XXK'

#Manually updating region, sub_region and iso code for Bosnia and Herzegovina
happy_region_df.loc[70,'region'] = 'Europe'
happy_region_df.loc[70,'sub_region'] = 'Southern Europe'
happy_region_df.loc[70,'iso_alpha'] = 'BIH'

#Manually updating region, sub_region and iso code for Congo (Brazzaville)
happy_region_df.loc[85,'region'] = 'Africa'
happy_region_df.loc[85,'sub_region'] = 'Sub-Saharan Africa'
happy_region_df.loc[85,'iso_alpha'] = 'COG'

#Manually updating region, sub_region and iso code for Congo (Kinshasa)
happy_region_df.loc[132,'region'] = 'Africa'
happy_region_df.loc[132,'sub_region'] = 'Sub-Saharan Africa'
happy_region_df.loc[132,'iso_alpha'] = 'COD'


import plotly.express as px

# Assuming happy_region_df and other necessary variables are already defined

fig = px.sunburst(data_frame=happy_region_df,
                  path=["region", "sub_region", "country"],
                  values="happiness_score",
                  color="happiness_score",
                  color_continuous_scale='Viridis',
                  width=1000, 
                  height=1000,
                  title='Happiness score sunburst - region / sub region / country')

# Here's how you update the legend title
fig.update_layout(coloraxis_colorbar_title='Happiness Score')

fig.write_image(file='Sunburst.png', format='png')
fig.show()