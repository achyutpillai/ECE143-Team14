import pandas as pd
import plotly.express as px

# reads happiness report csv
happiness = pd.read_csv('data/happinessReport2023/cleanData/clean2023HappinessData.csv')

# saves only needed columns for social support
social = happiness[['Country name', 'year','Life Ladder', 'Social support', 'Country Code', 'Continent', 'Region']]
social = social.dropna(subset=['Social support']).reset_index(drop=True) # drops any NaN values

# Creates a hsitogram of average Social Support Scores by country over the years
fig = px.histogram(social, x='Country name', y='Social support', color='Continent', histfunc='avg', template="plotly_white",
             title='Average Social Support by Country(2005-2022)').update_xaxes(categoryorder="total ascending")
fig.show() # displays figure

# Calculates correlation between social support and life ladder
corr = round(social['Social support'].corr(social['Life Ladder']), 3)

# Creates scatter plot of social support vs life ladder with trendline
fig = px.scatter(social, x='Social support', y='Life Ladder', color='Continent', trendline='ols', trendline_scope="overall", trendline_color_override="black",
                 title='Social Support vs Life Ladder(2005-2022)<br>' + 'Correlation: ' + str(corr), template="plotly_white")
fig.show() # displays figure

# finds average life ladder and social support for every country
avg_social_by_country = social.groupby('Country name').agg({
    'Social support': 'mean',
    'Life Ladder': 'mean',
    'Continent': 'first',
    'Region': 'first'
    }).reset_index()


# sorts by social support
avg_social_by_country = avg_social_by_country.sort_values('Social support').reset_index(drop=True)

# Creates a bar plot of average social support colored from red to green by least to greatest
fig = px.bar(avg_social_by_country, x='Country name', y='Social support', color='Social support', color_continuous_scale='RdYlGn',
             title='Average Social Support by Country(2005-2022)', template="plotly_white")
fig.show() # displays figure

bottomTen = avg_social_by_country[:10] # bottom 10 social support scores
topTen = avg_social_by_country[-10:].sort_values('Social support', ascending=False) # top 10 social support scores


