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
    
    # Se eliminan NaN y duplicados
    df.dropna(axis=0, inplace=True)
    df.drop_duplicates(inplace=True)

    # Se pasa a minúscula la columna sexo, de esta forma solo quedan dos posibles valores
    columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']
    df[columns] = df[columns].apply(lambda x: x.str.lower())

    # Se depuran las columnas idea_negocio, barrio, eliminando los caracteres especiales
    characters = ['_', '-']
    df[columns] = df[columns].apply(lambda x: x.replace(characters, ' '))

    # Se eliminan los símbolos y se convierte a entero la columna monto_del_credito
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(r'\$|,|\.\d+', '', regex=True).astype(int)
    
    # Se convierte a flotante la columna comuna_ciudadano
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    # Se convierte la columna fecha_de_beneficio al formato adecuado
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    # Se eliminan NaN y duplicados nuevamente
    df.dropna(axis=0, inplace=True)
    df.drop_duplicates(inplace=True)

    return df
