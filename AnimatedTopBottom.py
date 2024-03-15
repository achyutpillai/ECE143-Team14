
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import init_notebook_mode
init_notebook_mode(connected = True)
import seaborn as sns

import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('world-happiness-report.csv')
print(df.columns)


df['year'] = df['year'].astype(int)

def get_top_bottom_countries(df, year):
    yearly_data = df[df['year'] == year].sort_values(by='Life Ladder', ascending=False)
    top_10 = yearly_data.head(10)
    bottom_10 = yearly_data.tail(10)
    top_10['Status'] = 'Top 10'
    bottom_10['Status'] = 'Bottom 10'
    
    # Concatenate top 10 and bottom 10
    combined = pd.concat([top_10, bottom_10]).reset_index(drop=True)
    combined['Rank'] = combined.index + 1
    return combined



frames = []
years = sorted(df['year'].unique())  # Sort years to ensure ascending order
for year in years:
    yearly_frame = get_top_bottom_countries(df, year)
    yearly_frame['year'] = year  # Add year column for animation
    frames.append(yearly_frame)

animated_df = pd.concat(frames)

# Map the 'Status' to colors
color_map = {'Top 10': 'green', 'Bottom 10': 'red'}
animated_df['color'] = animated_df['Status'].map(color_map)
max_life_ladder = animated_df['Life Ladder'].max()

# Prepare the initial data frame and frames for the animation
initial_year = animated_df['year'].min()
initial_data = animated_df[animated_df['year'] == initial_year]

initial_frame_data = [
    go.Bar(
        x=initial_data['Life Ladder'][initial_data['Status'] == status], 
        y=initial_data['Rank'][initial_data['Status'] == status], 
        name=status,  # This name attribute contributes to the legend
        orientation='h',
        marker_color=color,
        legendgroup=status
    ) for status, color in color_map.items()
]

frames = []
years = sorted(animated_df['year'].unique())

for year in years:
    yearly_data = animated_df[animated_df['year'] == year]
    frame = go.Frame(
        data=[go.Bar(
            x=yearly_data['Life Ladder'][yearly_data['Status'] == status], 
            y=yearly_data['Rank'][yearly_data['Status'] == status], 
            name=status,  # Used for legend
            orientation='h',
            marker_color=color,
            legendgroup=status,  # Keep the same group for consistent legend handling
            showlegend=True
        ) for status, color in color_map.items()
             ],
        name=str(year),
        layout=go.Layout(
            annotations=[
                # Annotations for country names
                go.layout.Annotation(
                    x=row['Life Ladder'] + max_life_ladder * 0.05,  # Offset for text
                    y=row['Rank'],
                    text=row['Country name'],
                    showarrow=False,
                    font=dict(size=10, color="black"),
                    xref="x",
                    yref="y"
                )
                for index, row in yearly_data.iterrows()
            ] + [
                # Additional annotation for displaying the year prominently in the plot
                go.layout.Annotation(
                    x=max_life_ladder * 1.1,  # Place it towards the end of the x-axis
                    y=1,  # Top of the plot
                    text=f"Year: {year}",
                    showarrow=False,
                    font=dict(size=16, color="black"),
                    xref="x",
                    yref="paper"  # Reference to the entire plotting area for y
                )
            ]
        )
    )
    frames.append(frame)

# Create the figure with the initial frame and subsequent frames
fig = go.Figure(
    data=initial_frame_data,
    layout=go.Layout(
        xaxis=dict(range=[0, max_life_ladder * 1.2], autorange=False),
        yaxis=dict(range=[0, 21], autorange=False, tickmode='array', tickvals=list(range(1, 21)), showticklabels=False),
        title="Top 10 and Bottom 10 Happiest Countries Each Year : 2005 to 2020",
        updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None, {"frame": {"duration": 750, "redraw": True}, "transition": {"duration": 150}}])])]
    ),
    frames=frames
)

fig.update_layout(showlegend=True, xaxis_title="Happiness Score", yaxis_title="Country")

fig.write_html("happiness_report_animation.html")
fig.show()

