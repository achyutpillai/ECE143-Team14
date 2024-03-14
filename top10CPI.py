import matplotlib.pyplot as plt 
import csv 

x = [] 
y = []
data = []

  
with open('cpidata2023.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',')
    next(plots, None) 
      
    for row in plots:
        country_name = row[0] 
        cpi_score = int(row[3])
        data.append((country_name, cpi_score))
  
top_10_countries = sorted(data, key=lambda x: x[1], reverse=True)[:10]

# Unpack the top 10 countries into two lists for plotting
x, y = zip(*top_10_countries)

plt.bar(x, y, color='c', width=0.5, label="CPI")
plt.xlabel('Countries')
plt.ylabel('Corruption Perceptions Index')
plt.title('Top 10 CPI Scores 2023')
plt.xticks(rotation=45)  # Rotate country names for better readability
plt.legend()
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()
