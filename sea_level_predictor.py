import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

    # Line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    line_fit = slope * years_extended + intercept
    plt.plot(years_extended, line_fit, color='red', label='Fit (1880-2050)')

    # Line of best fit for data from year 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000_extended = pd.Series(range(2000, 2051))
    line_fit_2000 = slope_2000 * years_2000_extended + intercept_2000
    plt.plot(years_2000_extended, line_fit_2000, color='green', label='Fit (2000-2050)')

    # Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and show the plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
