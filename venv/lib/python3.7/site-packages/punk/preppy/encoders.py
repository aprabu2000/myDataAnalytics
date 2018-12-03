import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import random


def encode_df(df, data_types={}):
    """
    Encode columns so their values are usable in vector operations. Making a few 
    assumptions here, like that datetime should be an integer, and that it's 
    acceptable to fill NaNs with 0.
    """

    numbers = []
    categories = []
    datetimes = []
        
    for column, series in df.iteritems():
        if column in data_types:
            dtypes = data_types[column]
        else:
            dtypes = {}
        
        if 'datetime' in dtypes:
            index = pd.DatetimeIndex(pd.to_datetime(series.values))
            df[column] = index.astype(np.int64).astype(float)
            datetimes.append(column)
            
        elif any([dtype in dtypes for dtype in ['category', 'label']]):
            # If this can be treated as a category, encode it
            df = pd.get_dummies(df,columns=[column])
            categories.append(column)
                    
        elif 'numeric' in dtypes:
            df[column] = clean_numbers(df[column].values)
            df[column] = df[column].astype(float)
            numbers.append(column)
            
        else:
            df.drop(column,1,inplace=True)

    # Scale continuous columns
    scaler = MinMaxScaler()
    df[numbers + datetimes] = scaler.fit_transform(df[numbers + datetimes])
    
    return df, categories, numbers, datetimes

