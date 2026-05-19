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

    #Limites do Domínio

    df['mean_adherence_pct'] = df['mean_adherence_pct'].clip(lower=0, upper=100)
    df['age'] = df['age'].clip(lower=16, upper=100)
    df['sleep_hours'] = df['sleep_hours'].clip(lower=2, upper=15)

    #Metodo IQR (limitação)

    cols_outliers_iqr = ['sodium_limit_mg', 'fiber_target_g', 'years_experience']

    for col in cols_outliers_iqr:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        df[col] = df[col].clip(lower=limite_inferior, upper=limite_superior)

    return df

