import matplotlib.pyplot as plt 
import csv 

x = [] 
y = []
data = []

  
with open('cpidata.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',')
    next(plots, None) 
      
    for row in plots:
        country_name = row[0] 
        cpi_score = int(row[3])
        data.append((country_name, cpi_score))
  
bottom_10_countries = data[-10:]

# Unpack the top 10 countries into two lists for plotting
x, y = zip(*bottom_10_countries)

plt.bar(x, y, color='r', width=0.5, label="CPI")
plt.xlabel('Countries')
plt.ylabel('Corruption Perceptions Index')
plt.title('Bottom 10 CPI Scores')
plt.xticks(rotation=45)  # Rotate country names for better readability
plt.legend()
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()
