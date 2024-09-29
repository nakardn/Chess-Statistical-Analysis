import numpy as np
import pandas as pd

def transform(df):
    df = df.drop(columns=['id', 'opening_name', 'opening_ply', 'moves', 'opening_eco'])
    df.drop(df[df['rated'] == False].index, inplace=True)
    df['created_at'] = pd.to_datetime(df['created_at'], unit='ms')
    df['created_at'] = df['created_at'].dt.tz_localize('UTC')
    df['last_move_at'] = df['created_at'].dt.year
    df = df.rename(columns={'last_move_at': 'year'})
    df = df.rename(columns={'created_at': 'time'})
    df = df.rename(columns={'increment_code': 'time_control'})
    df = df[df['victory_status'] != 'resign']
    df = df[df['victory_status'] != 'outoftime']
    df = df.reset_index()
    df = df.drop(columns=['index'])
    df = updateELO(df)
    df = df.rename(columns={'white_id': 'ave_rating'})
    df = df.rename(columns={'black_id': 'dif_rating'})

    for index, row in df.iterrows():
        df.at[index, 'ave_rating'] = ave(row['white_rating'], row['black_rating'])
        df.at[index, 'dif_rating'] = dif(row['white_rating'], row['black_rating'])  
    return df

def updateELO(df):
    updatedELO = {}
    for index, row in df.iterrows():
        if row['white_id'] not in updatedELO or row['time'] > updatedELO[row['white_id']][1]:
            updatedELO[row['white_id']] = (row['white_rating'], row['time'])
        if row['black_id'] not in updatedELO or row['time'] > updatedELO[row['black_id']][1]:
            updatedELO[row['black_id']] = (row['black_rating'], row['time'])

    df['white_rating'] = df.apply(lambda row: updatedELO[row['white_id']][0], axis=1)
    df['black_rating'] = df.apply(lambda row: updatedELO[row['black_id']][0], axis=1)
    return df

def ave(white_rating, black_rating):
    return (white_rating + black_rating) // 2

def dif(white_rating, black_rating):
    return (white_rating - black_rating)