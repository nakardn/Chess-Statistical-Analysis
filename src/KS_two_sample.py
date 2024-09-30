import numpy as np
import pandas as pd
import scipy.stats as stats

def KS_2test(data1, data2):
    # Perform the KS test
    ks_statistic, p_value = stats.ks_2samp(data1, data2)

    print("\n2 Sample KS Test Results:")
    print(f"  KS statistic: {ks_statistic}")
    print(f"  p-value: {p_value}")