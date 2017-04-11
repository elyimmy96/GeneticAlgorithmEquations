from functions import *
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
print('Generation: {}'.format(variables.curGen))
for i in range(0, variables.populationSize):
    print('{}\t{}'.format(i,variables.population[i].codigo))
input("Press to continue")
for j in range(0, variables.generations):

    for i in range(0, variables.populationSize):
        parent = getParent()
        #Aqui debemos generar un numero aleatorio para ver si copiar a siguiente generacion, mutar o mezclar dos padres

        #Hay que revisar porcentajes, propongo:
        # 65%   -->    Crossover
        # 5%    -->    Mutacion
        # 30%   -->    Reproduccion
        #----------------------------
        # 100%  -->    Total
        reproduce(parent) #Esta funcion copia a la siguiente generacion
        print('Parent-->{}'.format(parent.fitness))
    variables.curGen += 1
    variables.population = variables.newGen
    variables.newGen = []
    print('Generation: {}'.format(variables.curGen))
    for i in range(0, variables.populationSize):
        print('{}\t{}'.format(i,variables.population[i].codigo))
    input("Press to continue")
