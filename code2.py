import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
This code Reads and filters data, plots data in bar plots and line plots and heat maps.
It also performs statistical functions on the data
"""

# Load the CSV file into a DataFrame
file_path = 'world_bank.csv'
df = pd.read_csv(file_path)


# List of countries to filter
countries = ['Australia', 'China', 'Colombia', 'Cyprus', 'European Union', 'United Kingdom', 'Pakistan', 
             'Russian Federation', 'United States', 'Zimbabwe']

# List of columns to select
columns_to_select = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '1990', '1995', 
                     '2000', '2005', '2010', '2015', '2020']

# Select the specified columns and update the DataFrame in place
df = df[columns_to_select]

# Filter rows containing the specified countries
df = df[df['Country Name'].isin(countries)]

indicators_to_select = ['EN.ATM.GHGT.KT.CE', 'EG.ELC.PETR.ZS']

# dataframe containing Total greenhouse gas and electricity production from oil sources
df1 = df[df['Indicator Code'].isin(indicators_to_select)]



indicators_to_select = ['SP.URB.TOTL.IN.ZS', 'AG.LND.FRST.K2']

# dataframe containing Forest area and urban population
df2 = df[df['Indicator Code'].isin(indicators_to_select)]



#Function to create bar plots of  greenhouse gas emissions and 'Electricity production from oil sources 
def create_bar_plots(df, indicators, years, bar_width=0.8):
    for indicator in indicators:
        # Filter the DataFrame for the specific indicator
        df_indicator = df[df['Indicator Name'] == indicator]

        # Select only the relevant years
        df_indicator_years = df_indicator[['Country Name'] + years]

        # Create a bar plot with adjusted bar width
        df_indicator_years.set_index('Country Name').plot(kind='bar', width=bar_width)
        plt.title(indicator)
        plt.ylabel('Value')
        plt.xlabel('Country')
        plt.show()

# Variables values
indicators_to_plot = ['Total greenhouse gas emissions (kt of CO2 equivalent)', 
                      'Electricity production from oil sources (% of total)']
years_to_plot = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

create_bar_plots(df, indicators_to_plot, years_to_plot)

#Function to create line plots of  Forest area and urban population 
def plot_indicators(df, indicators, years):
    for indicator in indicators:
        # Filter the DataFrame for the specific indicator
        df_indicator = df[df['Indicator Name'] == indicator]

        # Set up the plot
        plt.figure(figsize=(10, 6))
        plt.title(f'Comparison of {indicator}')
        plt.xlabel('Year')
        plt.ylabel('Value')

        # Plot dashed lines for each country
        for country in df['Country Name'].unique():
            country_data = df_indicator[df_indicator['Country Name'] == country]
            plt.plot(years, country_data[years].values.flatten(), label=country, linestyle='--', marker='o')

        # Show legend, grid, and plot
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.grid(True)
        plt.show()

# Variable Values
indicators_to_plot = ['Urban population (% of total population)', 'Forest area (sq. km)']
years_to_plot = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

plot_indicators(df2, indicators_to_plot, years_to_plot)

# List of indicator codes for heatmap
indicators_to_select = ['SP.URB.TOTL.IN.ZS', 'EN.ATM.GHGT.KT.CE', 'EG.ELC.PETR.ZS', 'AG.LND.FRST.K2', 
                        'EG.USE.ELEC.KH.PC', 'EG.USE.COMM.GD.PP.KD', 'EG.FEC.RNEW.ZS', 'EG.ELC.RNWX.ZS', 
                        'EG.ELC.RNEW.ZS', 'EG.ELC.NUCL.ZS', 'EG.ELC.NGAS.ZS', 
                        'EG.ELC.HYRO.ZS', 'EG.ELC.COAL.ZS']

# Select the desired columns for heatmap
columns_to_select = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', 
                     '1990', '1995', '2000', '2005', '2010', '2015', '2020']

# Filter rows containing the specified indicator codes for heatmap
dfh = df[df['Indicator Code'].isin(indicators_to_select)]

# Filtered data for heatmap
dfh = dfh[columns_to_select]


#Heatmap Code

def plot_heatmap(data, country_name):
    # Pivot the data for heatmap
    heatmap_data = data.pivot(index='Indicator Name', columns='Country Name', values=numeric_columns)

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 5))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt=".2f", cbar_kws={'label': 'Value'})
    plt.title(country_name)
    plt.show()

# List of countries
countries = ['China', 'European Union', 'United States']
numeric_columns = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']
# Loop through each country
for country in countries:
    # Filter data for the current country
    country_data = dfh[dfh['Country Name'] == country]

    # Plot heatmap for the current country
    plot_heatmap(country_data, country)

# Statistical Analysis starts
indicator_codes = ['SP.URB.TOTL.IN.ZS', 'EN.ATM.GHGT.KT.CE', 'EG.ELC.PETR.ZS', 'EG.USE.ELEC.KH.PC',
                   'EG.USE.COMM.GD.PP.KD', 'EG.FEC.RNEW.ZS', 'EG.ELC.RNWX.ZS', 'EG.ELC.RNEW.ZS',
                   'EG.ELC.NUCL.ZS', 'EG.ELC.NGAS.ZS', 'EG.ELC.HYRO.ZS', 'EG.ELC.COAL.ZS', 
                   'AG.LND.FRST.K2']

# Loop through each indicator code
for indicator_code in indicator_codes:
    # Extract data for the indicator code
    indicator_data = dfh[dfh['Indicator Code'] == indicator_code][['1990', '1995', '2000', '2005', '2010', '2015', 
                                                                   '2020']]

    #.describe() for basic statistics
    describe_stats = indicator_data.describe()

    # Additional statistical method Median
    median_value = indicator_data.median()

    # Additional statistical method standard deviation
    std_deviation = indicator_data.std()

    # Print the results for the indicator code
    print(f"\nDescribe Statistics for '{indicator_code}':")
    print(describe_stats)

    print("\nAdditional Statistical Method 1 - Median:")
    print(median_value)

    print("\nAdditional Statistical Method 2 - Standard Deviation:")
    print(std_deviation)
    print('\n' + '='*50 + '\n')  
