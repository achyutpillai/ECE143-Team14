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


#Create top 10 and bottom 10 identifier column

def top_bottom_identifier(value):
    if value < 11:
        return "top 10 happiest"
    if value > 127:
        return "bottom 10 happiest"
    elif 11 <= value < 128:
        return "not top/bottom 10"
    
 
happy_df_2023['top_bottom_identifier'] = happy_df_2023['rank'].map(top_bottom_identifier)


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

fig = plt. figure()
fig, axes = plt.subplots(2, 3, figsize= (10, 6))
plt.tight_layout(pad= 3)


plta = sns.kdeplot( data=happy_region_df, x='gdp_per_capita',color='#37F090',fill=True, ax=axes[0,0])
pltb = sns.kdeplot( data=happy_region_df, x='healthy_life_expectancy',color='#00D0A3',fill=True, ax=axes[0,1])
pltc = sns.kdeplot( data=happy_region_df, x='social_support',color='#00ADA7',fill=True, ax=axes[0,2])
pltd = sns.kdeplot( data=happy_region_df, x='freedom_to_make_life_choices',color='#008A9A',fill=True, ax=axes[1,0])
plte = sns.kdeplot( data=happy_region_df, x='generosity',color='#08687E',fill=True, ax=axes[1,1])
pltf = sns.kdeplot( data=happy_region_df, x='perceptions_of_corruption',color='#2F4858',fill=True, ax=axes[1,2])


plta.axvline(x = happy_region_df['gdp_per_capita'].mean(), color = 'red')
plta.axvline(x = happy_region_df['gdp_per_capita'].median(), color = 'black')
pltb.axvline(x = happy_region_df['healthy_life_expectancy'].mean(), color = 'red')
pltb.axvline(x = happy_region_df['healthy_life_expectancy'].median(), color = 'black')
pltc.axvline(x = happy_region_df['social_support'].mean(), color = 'red')
pltc.axvline(x = happy_region_df['social_support'].median(), color = 'black')
pltd.axvline(x = happy_region_df['freedom_to_make_life_choices'].mean(), color = 'red')
pltd.axvline(x = happy_region_df['freedom_to_make_life_choices'].median(), color = 'black')
plte.axvline(x = happy_region_df['generosity'].mean(), color = 'red')
plte.axvline(x = happy_region_df['generosity'].median(), color = 'black')
pltf.axvline(x = happy_region_df['perceptions_of_corruption'].mean(), color = 'red')
pltf.axvline(x = happy_region_df['perceptions_of_corruption'].median(), color = 'black')
pltf.axvline(x = happy_region_df['perceptions_of_corruption'].median(), color = 'black')

#Visualise GDP per capita on a global scale

gdp_world_map = px.choropleth(happy_region_df, locations = "iso_alpha", 
              color = "gdp_per_capita", scope = 'world', title = "GDP Ranking World Map", 
              color_continuous_scale= "rdylgn", hover_name="country")

gdp_world_map.show()

mean_happiness = happy_region_df.groupby('sub_region')[['happiness_score']].mean()
mean_happiness = mean_happiness.sort_values(by=['happiness_score'], ascending=False)
mean_happiness


#lets see what this looks like on a boxplot graph, ordering my sub_region mean

fig, ax = plt.subplots(figsize=(10,8))
plt.title("Happiness score boxplot by sub region", fontsize = 20)
sns.boxplot(y="sub_region", x="happiness_score", data=happy_region_df, orient="h", ax=ax, palette='Greens_r'
            , order=["Australia and New Zealand", "Northern Europe", "Western Europe", "Northern America", "Eastern Europe"
                     ,"Southern Europe","Latin America and the Caribbean","Eastern Asia","Central Asia","South-eastern Asia"
                     ,"Western Asia","Northern Africa","Sub-Saharan Africa","Southern Asia"]).set(
    xlabel='Happiness Score', 
    ylabel='Sub Region'
)

#Lets visualise this dataframe
palette ={"Europe": "#00A5E3", "Asia": "#4DD091", "Oceania": "#74737A", "Americas": "#FF5C77", "Africa": "#FFA23A"}
plt.figure(figsize = (5,10))
sns.pairplot(happy_region_df, hue = 'region', palette = palette)

fig, axes = plt.subplots(figsize=(11, 7))

# Define your custom palette
palette2 = {"top 10 happiest": "#00CC00", "bottom 10 happiest": "#FF0000", "not top/bottom 10": "#f5d79d"}

