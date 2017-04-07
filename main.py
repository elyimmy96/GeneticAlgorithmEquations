from functions import *
from classes import *
import variables

variables.init()
for i in range(0,variables.populationSize):
    variables.codigo=""
    variables.curDepth=-1
    generateProcedure()
    variables.population.append(variables.codigo)
    print('{}-->{}'.format(i, variables.population[i]))
