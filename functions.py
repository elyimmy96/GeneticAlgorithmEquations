from random import *
import variables

def sum(a, b):
    return a+b

def resta(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    if(b != 0):
        return a/b
    else:
        return 1

def fitness(output, x):
    y = x**2+x+1
    return (output-y)**2

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
