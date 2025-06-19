import os
from PIL import Image

def imagemParaVetor(path):
    img = Image.open(path).convert('L').resize((10, 10))
    return [1 if p < 128 else 0 for p in img.getdata()]  # 1=preto, 0=branco

def carregarDatasetImagens(pastaBase):
    X, y = [], []
    rotulos = {'quadrado':[1,0,0], 'circulo':[0,1,0], 'triangulo':[0,0,1]}
    for classe in rotulos.keys():
        pasta = os.path.join(pastaBase, classe)
        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.endswith('.png'):
                caminho = os.path.join(pasta, nome_arquivo)
                X.append(imagemParaVetor(caminho))
                y.append(rotulos[classe])
    return X, y