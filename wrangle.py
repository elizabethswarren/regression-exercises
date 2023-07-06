import pandas as pd
import os
from sklearn.model_selection import train_test_split
from env import get_db_url


##############################################   ACQUIRE     ##############################################

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
               FROM properties_2017
               WHERE propertylandusetypeid=261'''
        
        url = get_db_url('zillow')

        df = pd.read_sql(sql, url)

    #caches the the file
        df.to_csv(filename, index=False)

        return df


##############################################   CLEAN     ##############################################

def clean_zillow(df):
    '''This function cleans up the zillow data.'''
    # drop all of the null values
    df = df.dropna()

    #rename the columns
    df = df.rename(columns={'bedroomcnt':'bedcount',
                        'bathroomcnt':'bathcount',
                        'calculatedfinishedsquarefeet': 'sqfeet',
                        'taxvaluedollarcnt': 'value',})

    # change the dtype for the necessary columns
    df['sqfeet'] = df.sqfeet.astype(int)

    df['yearbuilt'] = df.yearbuilt.astype(int)

    df['sqfeet'] = df.sqfeet.astype(int)

    df['fips'] = df.fips.astype(int).astype(str)

    return df

##############################################   SPLIT     ##############################################

def split_zillow(df):
    '''This function splits the clean zillow data stratified on value'''
    #train/validate/test split
    
    train_validate, test = train_test_split(df, test_size = .2, random_state=311)

    train, validate = train_test_split(train_validate, test_size = .25, random_state=311)

    return train, validate, test


##############################################   WRANGLE    ##############################################

def wrangle_zillow():
    '''Acquires and cleans zillow data in one go'''
    df = clean_zillow(get_zillow_data())

    return df


##############################################  PREPARE - SCALED    ##############################################

def scaled_zillow(train, validate, test):
    scale = sklearn.preprocessing.MinMaxScaler()

    train_scaled = scaler.fit_transform(train)
    validate_scaled = scaler.transform(validate)
    test_scaled = scaler.transform(test)

    return train_scaled, validate_scaled, test_scaled



