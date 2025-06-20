from src.dataset_imagem import carregarDatasetImagens
from src.network import RedeNeural
import random

def interpretarSaida(saida):
    if max(saida) == saida[0]:
        return "quadrado"
    elif max(saida) == saida[1]:
        return "circulo"
    else:
        return "triangulo"

def treinarRedeParaTestes():
    X, y = carregarDatasetImagens("data/imagens")
    temp = list(zip(X, y))
    random.shuffle(temp)
    X, y = zip(*temp)
    X, y = list(X), list(y)
    n_treino = int(0.8 * len(X))
    X_treino, y_treino = X[:n_treino], y[:n_treino]
    rede = RedeNeural([100, 15, 3], 0.3)
    for _ in range(400):
        rede.treinar(X_treino, y_treino)
    print(f"\nRede treinada com {len(X_treino)} imagens de treino.\n")
    return rede

def treinarRedeImagens():
    
    from src.limitrofes import testarLimitrofes

    X, y = carregarDatasetImagens("data/imagens")
    temp = list(zip(X, y))
    random.shuffle(temp)
    X, y = zip(*temp)
    X, y = list(X), list(y)

    n_treino = int(0.8 * len(X))  # 80% treino
    X_treino, y_treino = X[:n_treino], y[:n_treino]
    X_teste, y_teste = X[n_treino:], y[n_treino:]

    vetor_para_nome = {(1,0,0):"quadrado", (0,1,0):"circulo", (0,0,1):"triangulo"}
    nomes_esperados = [vetor_para_nome[tuple(label)] for label in y_teste]

    print("Iniciando treinamento da rede neural para reconhecer formas geométricas em imagens 10x10.")
    print(f"Serão usados {len(X_treino)} imagens para treino e {len(X_teste)} para teste.")
    print("O programa irá mostrar o esperado, o predito e se a rede acertou cada imagem de teste.\n")

    rede = RedeNeural([100, 15, 3], 0.3)
    for _ in range(400):
        rede.treinar(X_treino, y_treino)

    corretos = 0
    print("Resultados dos testes:")
    for i, (entrada, esperado) in enumerate(zip(X_teste, nomes_esperados)):
        saida = rede.calcularSaidas(entrada)
        predito = interpretarSaida(saida)
        certo = "ACERTOU!" if predito == esperado else "ERROU."
        print(f"Teste {i+1:02d}: Esperado: {esperado:9s} | Predito: {predito:9s} {certo}")
        if predito == esperado:
            corretos += 1

    total = len(X_teste)
    percentual = corretos / total * 100

    print(f"\nA rede neural acertou {corretos} de {total} imagens de teste ({percentual:.2f}%).")
    if percentual >= 80:
        print("Ótimo desempenho! A rede está generalizando bem.")
    elif percentual >= 50:
        print("Desempenho razoável, mas pode melhorar com mais dados ou mais treino.")
    else:
        print("A rede ainda está aprendendo. Experimente aumentar as épocas ou gerar mais exemplos.")

    
    print("\nAgora, testando novamente nos casos limitrofes com a rede treinada...")
    testarLimitrofes(rede, interpretarSaida)

    resposta = input("\nDeseja rodar o teste novamente? (s/n): ").strip().lower()
    if resposta == 's':
        print("\nReiniciando teste...\n")
        treinarRedeImagens()
    else:
        print("Encerrando programa.")
