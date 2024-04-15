import matplotlib.pyplot as plt
import pandas as pd

db = pd.read_csv('world-data-2023.csv')
db['Agricultural Land( %)'] = db['Agricultural Land( %)'].str.replace('%', '').str.replace('.', '').astype(float)
db['Land Area(Km2)'] = db['Land Area(Km2)'].str.replace(',', '').astype(float)
top_al = db.sort_values('Agricultural Land( %)', ascending = False).head(5)
top_la = db.sort_values('Land Area(Km2)', ascending = False).head(5)

plt.figure(1, figsize=(10, 5))
plt.scatter(db["Land Area(Km2)"], db['Agricultural Land( %)'], color = 'blue')
plt.title('Correlation between land area and Co2-Emissions')
plt.xlabel('Land area')
plt.ylabel('Agricultural land')
plt.show()

plt.figure(1, figsize = (10, 5))
plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color = 'blue')
plt.legend(plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color = 'blue'), top_al['Country'])

plt.title('Countries with the largest argicultural land percentage')
plt.ylabel('Agricultural land')
plt.xlabel('Countries')

plt.show()

plt.figure(1, figsize = (10, 5))
plt.bar(top_la['Country'], top_la['Land Area(Km2)'], color = 'blue')
plt.legend(plt.bar(top_la['Country'], top_la[')'], color = 'blue'), top_la['Country'])

plt.title('Countries with the largest land area (km2)')
plt.ylabel('Land area')
plt.xlabel('Countries')

plt.show()