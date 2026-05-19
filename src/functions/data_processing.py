import pandas as pd
import numpy as np


def data_processing(df: pd.DataFrame) -> pd.DataFrame:
    #Tratamento de colunas desnecessárias
    cols_to_drop = ['bmi_redundant', 'experience_years', 'record_created_at', 'total_macros', 'adherence_ratio']  #'experience_years' é duplicada de 'years_experience'
    df.drop(columns=cols_to_drop, inplace=True)