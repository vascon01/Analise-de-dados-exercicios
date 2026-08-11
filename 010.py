import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo


# Carrega os dados
student_performance = fetch_ucirepo(id=320)
df = student_performance.data.original.copy()

# Dados originais
G1 = df["G1"]

# Cria uma cópia e contamina o primeiro valor
G1_contaminada = G1.copy()
G1_contaminada.loc[0] = 100



resultados = pd.DataFrame({
    "Original": [
        np.mean(G1),
        np.median(G1),
        np.mean(np.abs(G1 - np.mean(G1))),
        np.median(np.abs(G1 - np.median(G1))),
        np.mean((G1 - np.mean(G1)) ** 2),
        np.sqrt(np.mean((G1 - np.mean(G1)) ** 2))
    ],

    "Contaminada": [
        np.mean(G1_contaminada),
        np.median(G1_contaminada),
        np.mean(np.abs(G1_contaminada - np.mean(G1_contaminada))),
        np.median(np.abs(G1_contaminada - np.median(G1_contaminada))),
        np.mean((G1_contaminada - np.mean(G1_contaminada)) ** 2),
        np.sqrt(np.mean((G1_contaminada - np.mean(G1_contaminada)) ** 2))
    ]
}, index=[
    "Média",
    "Mediana",
    "Desvio absoluto médio",
    "Desvio absoluto mediano",
    "Variância",
    "Desvio padrão"
])

print(resultados.round(2))