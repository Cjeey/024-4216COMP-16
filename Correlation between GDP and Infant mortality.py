import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("world-data-2023.csv")

# Remove the dollar sign and commas from the 'GDP' column, and convert it to float
df['GDP'] = df['GDP'].str.replace(',', '').str.replace('$', '').astype(float)

# Convert 'Infant mortality' to float
df['Infant mortality'] = df['Infant mortality'].astype(float)

fig, ax = plt.subplots(figsize=(10, 15))  # Use ax instead of axs

# Plot the correlation between GDP and Infant mortality
ax.scatter(df["GDP"], df['Infant mortality'], alpha=0.6, edgecolors='w', color='blue')
ax.set_title('Correlation between GDP and Infant mortality')
ax.set_xlabel('GDP')
ax.set_ylabel('Infant mortality')
ax.grid(True)

plt.tight_layout()
plt.show()



  
