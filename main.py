import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv('games.csv')

# Transforming the dataset and removing unnecesary information 
df = df.drop(columns=['id', 'opening_name'])
df.drop(df[df['rated'] == False].index, inplace=True)
df['created_at'] = pd.to_datetime(df['created_at'], unit='ms')
df['created_at'] = df['created_at'].dt.tz_localize('UTC')
df['last_move_at'] = df['created_at'].dt.year
df = df.rename(columns={'last_move_at': 'year'})
print(df.head())