import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from src.transform import transform

# Read the dataset
df = pd.read_csv('games.csv')

# Transforming the dataset and removing unnecesary information
df = transform(df)
print(df.head(20))