import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def fit_gamma(data):
    shape, loc, scale = stats.gamma.fit(data, floc=0)  # Force location to 0 if appropriate

    # Set up the figure and axes
    fig, axs = plt.subplots()

    # Generate a range of values for plotting the fitted distribution
    x = np.linspace(1, 250, 250)

    # Plot the histogram of the actual data
    sns.histplot(data, kde=False, stat='density', label='Data')


    pdf_fitted = stats.gamma.pdf(x, shape, loc=loc, scale=scale)
    plt.plot(x, pdf_fitted, label='Fitted Gamma PDF', color='red')

    # Add plot labels
    plt.xlabel('Turns')
    plt.ylabel('Density')
    plt.legend()

    return fig