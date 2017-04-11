def init():
    global depth
    depth = 2
    global curDepth
    curDepth = -1
    global codigo
    codigo = ""
    global funciones
    funciones = ["s","r","m","d"]
    global funcionesConstantes
    funcionesConstantes = ["s", "r", "m","d", "x", "rand"]
    global constantes
    constantes = ["x", "rand"]
    global population
    population = []
    global populationSize
    populationSize = 10
    global curGen
    curGen = 0
    global generations
    generations = 3
    global newGen
    newGen = []
