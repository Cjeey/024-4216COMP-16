import matplotlib.pyplot as plt
import pandas as pd

# Reads the CSV file and turns it into a pandas dataframe named "db" for database
db = pd.read_csv('world-data-2023.csv')

# Cleaning the data by removing "," and converting it to a float
db['Land Area(Km2)'] = db['Land Area(Km2)'].str.replace(',', '').astype(float)

# Gathering the top 5 countries with the largest land area (km2)
top_la = db.sort_values('Land Area(Km2)', ascending = False).head(5)

# Creating a figure for the plot with a specific size
plt.figure(1, figsize = (10, 5))

# Creating a bar chart with the top 5 countries with the largest land area (km2)
plt.bar(top_la['Country'], top_la['Land Area(Km2)'], color = 'blue')

# Adding a legend to the plot with the names of the countries
plt.legend(plt.bar(top_la['Country'], top_la['Land Area(Km2)'], color = 'blue'), top_la['Country'])

# Titling and labeling the data
plt.title('Countries with the largest land area (km2)')
plt.ylabel('Land area')
plt.xlabel('Countries')

# Just shows the plot
plt.show()
