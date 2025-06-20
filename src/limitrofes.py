# limitrofes.py
from PIL import Image, ImageDraw
from src.network import RedeNeural
import os 

def gerarImagensLimitrofes():
    
    print("\nGerando mais imagens limitrofes...\n")

    os.makedirs('data/imagens/limitrofe', exist_ok=True)

    for i in range(7, 13):  
        img = Image.new('L', (10, 10), color=255)
        draw = ImageDraw.Draw(img)
        
        if i == 7:  
            draw.rectangle([2, 2, 8, 8], fill=0, outline=0, width=2)
            img.save(f'data/imagens/limitrofe/quadrado_circulo_4.png')
            print(f"Imagem salva: quadrado_circulo_4.png")
        
        elif i == 8:  
            draw.polygon([(2, 8), (8, 8), (5, 3)], fill=0)
            img.save(f'data/imagens/limitrofe/triangulo_quadrado_4.png')
            print(f"Imagem salva: triangulo_quadrado_4.png")
        
        elif i == 9:  
            draw.ellipse([2, 2, 8, 8], fill=0)
            img.save(f'data/imagens/limitrofe/quadrado_circulo_5.png')
            print(f"Imagem salva: quadrado_circulo_5.png")

        elif i == 10:  
            draw.polygon([(2, 8), (8, 8), (5, 2)], fill=0)
            img.save(f'data/imagens/limitrofe/triangulo_quadrado_5.png')
            print(f"Imagem salva: triangulo_quadrado_5.png")
        
        elif i == 11:  
            draw.ellipse([2, 2, 8, 8], fill=0)
            draw.polygon([(5, 2), (2, 7), (7, 7)], fill=255)
            img.save(f'data/imagens/limitrofe/circulo_triangulo_1.png')
            print(f"Imagem salva: circulo_triangulo_1.png")
        
        else: 
            draw.polygon([(5, 2), (2, 7), (8, 7)], fill=0)
            img.save(f'data/imagens/limitrofe/triangulo_circulo_2.png')
            print(f"Imagem salva: triangulo_circulo_2.png")

    print("Novas imagens limitrofes geradas!")

def interpretarSaida(saida):
    
    formas = ["quadrado", "circulo", "triangulo"]
    indice_max = saida.index(max(saida))
    return formas[indice_max]

imagem_descricao = {
    "quadrado_circulo_1.png": "Quadrado-Círculo 1",
    "quadrado_circulo_2.png": "Quadrado-Círculo 2",
    "quadrado_circulo_3.png": "Quadrado-Círculo 3",
    "triangulo_quadrado_1.png": "Triângulo-Quadrado 1",
    "triangulo_quadrado_2.png": "Triângulo-Quadrado 2",
    "triangulo_quadrado_3.png": "Triângulo-Quadrado 3"
}

def testarLimitrofes():
    
    img_paths = [
        "data/imagens/limitrofe/quadrado_circulo_1.png",
        "data/imagens/limitrofe/quadrado_circulo_2.png",
        "data/imagens/limitrofe/quadrado_circulo_3.png",
        "data/imagens/limitrofe/triangulo_quadrado_1.png",
        "data/imagens/limitrofe/triangulo_quadrado_2.png",
        "data/imagens/limitrofe/triangulo_quadrado_3.png",
    ]
    
    print("\n-------------------------------------------------")
    print("Iniciando o teste com imagens limitrofes...\n")
    
   
    rede = RedeNeural([100, 15, 3], 0.3)
    
    for img_path in img_paths:
        
        if not os.path.exists(img_path):
            print(f"Erro: A imagem {img_path} não foi encontrada.")
            continue
        
        nome_legivel = imagem_descricao[os.path.basename(img_path)]
        
        print(f"\nProcessando a imagem limitrofe: {nome_legivel}")
        img = Image.open(img_path).convert('L').resize((10, 10))
        img_vector = [1 if p < 128 else 0 for p in img.getdata()]
        
       
        predicao = rede.calcularSaidas(img_vector)  
        
        predicao_legivel = interpretarSaida(predicao)
        esperado = "quadrado" 
        acertou = "ACERTOU!" if predicao_legivel == esperado else "ERROU."
        
        print(f"Probabilidades: {predicao}")
        print(f"Esperado: {esperado} | Predito: {predicao_legivel} - {acertou}")
    
    print("\n-------------------------------------------------\n")
