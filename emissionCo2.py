import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('world-data-2023.csv')

# Remove the dollar sign and commas from the 'GDP' column, and convert it to float
df['Co2-Emissions'] = df['Co2-Emissions'].str.replace(',', '').str.replace('$', '').astype(float)

# Get the 5 countries with the highest GDP
data = df.sort_values('Co2-Emissions', ascending=False).head(5)

# Specify a list of colors for the countries
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Plot the GDP of the 5 countries with highest GDP, each in a different color
plt.figure(figsize=(10, 5))
bars = plt.bar(data['Country'], data['Co2-Emissions'], color=colors, alpha=0.5)

plt.legend(bars, data['Country'])
plt.title('5 Countries with the highest Co2-Emissions')
plt.xlabel('Country')
plt.ylabel('Value')
plt.show()
