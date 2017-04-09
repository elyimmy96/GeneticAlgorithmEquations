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
