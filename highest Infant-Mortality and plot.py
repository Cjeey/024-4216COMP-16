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

    

    # Get the 5 countries with the highest Infant-Mortality and plot
    top_infant_mortality = df.nlargest(5, 'Infant mortality')
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    bars_infant_mortality = axs[1].bar(top_infant_mortality['Country'], top_infant_mortality['Infant mortality'], color=colors, alpha=0.7)
    axs[1].set_title('5 Countries with the highest Infant-Mortality')
    axs[1].set_xlabel('Country')
    axs[1].set_ylabel('Infant mortality')
    axs[1].legend(bars_infant_mortality, top_infant_mortality['Country'])
    axs[1].grid(True)

    
    plt.tight_layout()
    plt.show()

# Call the plotting function
plot_data(df)
