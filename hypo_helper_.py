import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading function
def load_data(path, columns):
    data = pd.read_csv(path, usecols = columns)
    return data

# pivoting dataframe
def pivot(dataframe):
    student_tests = dataframe.pivot_table(
        index = 'StudentIdentifier', 
        columns = 'AssessmentName', 
        values = 'ScaleScoreAchievementLevel', 
        aggfunc = 'max'
    ).reset_index()
    
    data = pd.merge(dataframe, student_tests, on = 'StudentIdentifier')

    data = data.drop(['AssessmentName', 'ScaleScoreAchievementLevel'], axis = 1)
    data = data.drop_duplicates(subset=['StudentIdentifier'])
    return data

# coalesce interest scores
def singular_ela_column(dataframe):
    dataframe = dataframe.copy()
    dataframe['ELA Summative'] = (dataframe['ELA Summative Grade 11'].
        combine_first(dataframe['ELA Summative Grade 6']).
        combine_first(dataframe['ELA Summative Grade 7']).
        combine_first(dataframe['ELA Summative Grade 8'])
                            )
    ELA_cols = ['ELA Summative Grade 11',
              'ELA Summative Grade 6',
              'ELA Summative Grade 7',
              'ELA Summative Grade 8']

    dataframe = dataframe.drop(ELA_cols, axis = 1)
    dataframe = dataframe.dropna(subset = ['ELA Summative'])
    return dataframe

# subset columns for analysis
def get_interest_column(df, list):
    analysis_data = df[list].copy()
    analysis_data = analysis_data.dropna(subset = ['ELA Summative Grade 8'])
    return analysis_data

# define boolean statuses
def make_exposed(df, column):
    df = df.copy()
    df.loc[:,'exposed'] = df[column].notna()
    return df

def get_pass_fail(df, column):
    df = df.copy()
    df.loc[:, 'pass'] = df[column] >= 3.0
    return df

