import numpy as numpy
class Regression:
    def __init__(self, w=0,b=0):
        self.w = w
        self.b = b
        
    def predict(self, x):
        y_hat = self.w*x+self.b
        return y_hat