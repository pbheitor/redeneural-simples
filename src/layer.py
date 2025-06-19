from src.neuron import Neuronio
import random

class Camada:
    def __init__(self, camadaAnterior, numNeuronios, taxaAprendizagem, funcaoAtivacao, derivadaAtivacao):
        self.camadaAnterior = camadaAnterior
        self.neuronios = []
        
        
        for _ in range(numNeuronios):
            if camadaAnterior is None:
                pesos = []  
            else:
                
                pesos = [random.uniform(-0.5, 0.5) for _ in range(len(camadaAnterior.neuronios))]
            
            
            neuronio = Neuronio(len(camadaAnterior.neuronios) if camadaAnterior else 0, taxaAprendizagem, funcaoAtivacao, derivadaAtivacao)
            self.neuronios.append(neuronio)

        
        self.saidasCache = [0.0 for _ in range(numNeuronios)]

    def calcularSaidas(self, entradas):
        if self.camadaAnterior is None:
            self.saidasCache = entradas
        else:
            self.saidasCache = [n.calcularSaida(entradas) for n in self.neuronios]
        return self.saidasCache

    def calcularDeltasSaida(self, esperados):
        for i in range(len(self.neuronios)):
            self.neuronios[i].delta = self.neuronios[i].derivadaAtivacao(self.neuronios[i].saidaCache) * (esperados[i] - self.saidasCache[i])

    def calcularDeltasOculta(self, proximaCamada):
        for idx, neuronio in enumerate(self.neuronios):
            pesosProx = [n.pesos[idx] for n in proximaCamada.neuronios]
            deltasProx = [n.delta for n in proximaCamada.neuronios]
            soma = sum(p * d for p, d in zip(pesosProx, deltasProx))
            neuronio.delta = neuronio.derivadaAtivacao(neuronio.saidaCache) * soma
