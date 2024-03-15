import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a pandas DataFrame
file_path = 'data/corruption/CPI2021GlobalResults.csv'

cpi_data = pd.read_csv(file_path, skiprows=2)

# Extract the columns that contain the yearly CPI scores
cpi_score_columns = [col for col in cpi_data.columns if 'CPI score' in col]

# Calculate the median CPI score for each year
median_cpi_scores = cpi_data[cpi_score_columns].median()

boxplot_data = [cpi_data[col].dropna() for col in cpi_score_columns]

# Create a box plot for the yearly CPI scores
plt.figure(figsize=(12, 6))
boxplot_dict = plt.boxplot(boxplot_data, patch_artist=True, labels=[col.split()[-1] for col in cpi_score_columns])

# Set the labels and title
plt.title('Median CPI Scores by Year')
plt.xlabel('Year')
plt.ylabel('CPI Score')
plt.xticks(rotation=45)

# Annotate each box with the median score
for line, col in zip(boxplot_dict['medians'], cpi_score_columns):
    # Get the median value
    median = line.get_ydata()[0]
    x_position = line.get_xdata()[0] + (line.get_xdata()[1] - line.get_xdata()[0]) / 2
    plt.text(x_position, median, f'{median:.2f}', ha='center', va='bottom', fontsize=9, color='white')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()  # Adjust the layout to make room for the rotated x-axis labels
plt.show()

