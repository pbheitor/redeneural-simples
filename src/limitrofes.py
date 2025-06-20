import os
from PIL import Image

def testarLimitrofes(rede, interpretarSaida):
    img_paths = [
        "data/imagens/limitrofe/quadrado_circulo_1.png",
        "data/imagens/limitrofe/quadrado_circulo_2.png",
        "data/imagens/limitrofe/quadrado_circulo_3.png",
        "data/imagens/limitrofe/triangulo_quadrado_1.png",
        "data/imagens/limitrofe/triangulo_quadrado_2.png",
        "data/imagens/limitrofe/triangulo_quadrado_3.png",
    ]

    imagem_descricao = {
        "quadrado_circulo_1.png": "Quadrado-Círculo 1",
        "quadrado_circulo_2.png": "Quadrado-Círculo 2",
        "quadrado_circulo_3.png": "Quadrado-Círculo 3",
        "triangulo_quadrado_1.png": "Triângulo-Quadrado 1",
        "triangulo_quadrado_2.png": "Triângulo-Quadrado 2",
        "triangulo_quadrado_3.png": "Triângulo-Quadrado 3"
    }

    limitrofes_esperados = {
        "quadrado_circulo_1.png": "quadrado",
        "quadrado_circulo_2.png": "quadrado",
        "quadrado_circulo_3.png": "quadrado",
        "triangulo_quadrado_1.png": "triangulo",
        "triangulo_quadrado_2.png": "triangulo",
        "triangulo_quadrado_3.png": "triangulo",
    }

    print("\n-------------------------------------------------")
    print("Iniciando o teste com imagens limitrofes...\n")

    for img_path in img_paths:
        if not os.path.exists(img_path):
            print(f"Erro: A imagem {img_path} não foi encontrada.")
            continue

        nome_img = os.path.basename(img_path)
        nome_legivel = imagem_descricao[nome_img]
        esperado = limitrofes_esperados[nome_img]

        print(f"\nProcessando a imagem limitrofe: {nome_legivel}")
        img = Image.open(img_path).convert('L').resize((10, 10))
        img_vector = [1 if p < 128 else 0 for p in img.getdata()]

        predicao = rede.calcularSaidas(img_vector)
        predicao_legivel = interpretarSaida(predicao)
        acertou = "ACERTOU!" if predicao_legivel == esperado else "ERROU."

        print(f"Probabilidades: {predicao}")
        print(f"Esperado: {esperado} | Predito: {predicao_legivel} - {acertou}")

    print("\n-------------------------------------------------\n")
