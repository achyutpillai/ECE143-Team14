import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a pandas DataFrame
file_path = 'CPI2021GlobalResults.csv'  # Use the correct path to your CSV file
cpi_data = pd.read_csv(file_path, skiprows=2)

# Extract the columns that contain the yearly CPI scores
cpi_score_columns = [col for col in cpi_data.columns if 'CPI score' in col]

# Calculate the average CPI score for each year
average_cpi_scores = cpi_data[cpi_score_columns].mean()

# Create a line chart to display the average CPI scores
plt.figure(figsize=(10, 5))
plt.plot(average_cpi_scores.index, average_cpi_scores.values, marker='o', color='skyblue', linestyle='-')

# Annotate each point with the value of the average
for i, txt in enumerate(average_cpi_scores.values):
    plt.annotate(round(txt, 2), (average_cpi_scores.index[i], txt), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Average CPI Scores by Year')
plt.xlabel('Year')
plt.ylabel('Average CPI Score')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping
plt.grid(True)
plt.show()
