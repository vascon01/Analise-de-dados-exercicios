import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo

# 1. Carrega os dados na nova aba
student_performance = fetch_ucirepo(id=320)
df = student_performance.data.original.copy()

# 2. População de notas G1 da escola GP
df_GP = df[df["school"] == "GP"]
df_G1 = df_GP["G1"]
media_pop = df_G1.mean()


lista=[]
for i in range(1000):
    amostra=df["G1"].sample(n=50).mean()
    lista.append(amostra)
    
media_media=np.mean(lista)

resultado=media_media-media_pop

plt.hist(lista, bins=30, edgecolor='black', alpha=0.7)

plt.axvline(x=media_pop, color='red', linestyle='--', label=f'Média Pop. ({media_pop:.2f})')

plt.axvline(x=media_media,color="green",linestyle="--",label=f"Média das médias.({media_media:.2f})")

plt.xlabel('Média Amostral de G1 (n=50)')
plt.ylabel('Frequência')
plt.title('Histograma das Médias Amostrais (Simulação de Monte Carlo)')
plt.legend()
plt.grid(True, alpha=0.3)

# 5. Exibe o gráfico
plt.show()