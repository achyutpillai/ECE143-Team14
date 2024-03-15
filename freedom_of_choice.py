import pandas as pd
import plotly.express as px


happiness = pd.read_csv('data/WHR/cleanData/clean2023HappinessData.csv')

# keeps values relevant to Freedom and Life Ladder as well as location
freedom = happiness[['Country name', 'year', 'Life Ladder', 'Freedom to make life choices', 'Country Code', 'Continent', 'Region']]

freedom = freedom.dropna(subset=['Freedom to make life choices']) # drops any NaN values 

# creates histogram plot of averaged freedom values by country
fig = px.histogram(freedom, x='Country name', y='Freedom to make life choices', color='Continent', histfunc='avg', template="plotly_white",
             title='Average Freedom to make life choices by Country(2005-2022)').update_xaxes(categoryorder="total ascending")
fig.show() # displays figure

# Finds correlation between Freedom and Life Ladder
corr = round(freedom['Freedom to make life choices'].corr(freedom['Life Ladder']), 3)



# Creates a scatter plot of Freedom vs Life Ladder with a trendline
fig = px.scatter(freedom, x='Freedom to make life choices', y='Life Ladder', color='Continent', trendline='ols', trendline_scope="overall", trendline_color_override="black",
                 title='Freedom to make life choices vs Life Ladder(2005-2022)<br>' + 'Correlation: ' + str(corr), template="plotly_white")
fig.show() # displays figure

# groups countries and finds their average freedom and life ladder throughout the years
average_freedom_by_country = freedom.groupby('Country name').agg({
    'Freedom to make life choices': 'mean',
    'Life Ladder': 'mean',
    'Continent': 'first',
    'Region': 'first'
    }).reset_index()

# sorts average values by continent
average_freedom_by_country = average_freedom_by_country.sort_values('Continent')
# sorts Freedom values
average_freedom_by_country = average_freedom_by_country.sort_values('Freedom to make life choices').reset_index(drop=True)


# creates bar graph of Freedom for every country with colorbar from red to green of least to greatest
fig3 = px.bar(average_freedom_by_country, x='Country name', y='Freedom to make life choices', color='Freedom to make life choices', color_continuous_scale='RdYlGn',
             title='Average Freedom to make life choices by Country(2005-2022)', template="plotly_white")
fig3.show() # displays plot

bottomTen = average_freedom_by_country[:10] # bottom ten freedom values
topTen = average_freedom_by_country[-10:].sort_values('Freedom to make life choices', ascending=False) # top ten freedom values
# print(bottomTen.head(10))
# print(topTen.head(10))