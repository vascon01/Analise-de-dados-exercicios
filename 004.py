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



# Sementes solicitadas no exercício


sementes = [10, 42, 100]

plt.figure(figsize=(10, 5)) #Seria a separação do espaço como se fosse uma folha branca

for semente in sementes:
    # A variável 'amostra' é criada AQUI para cada semente:
    amostra = df_G1.sample(n=len(df_G1), random_state=semente).reset_index(
        drop=True
    )
    #! Pega todas notas dos aluno numa sacola e em baralha == df_G1.samble 
    #! o n=len(df_G1) é a quantidade de papeis que eu tiro 
    #! random state seria o estilo diferente de como eu embaralho
    #! Reset index serve para deixar visível a ordem 

    # Cálculo da média acumulada
    medias_acumuladas = amostra.cumsum() / np.arange(1, len(amostra) + 1)
    
    #* amostra.cumsum() seria uma soma acumulada ou seja soma o valor do anterior com o proximo como uma bola de neve
    #* E divide pela quantidade de alunos que estrarão na fila 
    

    # Desenha a linha da semente atual
    plt.plot(
        #!Seria o eixo horizontal
        np.arange(1, len(medias_acumuladas) + 1),
        
        #!O eixo verdical
        medias_acumuladas,
        
        #!A etiqueta da linha
        label=f"Semente {semente}",
    )

# Linha da Média Populacional Real
#!Eixo x
plt.axhline(
    
    #! Meu y
    y=media_pop,
    color="r",
    linestyle="--",
    label=f"Média Populacional ({media_pop:.2f})",
)


#Texto do eixo x
plt.xlabel("Tamanho da Amostra (n)")

#Texto do eixo y
plt.ylabel("Média de G1")
plt.title("Comparação da Média Amostral Acumulada por Semente (Questão 4)")
plt.legend()

#Linha do caderno
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()