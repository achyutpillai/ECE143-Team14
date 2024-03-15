import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

# Define custom color palettes for visualization
dark_theme_colors = ["#1F1F1F", "#313131", '#636363', '#AEAEAE', '#DADADA']
# Display the custom color palettes
sns.palplot(dark_theme_colors)

# Function to create a non-linear color dictionary for custom colormaps
def create_color_dictionary(step_values, color_hex_values):
    color_dictionary = {'red': (), 'green': (), 'blue': ()}
    for step, color_hex in zip(step_values, color_hex_values):
        rgb_color = mpl.colors.hex2color(color_hex)
        for color in ('red', 'green', 'blue'):
            color_dictionary[color] += ((step, rgb_color[color == 'red'], rgb_color[color == 'green'], rgb_color[color == 'blue']),)
    return color_dictionary

thresholds = [0, 0.2, 0.5, 0.8, 1]
color_dict_example = create_color_dictionary(thresholds, dark_theme_colors)

# Create custom colormaps
custom_colormap = LinearSegmentedColormap('ExampleColormap', color_dict_example)

# Setting up Matplotlib parameters for aesthetics
mpl.rcParams.update({
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.left': False,
    'axes.titlecolor': dark_theme_colors[0],
    'axes.labelcolor': dark_theme_colors[0],
    'xtick.color': dark_theme_colors[0],
    'ytick.color': dark_theme_colors[0],
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.edgecolor': dark_theme_colors[0],
})

# Load datasets
data_current_year = pd.read_csv("data/WHR/WHR2023.csv")
data_historical = pd.read_csv("data/WHR/world-happiness-report.csv")

# Extract components of happiness from the dataset
happiness_components = list(data_current_year.columns[-7:-1])

# Prepare dataframes for visualization
dataframe = data_current_year[["Country name"] + happiness_components].set_index("Country name")
dataframe.rename(columns={'Generosity': 'Air Quality'}, inplace=True)

# Visualizing data for Finland
data_finland = dataframe.loc['Finland']
figure, axis = plt.subplots(figsize=(14, 8), dpi=75)
explode_tuple = (0, 0, 0, 0, 0, 0.1)
axis.pie(
    data_finland, 
    colors=sns.color_palette("coolwarm", 7),
    explode=explode_tuple,
    wedgeprops=dict(width=0.5, alpha=0.9),
    autopct='%1.0f%%',
    pctdistance=1.12,
    textprops={
        'fontsize': 12, 
        'color': dark_theme_colors[2],
        'fontweight': 'bold'
    }
)

# Adjusting legend and title
axis.legend(data_finland.index, title="Components", loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, borderpad=1, frameon=True, fontsize=12, title_fontsize='13', shadow=True)
plt.suptitle(t="Breakdown of Finland's Happiness Score", fontsize=24, fontweight='bold', color=dark_theme_colors[0])
plt.title("GDP significantly influences Finland's score, with perceptions of corruption contributing up to 10%", fontsize=13, color=dark_theme_colors[2])
plt.tight_layout()
plt.savefig('Visual_Finland.png', dpi=300, bbox_inches='tight')
plt.show()

# Visualizing data for Lebanon
data_lebanon = dataframe.loc['Lebanon']
figure, axis = plt.subplots(figsize=(14, 8), dpi=75)
axis.pie(
    data_lebanon, 
    colors=sns.color_palette("coolwarm", 7),
    explode=explode_tuple,
    wedgeprops=dict(width=0.5, alpha=0.9),
    autopct='%1.0f%%',
    pctdistance=1.12,
    textprops={
        'fontsize': 12, 
        'color': dark_theme_colors[2],
        'fontweight': 'bold'
    }
)

# Adjusting legend and title for Lebanon
axis.legend(data_lebanon.index, title="Components", loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, borderpad=1, frameon=True, fontsize=12, title_fontsize='13', shadow=True)
plt.suptitle(t="Breakdown of Lebanon's Happiness Score", fontsize=24, fontweight='bold', color=dark_theme_colors[0])
plt.title("Negative GDP impact and lack of social support contribute up to 19% to Lebanon's score", fontsize=13, color=dark_theme_colors[2])
plt.tight_layout()
plt.show()
