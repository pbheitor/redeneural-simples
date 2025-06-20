import os
import shutil

limitrofes_map = [
    ('quadrado_circulo_1.png', 'quadrado'),
    ('quadrado_circulo_2.png', 'quadrado'),
    ('quadrado_circulo_3.png', 'quadrado'),
    ('triangulo_quadrado_1.png', 'triangulo'),
    ('triangulo_quadrado_2.png', 'triangulo'),
    ('triangulo_quadrado_3.png', 'triangulo'),
    ('circulo_triangulo_1.png', 'circulo'),
]

src_folder = os.path.join('data', 'imagens', 'limitrofe')

for img_name, destino in limitrofes_map:
    src_path = os.path.join(src_folder, img_name)
    dst_folder = os.path.join('data', 'imagens', destino)
    dst_path = os.path.join(dst_folder, f'lim_{img_name}')
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f'Copiado: {src_path} -> {dst_path}')
    else:
        print(f'Não encontrado: {src_path} (adicione ou corrija o nome se necessário)')
