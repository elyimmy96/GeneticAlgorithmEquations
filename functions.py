from random import *
import variables

def s(a, b):
    res = a+b
    return res
def r(a, b):
    res = a-b
    return res
def m(a, b):
    res = a*b
    return res
def d(a, b):
    if(b != 0):
        res = a/b
    else:
        res = 1
    return res

def generateProcedure():
    variables.curDepth += 1
    if(variables.curDepth < 2):
        r = variables.funcionesConstantes[randint(0,5)]
        if(r == "rand"):
            r = randint(0,5)
        variables.codigo += str(r)
        #print(variables.codigo)
        if(r in variables.funciones):
            variables.codigo += "("
            generateProcedure()
        if(variables.curDepth == 0):
            #print(variables.codigo)
            return
        else:
            variables.codigo += ","
            r = variables.funcionesConstantes[randint(0,5)]
            if(r == "rand"):
                r = randint(0,5)
            variables.codigo += str(r)
            #print(variables.codigo)
            if(r in variables.funciones):
                variables.codigo += "("
                generateProcedure()
            variables.curDepth -= 1
            variables.codigo += ")"
            return
    else:
        r = variables.constantes[randint(0,1)]
        if(r == "rand"):
            r = randint(0,5)
        variables.codigo += str(r)
        variables.codigo += ","
        r = variables.constantes[randint(0,1)]
        if(r == "rand"):
            r = randint(0,5)
        variables.codigo += str(r)
        variables.curDepth -= 1
        variables.codigo += ")"
        (variables.codigo)
        return

def getParent():
    temp =[]
    parent = Procedure("")
    for i in range(0,3):
        temp.append(variables.population[randint(0, variables.populationSize-1)])
    for i in range(0,3):
        print('{}-->{}'.format(i, temp[i].fitness))
        if(temp[i].fitness > parent.fitness):
            parent = temp[i]
    return parent

def reproduce(parent):
    variables.newGen.append(parent)

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
        if(self.fitness == 0):
            variables.solution = self
            return
        self.fitness = 1./self.fitness
