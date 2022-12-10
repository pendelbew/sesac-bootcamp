import pandas as pd
import numpy as np
import pickle


col_list = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

def ageRange(age):
    if 21 <= age < 30:
        return 1
    elif 30 <= age < 40:
        return 2
    elif 40 <= age < 50:
        return 3
    elif 50 <= age < 60:
        return 4
    elif 60 <= age < 70:
        return 5
    else:
        return 6
    
def prefunc(df):
    for col in col_list:
        df[col] = np.where(df[col] == 0, np.nan, df[col])
        
    df['Age2'] = df['Age'].apply(ageRange)
        
    with open('dict_total.pkl', 'rb') as f:
        dict_total = pickle.load(f)
            
    for col in col_list:
        df[col].fillna(dict_total[col][df.loc[0]['Age2']],inplace=True)
            
    df.drop('Age2', axis = 1, inplace = True)


    return df
