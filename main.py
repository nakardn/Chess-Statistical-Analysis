import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from src.transform import transform
from src.trasformation_plot import tr_plot
from src.save_plot import save_plot
from src.qq_rating_plot import qq_plot
from src.correlation import corr_plot
from src.gamma_fit import fit_gamma
from src.gamma_poisson_fit import fit_gamma_poisson
from src.KS_two_sample import KS_2test
from src.dataset_statistics import dataset_statistics
from src.KS_normal_test import KS_norm_test
from src.MWU_test import MWU_test

save_dir = os.path.abspath('figures')

# Read the dataset
df = pd.read_csv('games.csv')

# Transforming the dataset and removing unnecesary information
df_tr = transform(df)

fig = tr_plot(df, df_tr)

save_plot(fig, 'transformation_plot', save_dir)

fig = qq_plot(df_tr['white_rating']) 

save_plot(fig, 'ratingqq', save_dir)

KS_norm_test(df_tr['ave_rating'].astype(int))

# Classifying players into groups based on skill
df_cl = df_tr.copy()
def skill_classification(x):
    if x < 1500:
        return 'low'
    else:
        return 'high'

df_cl['ave_rating'] = df_cl['ave_rating'].apply(skill_classification)
MWU_test(df_cl[df_cl['ave_rating'] == 'high']['turns'], df_cl[df_cl['ave_rating'] == 'low']['turns'])

fig = corr_plot(df_tr) 

save_plot(fig, 'corr_mat', save_dir)

fig = fit_gamma(df_tr['turns'])

save_plot(fig, 'gamma_fit', save_dir)

fig, a_fitted, c_fitted, loc_fitted, scale_fitted, lam_fitted, w_fitted = fit_gamma_poisson(df_tr['turns'])

save_plot(fig, 'gamma_poisson_fit', save_dir)

dataset_statistics(df_tr['turns'])


data = df_tr['turns']
n = len(data)
# Use a weighted random choice to sample from the mixture
samples = np.zeros(n)
for i in range(n):
    if np.random.rand() < w_fitted:
        samples[i] = stats.gengamma.rvs(a_fitted, c_fitted, loc=loc_fitted, scale=scale_fitted)
    else:
        samples[i] = stats.poisson.rvs(lam_fitted)
KS_2test(data, samples)