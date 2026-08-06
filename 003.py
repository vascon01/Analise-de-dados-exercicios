import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo

# 1. Importação dos dados
student_performance = fetch_ucirepo(id=320)
df = student_performance.data.original.copy()

# Correção 1: Filtrar apenas estudantes da escola GP
df_GP = df[df["school"] == "GP"]
df_G1 = df_GP["G1"]


def main():
    media_pop = questao_3_a()
    amostra = questao_3_b()
    medias_acumuladas = questao_3_c(amostra)
    
    print(f"A média populacional de G1 (GP): {media_pop:.2f}")
    print("-" * 50)

    # Gera o gráfico com os dados e a média populacional real
    questao_3_d(medias_acumuladas, media_pop)


def questao_3_a():
    return df_G1.mean()


def questao_3_b():
    # Embaralha a população GP
    return df_G1.sample(n=len(df_G1), random_state=2004).reset_index(
        drop=True
    )


def questao_3_c(amostra_embaralhada):
    # Correção 2: Uso de cumsum para eficiência O(N)
    soma_acumulada = amostra_embaralhada.cumsum()
    tamanho_n = np.arange(1, len(amostra_embaralhada) + 1)
    return soma_acumulada / tamanho_n


def questao_3_d(medias_acumuladas, media_pop):
    # Correção 3: Gráfico de linhas com tamanho da amostra no eixo X e médias no eixo Y
    tamanho_amostra = np.arange(1, len(medias_acumuladas) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(
        tamanho_amostra,
        medias_acumuladas,
        label="Média Amostral Acumulada",
        color="b",
    )
    plt.axhline(
        y=media_pop,
        color="r",
        linestyle="--",
        label=f"Média Populacional ({media_pop:.2f})",
    )

    plt.xlabel("Tamanho da Amostra (n)")
    plt.ylabel("Média de G1")
    plt.title("Convergência da Média Amostral (Escola GP)")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.show()


main()