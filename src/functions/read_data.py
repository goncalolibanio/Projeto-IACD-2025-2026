import pandas as pd

def read_data():

    df_diets = pd.read_csv('data/diets.csv')
    df_nutritionists = pd.read_csv('data/nutritionists.csv')
    df_outcomes = pd.read_csv('data/outcomes.csv')
    df_patients = pd.read_csv('data/patients.csv')

    # Integrar os dados usando a tabela 'outcomes' como base
    df_merged = df_outcomes.merge(df_patients, on='patient_id', how='left')

    # Juntar dados dos nutricionistas
    df_merged = df_merged.merge(df_nutritionists, on='patient_id', how='left')

    # juntar dados das dietas
    df_merged = df_merged.merge(df_diets, on='diet_id', how='left')

    # Guardar o dataset unido num novo ficheiro CSV
    df_merged.to_csv('data/processed/integrated_dataset.csv', index=False)

