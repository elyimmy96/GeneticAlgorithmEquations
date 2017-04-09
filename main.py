from functions import *
from classes import *
import variables

variables.init()
for i in range(0,variables.populationSize):
    variables.codigo=""
    variables.curDepth=-1
    generateProcedure()
    procedure = Procedure(variables.codigo)
    procedure.calcFitness()
    variables.population.append(procedure)
    print('{}\n{}\t{}'.format(i, variables.population[i].fitness, variables.population[i].codigo))
