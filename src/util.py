from math import exp

def produtoEscalar(xs, ys):
    return sum(x * y for x, y in zip(xs, ys))

def sigmoide(x):
    return 1 / (1 + exp(-x))

def derivadaSigmoide(x):
    s = sigmoide(x)
    return s * (1 - s)

def normalizarPorCaracteristica(dataset):
    for col in range(len(dataset[0])):
        colVals = [row[col] for row in dataset]
        minVal, maxVal = min(colVals), max(colVals)
        for row in dataset:
            row[col] = (row[col] - minVal) / (maxVal - minVal)