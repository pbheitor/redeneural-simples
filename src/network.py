from src.layer import Camada
from src.util import sigmoide, derivadaSigmoide
from functools import reduce

class RedeNeural:
    
    def __init__(self, estruturaCamadas, taxaAprendizagem, funcaoAtivacao=sigmoide, derivadaAtivacao=derivadaSigmoide):
        if len(estruturaCamadas) < 3:
            raise ValueError("A rede precisa de ao menos 3 camadas (entrada, oculta, saída)")
        self.camadas = []
        camadaEntrada = Camada(None, estruturaCamadas[0], taxaAprendizagem, funcaoAtivacao, derivadaAtivacao)
        self.camadas.append(camadaEntrada)
        for i, numNeuronios in enumerate(estruturaCamadas[1:]):
            novaCamada = Camada(self.camadas[i], numNeuronios, taxaAprendizagem, funcaoAtivacao, derivadaAtivacao)
            self.camadas.append(novaCamada)


    def calcularSaidas(self, entrada):
        return reduce(lambda entradas, camada: camada.calcularSaidas(entradas), self.camadas, entrada)


    def retropropagar(self, esperado):
        ultima = len(self.camadas) - 1
        self.camadas[ultima].calcularDeltasSaida(esperado)
        for l in range(ultima - 1, 0, -1):
            self.camadas[l].calcularDeltasOculta(self.camadas[l + 1])


    def atualizarPesos(self):
        for camada in self.camadas[1:]:
            for neuronio in camada.neuronios:
                for w in range(len(neuronio.pesos)):
                    neuronio.pesos[w] += neuronio.taxaAprendizagem * camada.camadaAnterior.saidasCache[w] * neuronio.delta


    def treinar(self, entradas, esperados):
        for i, xs in enumerate(entradas):
            ys = esperados[i]
            self.calcularSaidas(xs)
            self.retropropagar(ys)
            self.atualizarPesos()


    def validar(self, entradas, esperados, interpretarSaida):
        corretos = 0
        for entrada, esperado in zip(entradas, esperados):
            resultado = interpretarSaida(self.calcularSaidas(entrada))
            if resultado == esperado:
                corretos += 1
        percentual = corretos / len(entradas)
        return corretos, len(entradas), percentual