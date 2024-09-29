import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def tr_plot(df1, df2):
    # Generate random data for four datasets
    data1 = df1['white_rating']
    data2 = df2['white_rating']

    data = [data1, data2]

    # Set up the figure and axes
    fig, axs = plt.subplots(2, figsize=(10, 10))

    for i, ax in enumerate(axs.flatten()):
        # Plot the histogram
        if i % 2 == 0:
            color = 'b'
        else:
            color = 'g'
        ax.hist(data[i], bins=50, density=True, alpha=0.6, color=color)
        
        # Fit a normal distribution to the data
        mu, std = stats.norm.fit(data[i])
        
        # Plot the PDF of the fitted normal distribution
        xmin, xmax = ax.get_xlim()
        x = np.linspace(xmin, xmax, 100)
        p = stats.norm.pdf(x, mu, std)
        ax.plot(x, p, 'k', linewidth=2)
        
        # Title with the fit parameters
        title1 = 'player rating'
        title2 = ' before transformation' if i % 2 == 0 else ' after transformation'
        ax.set_title(title1+title2)

    return fig

