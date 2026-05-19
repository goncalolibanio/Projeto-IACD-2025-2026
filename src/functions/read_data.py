import pandas as pd

def read_data():
    try:
        df_diets = pd.read_csv("data/diets.csv")
        df_nutritionists = pd.read_csv("data/nutritionists.csv")
        df_outcomes = pd.read_csv("data/outcomes.csv")
        df_patients = pd.read_csv("data/patients.csv")

        #MERGES
        df_merged = pd.merge(df_outcomes, df_patients, on='patient_id', how='left')
        df_merged1 = pd.merge(df_merged, df_diets, on='diet_id', how='left')
        df_merged_final = pd.merge(df_merged1, df_nutritionists, on='nutritionist_id', how='left')

        return df_merged_final

    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a integração: {e}")