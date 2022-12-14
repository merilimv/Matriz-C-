import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#######################################################
#CASO ENTRE NESSE CÓDIGO LEIA O README.MD DESSE ARQUIVO
#######################################################

def createLineIT(cor, label, metodo, dataframe, ax):
    ticks = [0.001, 0.01, 0.05, 0.1]
    x = list(range(len(ticks)))
    y = dataframe.loc[dataframe['metodo'] == metodo].sort_values(by = ['epsilon'])
    y = y['iteracoes']
    ax.plot(x, y, marker = 'o', color = cor, label = label)

def plotIteracoes():
    fig, ax = plt.subplots(figsize = (10,8))
    dataframe = pd.read_csv("./graficosMN/metodos.csv")
    dataframe = dataframe[['epsilon', 'iteracoes', 'metodo']]
    ticks = [0.001, 0.01, 0.05, 0.1] # Poderia fazer isso dinamicamente mas como é fixo vou manter
    x = list(range(len(ticks)))
    metodos = ('GaussSeidelInverso', 'GaussSeidelNormal', 'GaussJacobiInverso', 'GaussJacobiNormal')
    nomes = ("Gauss Seidel por Inversa", "Gauss Seidel", "Gauss Jacobi por Inversa", "Gauss Jacobi")
    cores = ("r", "b", "g", "k")
    for i in range(len(metodos)):
        createLineIT(cores[i], nomes[i], metodos[i], dataframe, ax)
    ax.set_xlabel('Epsilon')
    ax.set_ylabel('Número de Iterações')
    ax.set_title('Número de Iterações para os Diferentes em Outro Exemplo')
    ax.set_xticks(x, ticks)
    ax.legend()
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    fig.savefig("./graficosMN/Gráficos/Iteracao2.png")

def createLineER(cor, label, metodo, dataframe, ax):
    ticks = [0.001, 0.01, 0.05, 0.1]
    x = list(range(len(ticks)))
    y = dataframe.loc[dataframe['metodo'] == metodo].sort_values(by = ['epsilon'])
    y = y['erromedio']
    ax.plot(x, y, marker = 'o', color = cor, label = label)
    

def plotErro():
    fig, ax = plt.subplots(figsize = (10,8))
    dataframe = pd.read_csv("./graficosMN/metodos.csv")
    dataframe = dataframe[['epsilon', 'erromedio', 'metodo']]
    ticks = [0.001, 0.01, 0.05, 0.1]
    x = list(range(len(ticks)))
    metodos = ('GaussSeidelInverso', 'GaussSeidelNormal', 'GaussJacobiInverso', 'GaussJacobiNormal')
    nomes = ("Gauss Seidel por Inversa", "Gauss Seidel", "Gauss Jacobi por Inversa", "Gauss Jacobi")
    cores = ("r", "b", "g", "k")
    for i in range(len(metodos)):
        createLineER(cores[i], nomes[i], metodos[i], dataframe, ax)
    ax.set_xlabel('Epsilon')
    ax.set_ylabel('Valor de Erro Médio')
    ax.set_title('Erro Médio de Diferentes Métodos em Outro Exemplo')
    ax.set_xticks(x, ticks)
    ax.legend()
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    fig.savefig("./graficosMN/Gráficos/Erro2.png")


plotIteracoes()
plotErro()
#cheguei num resultado próximo ao desejado.

#######################################################
#CASO ENTRE NESSE CÓDIGO LEIA O README.MD DESSE ARQUIVO
#######################################################