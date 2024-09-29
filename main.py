import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from src.transform import transform
from src.trasformation_plot import tr_plot
from src.save_plot import save_plot

save_dir = os.path.abspath('figures')

# Read the dataset
df = pd.read_csv('games.csv')

# Transforming the dataset and removing unnecesary information
df_tr = transform(df)

fig = tr_plot(df, df_tr)

save_plot(fig, 'transformation_plot', save_dir)