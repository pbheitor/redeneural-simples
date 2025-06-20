from src.treinar_imagem import treinarRedeImagens
from src.limitrofes import gerarImagensLimitrofes, testarLimitrofes

def executarTeste():
    # Primeiro, testes com imagens limitrofes
    print("Primeiro, os testes limitrofes...\n")
    gerarImagensLimitrofes()  # Gerar as imagens limitrofes
    testarLimitrofes()         # Testar as imagens limitrofes

    # Agora, testes com formas geométricas normais
    print("\nAgora, o teste normal...\n")
    treinarRedeImagens()      # Treinamento da rede e avaliação das imagens normais

if __name__ == "__main__":
    executarTeste()  # Chama a função que executa os testes