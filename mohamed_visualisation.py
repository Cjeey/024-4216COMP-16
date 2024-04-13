import pandas as pd
import matplotlib.pyplot as plt

def Mo_visualisation():
    df = pd.read_csv('world-data-2023.csv')
    
    # Clean 'Co2-Emissions' and 'Population' columns
    # Remove commas and convert to float
    df['Co2-Emissions'] = df['Co2-Emissions'].replace('[\$,]', '', regex=True).astype(float)
    df['Population'] = df['Population'].replace('[\$,]', '', regex=True).astype(float)
    
    fig, axs = plt.subplots(3, figsize=(10, 15))
    
    # Plot the correlation between CO2 Emissions and Population
    axs[0].scatter(df["Co2-Emissions"], df['Population'], alpha=0.6, edgecolors='w', color='blue')
    axs[0].set_title('Correlation between CO2 Emissions and Population')
    axs[0].set_xlabel('CO2 Emissions (in tons)')
    axs[0].set_ylabel('Population')
    axs[0].grid(True)
    
    # Get the 5 countries with the highest Population and plot
    top_population = df.nlargest(5, 'Population')
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    bars_population = axs[1].bar(top_population['Country'], top_population['Population'], color=colors, alpha=0.7)
    axs[1].set_title('5 Countries with the highest Population')
    axs[1].set_xlabel('Country')
    axs[1].set_ylabel('Population (millions)')
    axs[1].legend(bars_population, top_population['Country'])
    axs[1].grid(True)
    
    # Get the 5 countries with the highest CO2 Emissions and plot
    top_co2 = df.nlargest(5, 'Co2-Emissions')
    bars_co2 = axs[2].bar(top_co2['Country'], top_co2['Co2-Emissions'], color=colors, alpha=0.7)
    axs[2].set_title('5 Countries with the highest CO2 Emissions')
    axs[2].set_xlabel('Country')
    axs[2].set_ylabel('CO2 Emissions (in tons)')
    axs[2].legend(bars_co2, top_co2['Country'])
    axs[2].grid(True)
    
    plt.tight_layout()
    plt.show()
