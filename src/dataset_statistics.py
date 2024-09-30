import numpy as np
import pandas as pd
import scipy.stats as stats

def dataset_statistics(data):
    # Calculate statistics
    mean = np.mean(data)
    std = np.std(data)
    skew = stats.skew(data)
    kurt = stats.kurtosis(data)

    # Print statistics
    print("Mean:", mean)
    print("Standard Deviation:", std)
    print("Skewness:", skew)
    print("Kurtosis:", kurt)