from src.treinar_imagem import treinarRedeParaTestes, treinarRedeImagens, interpretarSaida
from src.limitrofes import testarLimitrofes
from src.network import RedeNeural

def executarTeste():
    print("Primeiro, teste com rede NÃO treinada (só pra comparar)...")
    rede_vazia = RedeNeural([100, 15, 3], 0.3)
    testarLimitrofes(rede_vazia, interpretarSaida)
    
    print("\nAgora, treino normal + testes padrões e limitrofes COM rede treinada...\n")
    
    treinarRedeImagens()

    
    rede_treinada = treinarRedeParaTestes()  
    testarLimitrofes(rede_treinada, interpretarSaida)

    print("\nTestes completos.")

if __name__ == "__main__":
    executarTeste()
