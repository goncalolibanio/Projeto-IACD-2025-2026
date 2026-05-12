import pandas as pd

def read_data():
    df_diets = pd.read_csv('../../data/diets.csv')
    df_nutritionists = pd.read_csv('../../data/nutritionists.csv')
    df_outcomes = pd.read_csv('../../data/outcomes.csv')
    df_patients = pd.read_csv('../../data/patients.csv')
    return df_diets, df_nutritionists, df_outcomes, df_patients

