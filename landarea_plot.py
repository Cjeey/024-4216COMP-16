import matplotlib.pyplot as plt
import pandas as pd

db = pd.read_csv('world-data-2023.csv')
db['Land Area(Km2)'] = db['Land Area(Km2)'].str.replace(',', '').astype(float)
top_la = db.sort_values('Land Area(Km2)', ascending = False).head(5)

plt.figure(1, figsize = (10, 5))
plt.bar(top_la['Country'], top_la['Land Area(Km2)'], color = 'blue')
plt.legend(plt.bar(top_la['Country'], top_la['Land Area(Km2))'], color = 'blue'), top_la['Country'])

plt.title('Countries with the largest land area (km2)')
plt.ylabel('Land area')
plt.xlabel('Countries')

plt.show()