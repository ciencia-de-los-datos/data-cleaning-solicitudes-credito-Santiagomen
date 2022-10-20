"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np
import datetime as dt
import re 

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0,inplace=True)
    #Homologación sexo
    df['sexo'] = df['sexo'].str.upper()
    #Homologación tipo emprendimiento
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.upper()
    #Idea de negocio
    df['idea_negocio'] = df['idea_negocio'].str.upper()
    df['idea_negocio'] = df['idea_negocio'].apply(lambda x : re.sub('[^a-zA-Z0-9 \n\.]', ' ', x))
    #Barrio
    df['barrio'] = df['barrio'].str.upper()
    df['barrio'] = df['barrio'].astype(str)
    df['barrio'] = df['barrio'].map(lambda x: x.replace("-",' '))
    df['barrio'] = df['barrio'].map(lambda x: x.replace("_",' '))

    #Comuna ciudadano
    df['comuna_ciudadano']=df['comuna_ciudadano'].astype(float)

    #Fechas
    a = df.loc[df['fecha_de_beneficio'].str.split("/").str[2].str.len() == 4]['fecha_de_beneficio']
    pd.to_datetime(a, format='%d/%m/%Y')
    df.loc[df['fecha_de_beneficio'].str.split("/").str[2].str.len() == 4,"fecha_de_beneficio"] = df.loc[df['fecha_de_beneficio'].str.split("/").str[2].str.len() == 4,"fecha_de_beneficio"].apply(lambda x:dt.datetime.strptime(x, "%d/%m/%Y").strftime("%Y-%m-%d"))
    df.loc[df['fecha_de_beneficio'].str.split("/").str[0].str.len() == 4,"fecha_de_beneficio"] = df.loc[df['fecha_de_beneficio'].str.split("/").str[0].str.len() == 4,"fecha_de_beneficio"].apply(lambda x:dt.datetime.strptime(x, "%Y/%m/%d").strftime("%Y-%m-%d"))

    #Linea de crédito
    df['línea_credito'] = df['línea_credito'].str.upper()
    df['línea_credito'] = df['línea_credito'].apply(lambda x : re.sub('[^a-zA-Z0-9 \n\.]', ' ', x))
    #Monto del crédito 
    df['monto_del_credito'] = df['monto_del_credito'].astype(str).str.split(".").str[0]
    df['monto_del_credito'] = df['monto_del_credito'].astype(str).apply(lambda x : re.sub('[^0-9]', '', x)).astype(int)

    df.drop_duplicates(inplace=True)
    df.dropna(axis=0,inplace=True)
    return df
