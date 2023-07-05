import pandas as pd
import os
from env import get_db_url

def get_zillow_data():
    '''This function will check to see if a zillow file exists and read it.
       If the file doesn't exist it will run a sql query and cache query to csv.'''
    filename = 'zillow.csv'

    #checks if the file already exists
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    #if not, queries db
    else:
        sql = '''SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet,
                taxvaluedollarcnt, yearbuilt, taxamount, fips
               FROM properties_2017'''
        
        url = get_db_url('zillow')

        df = pd.read_sql(sql, url)

    #caches the the file
        df.to_csv(filename, index=False)

        return df


def clean_zillow(df):
    '''This function cleans up the zillow data.'''
    # drop all of the null values
    df = df.dropna()

    #rename the columns
    df = df.rename(columns={'bedroomcnt':'bedcount',
                        'bathroomcnt':'bathcount',
                        'calculatedfinishedsquarefeet': 'sqfeet',
                        'taxvaluedollarcnt': 'taxvalue',})

    # change the dtype for the necessary columns
    df['sqfeet'] = df.sqfeet.astype(int)





