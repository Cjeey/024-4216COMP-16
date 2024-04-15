import matplotlib.pyplot as plt
import pandas as pd

db = pd.read_csv('world-data-2023.csv')
db['Agricultural Land( %)'] = db['Agricultural Land( %)'].str.replace('%', '').str.replace('.', '').astype(float)
top_al = db.sort_values('Agricultural Land( %)', ascending = False).head(5)

plt.figure(1, figsize = (10, 5))
plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color = 'blue')
plt.legend(plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color = 'blue'), top_al['Country'])

plt.title('Countries with the largest argicultural land percentage')
plt.ylabel('Agricultural land')
plt.xlabel('Countries')

plt.show()