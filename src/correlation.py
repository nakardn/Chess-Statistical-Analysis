import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def corr_plot(df):

    fig, ax = plt.subplots()
    df['winner'] = df['winner'].replace({'white' : 1, 'black' : 1, 'draw' : 0})
    corr_matrix = df[['turns', 'winner', 'ave_rating', 'dif_rating']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='seismic', center=0)
    
    return fig
    
    