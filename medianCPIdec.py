import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a pandas DataFrame
file_path = 'CPI2021GlobalResults.csv'  # Use the correct path to your CSV file

cpi_data = pd.read_csv(file_path, skiprows=2)

# Extract the columns that contain the yearly CPI scores
cpi_score_columns = [col for col in cpi_data.columns if 'CPI score' in col]

# Calculate the median CPI score for each year
median_cpi_scores = cpi_data[cpi_score_columns].median()

# Create a bar chart to display the median CPI scores
plt.figure(figsize=(10, 5))
bars = plt.bar(median_cpi_scores.index, median_cpi_scores.values, color='skyblue')

# Annotate each bar with the value of the median
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2), ha='center', va='bottom')

plt.title('Median CPI Scores by Year')
plt.xlabel('Year')
plt.ylabel('Median CPI Score')
plt.xticks(rotation=45)
plt.tight_layout()  # This will adjust the plot to ensure everything fits without overlapping
plt.show()
