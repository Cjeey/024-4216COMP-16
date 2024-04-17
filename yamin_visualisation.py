import matplotlib.pyplot as plt
import pandas as pd

def Ya_visualisation():
    df = pd.read_csv('world-data-2023.csv')
    df['Agricultural Land( %)'] = df['Agricultural Land( %)'].str.replace('%', '').astype(float)
    df['Land Area(Km2)'] = df['Land Area(Km2)'].str.replace(',', '').astype(float)
    
    top_al = df.sort_values('Agricultural Land( %)', ascending=False).head(5)
    top_la = df.sort_values('Land Area(Km2)', ascending=False).head(5)

    plt.figure(figsize=(10, 5))
    plt.scatter(df["Land Area(Km2)"], df['Agricultural Land( %)'], color='blue')
    plt.title('Correlation between land area and Agricultural Land')
    plt.xlabel('Land area (Km²)')
    plt.ylabel('Agricultural land (%)')
    plt.show()

    plt.figure(figsize=(10, 5))
    bars_al = plt.bar(top_al['Country'], top_al['Agricultural Land( %)'], color='blue')
    plt.legend(bars_al, top_al['Country'])
    plt.title('Countries with the largest agricultural land percentage')
    plt.xlabel('Countries')
    plt.ylabel('Agricultural land (%)')
    plt.show()

    plt.figure(figsize=(10, 5))
    bars_la = plt.bar(top_la['Country'], top_la['Land Area(Km2)'], color='blue')
    plt.legend(bars_la, top_la['Country'])
    plt.title('Countries with the largest land area (km²)')
    plt.xlabel('Countries')
    plt.ylabel('Land area (km²)')
    plt.show()


