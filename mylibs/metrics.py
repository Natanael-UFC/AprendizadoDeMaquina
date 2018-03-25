import numpy as np

# Função responsavel por calcular a taxa de erro MSE de um modelo
def mse(y_true, y_pred):
    return np.sum((y_true - y_pred) ** 2) / len(y_true)

# Função que calcula a taxa de erro RMSE(raiz quadrada do MSE) de um modelo
def rmse(y_true, y_pred):
    return np.sqrt(mse(y_true, y_pred))

# Função que calcula o erro absoluto de um modelo
def mae(y_true, y_pred):
    return np.sum(np.abs(y_true - y_pred)) / len(y_true)