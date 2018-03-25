import numpy as np
from mylibs import stats

class SimpleLinearRegression(object):
    b1 = None 
    b0 = None
    
    def __init__(self):
        self.b1 = 0
        self.b0 = 0
        
    def fit(self, X, y):
        self.b1 = np.sum((X - stats.mean(X)) * (y - stats.mean(y))) / np.sum((X - stats.mean(X)) ** 2)
        self.b0 = stats.mean(y) - self.b1 * stats.mean(X)
        
    def predict(self, X):
        pred = []
        for i in range(len(X)):
            pred.append(self.b1 * X[i] + self.b0)
        return np.array(pred)
        
        