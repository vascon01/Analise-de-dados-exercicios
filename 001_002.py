import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo


student_performance = fetch_ucirepo(id=320)
df = student_performance.data.original.copy()

def main():
    questao_um()
    #questao_dois()
    pass
    
        
def questao_um():
    return print(f"Numero de linhas: {df.shape[0]} \nNumero de colunas: {df.shape[1]}")

def questao_dois():
    return print(df.isna().sum())
    


main()
