import pandas as pd
import plotly.express as px

#reads happienss report csv
happiness = pd.read_csv('data/WHR/cleanData/clean2023HappinessData.csv')

'''
Happiness score or subjective well-being (variable name ladder): The survey
measure of SWB is from the Jan 20, 2023 release of the Gallup World Poll
(GWP) covering years from 2005 to 2022. Unless stated otherwise, it is the national average 
response to the question of life evaluations. The English wording of the question is 
“Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top.
The top of the ladder represents the best possible life for you and the bottom 
of the ladder represents the worst possible life for you. On which step of 
the ladder would you say you personally feel you stand at this time?” This 
measure is also referred to as Cantril life ladder, or just life ladder in our analysis.
'''
#saves only the necessary columns
avg = happiness[['Country name', 'Life Ladder', 'Country Code']]

# takes the mean of life ladder score for all years and saves it with corresponding country code and name
avg = avg.groupby('Country name').agg({'Country Code': 'first', 'Life Ladder': 'mean'}).reset_index()
avg['year'] = 'AVG' # sets year AVG

result = pd.concat([happiness, avg], ignore_index=True) #adds avg dataframe to happiness dataframe as "final year"

# Creates basic choropleth map of Life Ladder Scores as Color
fig = px.choropleth(result, locations='Country Code', color='Life Ladder', hover_name='Country name', animation_frame='year',
                    projection='natural earth', title='Life Ladder Score', color_continuous_scale='Viridis')

# Increases speed of animation
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 150
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 25

fig.show() # displays figure



