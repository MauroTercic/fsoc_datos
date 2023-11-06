import matplotlib.pyplot as plt
import pandas as pd
from preprocesamiento import dropping_columns



FILE = "data\worlddata.csv"

df = pd.read_csv(FILE)

'''
Empece eliminando las columnas que no tenian una incidencia estadisticamente relevante para entender el PBI (GDP)
Para eso cree un script adaptable que importe 
También elimine 3 paises que tenian demasiados datos faltantes

'''

def preprocess():
    dropping_columns(FILE) 


# Visualización de los datos

def scatter_1():
    y = df["gdp_capita"]
    plt.ylabel("GDP per Capita")
    x = df["unemployment_rate"]
    plt.xlabel("Unemployment Rate")
    n = df["country"]
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))

    plt.show()



def scatter_2():
    y = df["gdp_capita"]
    plt.ylabel("GDP per Capita")
    x = df["life_expectancy"]
    plt.xlabel("life_expectancy")
    n = df["country"]
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))

    plt.show()

