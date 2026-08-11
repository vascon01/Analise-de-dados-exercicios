import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import trim_mean

student_performance = fetch_ucirepo(id=320)
df = student_performance.data.original.copy()

# Exemplo: sua população
populacao = df_G1.to_numpy()

# Média aritmética da população
media_populacao = np.mean(populacao)

# Média aparada da população (10%)
media_aparada_populacao = trim_mean(populacao, proportiontocut=0.1)

# Guarda as médias aparadas de cada tamanho amostral
medias_aparadas = []

# Para cada tamanho de amostra
for n in range(1, len(populacao) + 1):

    # Cria uma amostra com n elementos
    amostra = populacao[:n]

    # Média aparada da amostra
    media = trim_mean(amostra, proportiontocut=0.1)

    medias_aparadas.append(media)

# Tamanhos das amostras
tamanhos = range(1, len(populacao) + 1)

# Gráfico
plt.plot(tamanhos, medias_aparadas, label="Média aparada da amostra")

# Linha da média aparada da população
plt.axhline(
    media_aparada_populacao,
    linestyle="--",
    label="Média aparada da população"
)

# Linha da média aritmética da população
plt.axhline(
    media_populacao,
    linestyle="--",
    label="Média aritmética da população"
)

plt.xlabel("Tamanho da amostra")
plt.ylabel("Média")
plt.title("Média aparada para cada tamanho amostral")
plt.legend()
plt.grid()
plt.show()