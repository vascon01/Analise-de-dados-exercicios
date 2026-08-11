import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plotar_distribuicao_normal(dados):
    # 1. Calcula a média e o desvio padrão automaticamente dos dados
    mu = np.mean(dados)
    sigma = np.std(dados)
    
    # 2. Gera o eixo XCobrindo 4 desvios padrão para cada lado
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    y = norm.pdf(x, loc=mu, scale=sigma)
    
    # 3. Cria o gráfico
    plt.figure(figsize=(8, 5))
    
    # Histograma dos dados reais
    plt.hist(dados, density=True, alpha=0.4, color='g', label='Dados Reais')
    
    # Curva Normal Teórica
    plt.plot(x, y, color='red', linewidth=2, label=f'Curva Normal\n($\mu$={mu:.2f}, $\sigma$={sigma:.2f})')
    
    # Linha central destacando a média
    plt.axvline(mu, color='black', linestyle='--', label='Média')
    
    # Ajustes visuais
    plt.title('Distribuição Normal dos Dados')
    plt.xlabel('Valores')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.show()

# --- EXEMPLO DE USO ---
# Adicione seus valores aqui na lista:
meus_dados = [65, 70, 72, 68, 75, 80, 62, 70, 71, 69, 73, 78, 67, 70, 74]

plotar_distribuicao_normal(meus_dados)