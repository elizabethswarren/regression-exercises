import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import sklearn.preprocessing
from sklearn.model_selection import train_test_split

import pandas as pd
import seaborn as sns

##############################################   ACQUIRE     ##############################################

def scaled_data(train, validate, test):
    '''This function takes in the train, validate, and test dataframes and returns the scaled data as dataframes.'''
    
    scaler = sklearn.preprocessing.MinMaxScaler()

    scaler.fit(train)

    train_scaled = pd.DataFrame(scaler.transform(train))
    validate_scaled = pd.DataFrame(scaler.transform(validate))
    test_scaled = pd.DataFrame(scaler.transform(test))
    
    return train_scaled, validate_scaled, test_scaled