"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    columns_to_lower = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']
    characters_to_replace = ['_', '-']
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    for column in columns_to_lower:
        df[column] = df[column].str.lower()
        for character in characters_to_replace:
            df[column] = df[column].str.replace(character, ' ')

    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: int(re.sub(r'[\$,\.]', '', x)))
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format="%Y/%m/%d", errors='coerce')
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    return df
