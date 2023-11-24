import cv2
import os
from colorizar_imagem import ColorizarImagem

if __name__ == '__main__':
    # Caminho das pastas
    pasta_origem = 'images/gray'
    pasta_destino = 'images/color'

    # Objeto usado para colorir
    colorizador = ColorizarImagem()

    # Certifique-se de que a pasta de destino existe
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Iterar sobre todos os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)

        # Verifique se é um arquivo (e não uma pasta, por exemplo)
        if os.path.isfile(caminho_arquivo_origem):
            # Manda a imagem para a colorização
            img_cor = colorizador.colorizar_imagem(caminho_arquivo_origem)

            # Caminho para o novo arquivo
            caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)

            # Salva a nova imagem colorida
            cv2.imwrite(caminho_arquivo_destino, img_cor)
