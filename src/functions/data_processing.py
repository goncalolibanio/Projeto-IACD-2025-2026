import pandas as pd
import numpy as np


def data_processing(df: pd.DataFrame) -> pd.DataFrame:
    #Tratamento de colunas desnecessárias
    cols_to_drop = ['bmi_redundant', 'experience_years', 'record_created_at', 'total_macros', 'adherence_ratio']  #'experience_years' é duplicada de 'years_experience'
    df.drop(columns=cols_to_drop, inplace=True)

    #Tratamento Nulls
    cols_median_in = ['sleep_hours', 'years_experience', 'age']
    df[cols_median_in] = df[cols_median_in].fillna(df[cols_median_in].median())

    cols_mean_in = ['motivation_score', 'motivation_score_program', 'mean_adherence_pct']
    df[cols_mean_in] = df[cols_mean_in].fillna(df[cols_mean_in].mean())

    df['approach'] = df['approach'].str.strip().str.lower() #normalizar antes de usar a moda
    df['approach'] = df['approach'].fillna(df['approach'].mode()[0])

    df['sodium_limit_mg'] = df.groupby('diet_type')['sodium_limit_mg'].transform(lambda x: x.fillna(x.mean()))
    df['fiber_target_g'] = df.groupby('diet_type')['fiber_target_g'].transform(lambda x: x.fillna(x.mean()))

    df = df.dropna(subset=['weight_change_kg_6m'])

    #Normalização
    df['sex'] = df['sex'].str.strip().str.lower()
    gender_map = {'m': 'M', 'f': 'F', 'male': 'M', 'female': 'F'}
    df['sex'] = df['sex'].map(gender_map)

    float_cols = df.select_dtypes(include='float').columns
    df[float_cols] = df[float_cols].round(3)

    return df
