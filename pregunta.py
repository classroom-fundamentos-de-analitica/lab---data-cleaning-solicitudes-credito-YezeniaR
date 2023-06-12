"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df = df.drop_duplicates()
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(inplace = True)

    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']: #['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']:
        df[columna] = df[columna].apply(lambda x: x.lower()) 

    df["monto_del_credito"] = df["monto_del_credito"].str.replace("[^0-9]", "", regex=True)
    df["línea_credito"] = df["línea_credito"].str.lower()

    df = df.dropna()

    return df
