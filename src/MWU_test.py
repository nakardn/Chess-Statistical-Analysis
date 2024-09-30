import scipy.stats as stats
import numpy as np
import pandas as pd

def MWU_test(data1, data2):
    statistic, p_value = stats.mannwhitneyu(data1, data2, alternative='greater')

    data1 = data1.dropna()
    data2 = data2.dropna()
    print(f"Mann-Whitney U statistic: {statistic}")
    print(f"P-value: {p_value}")