import matplotlib.pyplot as plt
import pandas as pd

def Ya_visualisation():
    # Reads the CSV file and turns it into a pandas dataframe
    df = pd.read_csv('world-data-2023.csv')

    # Cleaning the data by removing "%", "," and converting it to a float
    df['Agricultural Land( %)'] = df['Agricultural Land( %)'].str.replace('%', '').astype(float)
    df['Land Area(Km2)'] = df['Land Area(Km2)'].str.replace(',', '').astype(float)

    # Gathering the top 5 countries with the highest agricultural land percentage and land area (Km2)
    top_al = df.sort_values('Agricultural Land( %)', ascending=False).head(5)
    top_la = df.sort_values('Land Area(Km2)', ascending=False).head(5)

    # Creating a figure for the plot with a specific size
    plt.figure(figsize=(10, 5))

    # Creating a scatter chart with the top 5 countries with the highest agricultural land percentage and land area (Km2)
    plt.scatter(df["Land Area(Km2)"], df['Agricultural Land( %)'], color='blue')
    
    # Titling and labeling the data
    plt.title('Correlation between land area and Agricultural Land')
    plt.xlabel('Land area (Km²)')
    plt.ylabel('Agricultural land (%)')
    
    # Just shows the plot
    plt.show()

    # Creating a figure for the plot with a specific size
    plt.figure(figsize=(10, 5))

    # Creating a bar chart with the top 5 countries with the highest agricultural land percentage
    bars_al = plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color='blue')
    
    # Adding a legend to the plot with the names of the countries
    plt.legend(bars_al, top_al['Country'])
    
    # Titling and labeling the data
    plt.title('Countries with the largest agricultural land percentage')
    plt.xlabel('Countries')
    plt.ylabel('Agricultural land (%)')
    
    # Just shows the plot
    plt.show()

    # Creating a figure for the plot with a specific size
    plt.figure(figsize=(10, 5))
   
    # Creating a bar chart with the top 5 countries with the largest land area (km2)
    bars_la = plt.bar(top_la['Country'], top_la['Land Area(Km2)'], color='blue')

    # Adding a legend to the plot with the names of the countries
    plt.legend(bars_la, top_la['Country'])
    
    # Titling and labeling the data
    plt.title('Countries with the largest land area (km²)')
    plt.xlabel('Countries')
    plt.ylabel('Land area (km²)')
    
    # Just shows the plot
    plt.show()


