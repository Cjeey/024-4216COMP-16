import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('world-data-2023.csv')

# Remove the dollar sign and commas from the 'GDP' column, and convert it to float
df['GDP'] = df['GDP'].str.replace(',', '').str.replace('$', '').astype(float)

# Convert 'Infant mortality' to float
df['Infant mortality'] = df['Infant mortality'].astype(float)

def plot_data(df):
    fig, axs = plt.subplots(3, figsize=(10, 15))
    
    # Define colors for the bar plots
    colors = ['blue', 'green', 'red', 'purple', 'orange']

    # Get the 5 countries with the highest GDP and plot
    top_gdp = df.nlargest(5, 'GDP')
    bars_gdp = axs[2].bar(top_gdp['Country'], top_gdp['GDP'], color=colors, alpha=0.7)
    axs[2].set_title('5 Countries with the highest GDP')
    axs[2].set_xlabel('Country')
    axs[2].set_ylabel('GDP')
    axs[2].legend(bars_gdp, top_gdp['Country'])
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()

# Call the plotting function
plot_data(df)
