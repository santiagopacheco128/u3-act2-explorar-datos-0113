# importar libretas
import pandas as pd
import numpy as np

print("Analisis de datos de autos Santiago Pacheco 0113")

automoviles = {
    "Id_Automovil": ["A001", "A002", "A003", "A004", "A005", "A006"],
    "Precio": [250000, 850000, 220000, 450000, 280000, 650000],
    "Marca": ["Toyota", "Ford", "Nissan", "Toyota", "Chevrolet", "Ford"],
    "Es_Usado": [False, True, True, False, True, False]
}

df = pd.DataFrame(automoviles)
print(df)

print("+-+-+- agrupar columnas +-+-+-+")
agrupado = df.groupby("Marca")
print(agrupado)

print("---- por agregacion ----")

# Precio promedio por marca
print(agrupado["Precio"].mean())


# Precio maximo por marca
print(agrupado["Precio"].max())