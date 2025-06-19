from PIL import Image, ImageDraw
import os

def salvarImagemQuadrado(nome):
    img = Image.new('L', (10, 10), color=255)
    draw = ImageDraw.Draw(img)
    draw.rectangle([2,2,7,7], fill=0)  # quadrado preto centralizado
    img.save(nome)

def salvarImagemCirculo(nome):
    img = Image.new('L', (10, 10), color=255)
    draw = ImageDraw.Draw(img)
    draw.ellipse([2,2,7,7], fill=0)   # círculo preto centralizado
    img.save(nome)

def salvarImagemTriangulo(nome):
    img = Image.new('L', (10, 10), color=255)
    draw = ImageDraw.Draw(img)
    draw.polygon([ (5,2), (2,7), (7,7) ], fill=0) # triângulo preto
    img.save(nome)

def gerarTodas():
    os.makedirs("data/imagens/quadrado", exist_ok=True)
    os.makedirs("data/imagens/circulo", exist_ok=True)
    os.makedirs("data/imagens/triangulo", exist_ok=True)
    # mudar range, gera +
    for i in range(10):
        salvarImagemQuadrado(f"data/imagens/quadrado/q_{i}.png")
        salvarImagemCirculo(f"data/imagens/circulo/c_{i}.png")
        salvarImagemTriangulo(f"data/imagens/triangulo/t_{i}.png")

if __name__ == "__main__":
    gerarTodas()
    print("Imagens geradas em data/imagens/")