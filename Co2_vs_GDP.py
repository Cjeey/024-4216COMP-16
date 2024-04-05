import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('world-data-2023.csv')

# Remove the dollar sign and commas from the 'GDP' and 'Co2-Emissions' columns, and convert them to float
df['GDP'] = df['GDP'].str.replace(',', '').str.replace('$', '').astype(float)
df['Co2-Emissions'] = df['Co2-Emissions'].str.replace(',', '').str.replace('$', '').astype(float)

# Plot the correlation between GDP and Co2-Emissions
plt.figure(figsize=(10, 5))
plt.scatter(df["GDP"], df['Co2-Emissions'], label='GDP vs Co2-Emissions')

plt.title('Correlation between GDP and Co2-Emissions')
plt.xlabel('GDP')
plt.ylabel('Co2-Emissions')
plt.legend()
plt.show()


