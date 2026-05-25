import pandas as pd

def data_processing(df: pd.DataFrame) -> pd.DataFrame:
    #Tratamento de colunas desnecessárias
    cols_to_drop = ['bmi_redundant', 'experience_years', 'record_created_at', 'total_macros', 'adherence_ratio']  #'experience_years' é duplicada de 'years_experience'
    df.drop(columns=cols_to_drop, inplace=True)

    # Normalização
    df['sex'] = df['sex'].str.strip().str.lower()
    gender_map = {'m': 'M', 'f': 'F', 'male': 'M', 'female': 'F'}
    df['sex'] = df['sex'].map(gender_map)

    df['approach'] = df['approach'].str.strip().str.lower()  # normalizar antes de usar a moda
    df['approach'] = df['approach'].fillna(df['approach'].mode()[0])

    df = df.dropna(subset=['weight_change_kg_6m'])

    # Limites do Domínio

    df['mean_adherence_pct'] = df['mean_adherence_pct'].clip(lower=0, upper=100)
    df['age'] = df['age'].clip(lower=16, upper=100)
    df['motivation_score'] = df['motivation_score'].clip(upper=1.0)
    df['weight_change_kg_6m'] = df['weight_change_kg_6m'].clip(lower=-40, upper=40)

    #Tratamento Nulls
    cols_median_in = ['sleep_hours', 'years_experience', 'age']
    df[cols_median_in] = df[cols_median_in].fillna(df[cols_median_in].median())

    cols_mean_in = ['motivation_score', 'motivation_score_program', 'mean_adherence_pct']
    df[cols_mean_in] = df[cols_mean_in].fillna(df[cols_mean_in].mean())

    df['sodium_limit_mg'] = df.groupby('diet_type')['sodium_limit_mg'].transform(lambda x: x.fillna(x.mean()))
    df['fiber_target_g'] = df.groupby('diet_type')['fiber_target_g'].transform(lambda x: x.fillna(x.mean()))


    #Metodo IQR (limitação)

    cols_outliers_iqr = ['sodium_limit_mg', 'fiber_target_g', 'years_experience', 'height_cm', 'baseline_weight_kg', 'sleep_hours']

    for col in cols_outliers_iqr:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        df = df[(df[col] >= limite_inferior) & (df[col] <= limite_superior)]

    return df