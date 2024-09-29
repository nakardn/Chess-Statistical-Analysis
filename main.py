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

save_dir = os.path.abspath('figures')

# Read the dataset
df = pd.read_csv('games.csv')

# Transforming the dataset and removing unnecesary information
df_tr = transform(df)

fig = tr_plot(df, df_tr)

save_plot(fig, 'transformation_plot', save_dir)

fig = qq_plot(df_tr['white_rating']) 

save_plot(fig, 'ratingqq', save_dir)

fig = corr_plot(df_tr) 

save_plot(fig, 'corr_mat', save_dir)

