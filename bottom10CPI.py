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
  
bottom_10_countries = data[-10:]

# Unpack the top 10 countries into two lists for plotting
x, y = zip(*bottom_10_countries)

plt.bar(x, y, color='r', width=0.5)

for i in range(len(x)):
    plt.text(i, y[i] + 0.5, str(y[i]), ha='center', va='bottom')

plt.xlabel('Countries')
plt.ylabel('Corruption Perceptions Index')
plt.title('Bottom 10 CPI Scores 2023')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
