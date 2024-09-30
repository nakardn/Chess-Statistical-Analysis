import numpy as np
import pandas as pd
import scipy.stats as stats

def KS_norm_test(data):
    
    ks_stat, ks_p_value = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data)))

    print(f"KS Statistic: {ks_stat}, p-value: {ks_p_value}")