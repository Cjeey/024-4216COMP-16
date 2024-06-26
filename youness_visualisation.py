import pandas as pd
import matplotlib.pyplot as plt

def Yo_visualisation():
    df = pd.read_csv('world-data-2023.csv')
    
    # Remove the dollar sign and commas from the 'GDP' column, and convert it to float
    df['GDP'] = df['GDP'].replace('[\$,]', '', regex=True).astype(float)
    
    # Convert 'Infant mortality' to float (assuming it is given as a string with commas)
    df['Infant mortality'] = df['Infant mortality'].replace(',', '', regex=True).astype(float)
   
    fig, axs = plt.subplots(3, figsize=(10, 15))

    # Plot the correlation between GDP and Infant mortality
    axs[0].scatter(df["GDP"], df['Infant mortality'], alpha=0.6, edgecolors='w', color='blue')
    axs[0].set_title('Correlation between GDP and Infant mortality')
    axs[0].set_xlabel('GDP ($)')
    axs[0].set_ylabel('Infant mortality (per 1000 live births)')
    axs[0].grid(True)


    # Get the 5 countries with the highest Infant-Mortality and plot
    top_infant_mortality = df.nlargest(5, 'Infant mortality')
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    bars_infant_mortality = axs[1].bar(top_infant_mortality['Country'], top_infant_mortality['Infant mortality'], color=colors, alpha=0.7)
    axs[1].set_title('5 Countries with the highest Infant-Mortality')
    axs[1].set_xlabel('Country')
    axs[1].set_ylabel('Infant mortality (per 1000 live births)')
    axs[1].legend(bars_infant_mortality, top_infant_mortality['Country'])
    axs[1].grid(True)
   
    
    # Get the 5 countries with the highest GDP and plot
    top_gdp = df.nlargest(5, 'GDP')
    bars_gdp = axs[2].bar(top_gdp['Country'], top_gdp['GDP'], color=colors, alpha=0.7)
    axs[2].set_title('5 Countries with the highest GDP')
    axs[2].set_xlabel('Country')
    axs[2].set_ylabel('GDP ($)')
    axs[2].legend(bars_gdp, top_gdp['Country'])
    axs[2].grid(True)
    
    plt.tight_layout()

    plt.show()
