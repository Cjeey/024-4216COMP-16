import matplotlib.pyplot as plt
import pandas as pd

# Reads the CSV file and turns it into a pandas dataframe named "db" for database
db = pd.read_csv('world-data-2023.csv')

# Cleaning the data by removing "%", ".", "," and converting it to a float
db['Agricultural Land( %)'] = db['Agricultural Land( %)'].str.replace('%', '').str.replace('.', '').astype(float)
db['Land Area(Km2)'] = db['Land Area(Km2)'].str.replace(',', '').astype(float)

# Gathering the top 5 countries with the highest agricultural land percentage and land area (Km2)
top_al = db.sort_values('Agricultural Land( %)', ascending = False).head(5)
top_la = db.sort_values('Land Area(Km2)', ascending = False).head(5)

# Creating a figure for the plot with a specific size
plt.figure(1, figsize=(10, 5))

# Creating a scatter chart with the top 5 countries with the highest agricultural land percentage and land area (Km2)
plt.scatter(db["Land Area(Km2)"], db['Agricultural Land( %)'], color = 'blue')

# Titling and labeling the data
plt.title('Correlation between land area and Agricultural land')
plt.xlabel('Land area')
plt.ylabel('Agricultural land')

# Just shows the plot
plt.show()

# Creating a figure for the plot with a specific size
plt.figure(1, figsize=(10, 5))

# Creating a bar chart with the top 5 countries with the highest agricultural land percentage
plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color='blue')

# Adding a legend to the plot with the names of the countries
plt.legend(plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color='blue'), top_al['Country'])

# Titling and labeling the data
plt.title('Countries with the largest agricultural land percentage')
plt.ylabel('Agricultural land')
plt.xlabel('Countries')

# Just shows the plot
plt.show()

# Creating a figure for the plot with a specific size
plt.figure(1, figsize = (10, 5))

# Creating a bar chart with the top 5 countries with the largest land area (km2)
plt.bar(top_la['Country'], top_la['Land Area(Km2)'], color = 'blue')

# Adding a legend to the plot with the names of the countries
plt.legend(plt.bar(top_la['Country'], top_la['Land Area(Km2))'], color = 'blue'), top_la['Country'])

# Titling and labeling the data
plt.title('Countries with the largest land area (km2)')
plt.ylabel('Land area')
plt.xlabel('Countries')

# Just shows the plot
plt.show()
