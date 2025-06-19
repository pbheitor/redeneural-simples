from src.util import produtoEscalar
import random

class Neuronio:
    def __init__(self, numEntradas, taxaAprendizagem, funcaoAtivacao, derivadaAtivacao):
        
        self.pesos = [random.uniform(-0.5, 0.5) for _ in range(numEntradas)]  
        self.funcaoAtivacao = funcaoAtivacao
        self.derivadaAtivacao = derivadaAtivacao
        self.taxaAprendizagem = taxaAprendizagem
        self.saidaCache = 0.0
        self.delta = 0.0

    def calcularSaida(self, entradas):
        self.saidaCache = produtoEscalar(entradas, self.pesos)
        return self.funcaoAtivacao(self.saidaCache)