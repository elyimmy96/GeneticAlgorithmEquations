from random import *
from functions import *
class Procedure(object):
    fitness = 0
    codigo = ""
    ytemp = 0
    def __init__(self, codigo):
        self.codigo = 'self.ytemp = {}'.format(codigo)
    def calcFitness(self):
        xar = []
        output = []
        y = []
        for i in range(0,5):
            xar.append(randint(-5,5))
        for i in range(0,5):
            x = xar[i]
            out = x**2+x+1
            output.append(out)
            exec(self.codigo)
            y.append(self.ytemp)
        print('{}-->{}\n{}-->{}'.format(xar, output, xar, y))
        for i in range(0, 5):
            self.fitness += (output[i]-y[i])**2
