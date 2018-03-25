import numpy as np

#Função para calcular a media de um array
def mean(x):
    return np.sum(x) / len(x)
    
#Função para calcular o desvio padrão de um array
def stdev(x):
    media = mean(x)
    variancia = np.sum((x - media) ** 2) / len(x)
    return np.sqrt(variancia)

#Função para calcular a variancia de um array
def var(y):
    media = mean(y)
    return np.sum((y - media) ** 2) / len(y)