import pandas as pd

import matplotlib.pyplot as plt

def Al_visualisation():


    df = pd.read_csv("world-data-2023.csv")

    

    # Remove the dollar sign and commas from the 'CPI' column, and convert it to float

    df['CPI'] = df['CPI'].replace(',', '', regex=True).astype(float)

    

    # Convert 'Total tax rate' to float (assuming it is given as a string with commas)

    df['Total tax rate'] = df['Total tax rate'].replace(',', '', regex=True).replace('%', '', regex=True).astype(float)

    

    fig, axs = plt.subplots(3, figsize=(10, 15))

    

    # Plot the correlation between CPI and Total tax rate

    axs[0].scatter(df["CPI"], df['Total tax rate'], alpha=0.6, edgecolors='w', color='blue')

    axs[0].set_title('Correlation between CPI and Total tax rate')

    axs[0].set_xlabel('CPI')

    axs[0].set_ylabel('Total tax rate (percentage)')

    axs[0].grid(True)

    

    # Get the 5 countries with the highest Total tax rate and plot

    top_total_tax_rate = df.nlargest(5, 'Total tax rate')

    colors = ['blue', 'green', 'red', 'purple', 'orange']

    bars_total_tax_rate = axs[1].bar(top_total_tax_rate['Country'], top_total_tax_rate['Total tax rate'], color=colors, alpha=0.7)

    axs[1].set_title('5 Countries with the highest Total tax rate')

    axs[1].set_xlabel('Country')

    axs[1].set_ylabel('Total tax rate (percentage)')

    axs[1].legend(bars_total_tax_rate, top_total_tax_rate['Country'])

    axs[1].grid(True) 

    

    # Get the 5 countries with the highest CPI and plot

    top_cpi = df.nlargest(5, 'CPI')

    bars_cpi = axs[2].bar(top_cpi['Country'], top_cpi['CPI'], color=colors, alpha=0.7)

    axs[2].set_title('5 Countries with the highest CPI')

    axs[2].set_xlabel('Country')

    axs[2].set_ylabel('CPI')

    axs[2].legend(bars_cpi, top_cpi['Country'])

    axs[2].grid(True)

    

    plt.tight_layout()

    

    plt.show()
