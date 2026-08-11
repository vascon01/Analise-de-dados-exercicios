import statistics


def media(x):
    return statistics.mean(x)


def mediana(x):
    return statistics.median(x)


def dam(x):
    m = statistics.mean(x)
    return sum(abs(i - m) for i in x) / len(x)


# Conjuntos de dados
A = [4, 5, 6, 7, 8]
B = [0, 5, 6, 7, 12]

# Exibição dos resultados organizados
print("--- CONJUNTO A ---")
print(f"Média: {media(A)}")
print(f"Mediana: {mediana(A)}")
print(f"Desvio Absoluto Médio (DAM): {dam(A):.1f}\n")

print("--- CONJUNTO B ---")
print(f"Média: {media(B)}")
print(f"Mediana: {mediana(B)}")
print(f"Desvio Absoluto Médio (DAM): {dam(B):.1f}")