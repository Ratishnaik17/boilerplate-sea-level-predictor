
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years = pd.Series(range(1880, 2051))
    predictions = slope * years + intercept

    ax.plot(
        years,
        predictions,
        color='red'
    )

    # Line of best fit using data from 2000 onward
    recent_df = df[df['Year'] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_df['Year'],
        recent_df['CSIRO Adjusted Sea Level']
    )

    recent_years = pd.Series(range(2000, 2051))
    recent_predictions = (
        slope_recent * recent_years + intercept_recent
    )

    ax.plot(
        recent_years,
        recent_predictions,
        color='green'
    )

    # Set labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    fig.tight_layout()
    fig.savefig('sea_level_plot.png')

    # Return Axes object for freeCodeCamp tests
    return ax