# Create the scatter plot
plot = sns.scatterplot(
    x=happy_region_df.gdp_per_capita,
    y=happy_region_df.happiness_score,
    ax=axes,
    hue=happy_region_df.top_bottom_identifier,
    palette=palette2,
    s=50,
    legend='full'  # Ensure legend is shown
)

# Set the labels and title
axes.set_xlabel("GDP per Capita", fontsize=14)
axes.set_ylabel("Happiness Score", fontsize=14)
axes.set_title("Happiness score correlated to GDP per Capita for 2023 : Highlighting Top and Bottom Ranks", fontsize=20)

# Handle the legend
# Extract the handles and labels from the current plot
handles, labels = axes.get_legend_handles_labels()
# Create a custom legend
axes.legend(handles=handles, labels=labels, title='Category', loc='best', fontsize='medium', title_fontsize='13')

# Show the plot
plt.show()


palette = {
    "Europe": "#00A5E3", 
    "Asia": "#4DD091", 
    "Oceania": "#74737A", 
    "Americas": "#FF5C77", 
    "Africa": "#FFA23A"
}

# Create a scatter plot
fig, axes = plt.subplots(figsize=(10,8))
sns.scatterplot(x='gdp_per_capita', y='happiness_score', data=happy_region_df,
                hue='region', palette=palette, s=50, ax=axes)

# Set the labels and title
plt.xlabel("GDP per Capita")
plt.ylabel("Happiness Score")
plt.title("Happiness score correlated to GDP per Capita for 2023", fontsize=20)

# Ensure the legend is displayed. This line may be adjusted or omitted if the legend displays correctly by default.
axes.legend(title='Region')

#plt.savefig('GDP2023.png')
plt.show()

corr = round(happy_region_df['gdp_per_capita'].corr(happy_region_df['happiness_score']), 3)

# Creating the scatter plot with a trendline
fig = px.scatter(happy_region_df, x='gdp_per_capita', y='happiness_score', color='region',
                 trendline='ols', trendline_scope="overall", trendline_color_override="black",
                 template="plotly_white",
                 labels={"gdp_per_capita": "GDP per Capita", "happiness_score": "Happiness Score"}, # Correctly setting axis labels
                 title=f"Happiness score correlated to GDP per Capita for 2023<br>Correlation: {corr}") # Setting the title
fig.update_layout(legend_title_text='Continents')
fig.write_image('images/GDP/GDP2023.png')

fig.show()

corr = round(happy_region_df['gdp_per_capita'].corr(happy_region_df['happiness_score']), 3)

# Creating the scatter plot with a trendline
fig = px.scatter(happy_region_df, x='gdp_per_capita', y='happiness_score', color='top_bottom_identifier',
                 trendline='ols', trendline_scope="overall", trendline_color_override="black",
                 template="plotly_white",
                 labels={"gdp_per_capita": "GDP per Capita", "happiness_score": "Happiness Score"}, # Correctly setting axis labels
                 title=f"Happiness score correlated to GDP per Capita for 2023<br>Correlation: {corr}") # Setting the title
fig.update_layout(legend_title_text='Continents')
fig.write_image('images/GDP/GDPTB2023.png')

fig.show()

correlation_mattrix = happy_region_df.drop(columns=['country','top_bottom_identifier','iso_alpha','region','sub_region'])
correlation_df = correlation_mattrix.corr()

#Let's visualise some of the strongest correlations

fig, axes = plt.subplots(2, 3, figsize= (10, 7))
plt.tight_layout(pad= 3)

sns.regplot(x = happy_region_df.gdp_per_capita, y = happy_region_df.healthy_life_expectancy, marker=".", scatter_kws={"alpha":0.3,"s":75},ax=axes[0,0])
sns.regplot(x = happy_region_df.happiness_score, y = happy_region_df.social_support, marker=".", scatter_kws={"alpha":0.3,"s":75}, ax=axes[0,1])
sns.regplot(x = happy_region_df.happiness_score, y = happy_region_df.gdp_per_capita, marker=".", scatter_kws={"alpha":0.3,"s":75}, ax=axes[0,2])
sns.regplot(x = happy_region_df.happiness_score, y = happy_region_df.healthy_life_expectancy, marker=".", scatter_kws={"alpha":0.3,"s":75}, ax=axes[1,0])
sns.regplot(x = happy_region_df.gdp_per_capita, y = happy_region_df.social_support, marker=".", scatter_kws={"alpha":0.3,"s":75}, ax=axes[1,1])
sns.regplot(x = happy_region_df.social_support, y = happy_region_df.healthy_life_expectancy, marker=".", scatter_kws={"alpha":0.3,"s":75}, ax=axes[1,2])

