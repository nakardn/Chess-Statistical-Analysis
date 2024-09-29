import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def qq_plot(data):

    # Create QQ plot using statsmodels
    fig, ax = plt.subplots()
    sm.qqplot(data, line='s')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')
    
    return fig
    
    