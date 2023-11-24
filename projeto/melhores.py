import os
from PIL import Image

if __name__ == '__main__':
    # Nomes das pastas e o nome do arquivo de imagem
    pasta1 = os.path.join(os.getcwd(), 'images/gray')
    pasta2 = os.path.join(os.getcwd(), 'images/color')
    pasta3 = os.path.join(os.getcwd(), 'images/origin')
    pasta4 = os.path.join(os.getcwd(), 'images/join')
    
    # Iterar sobre todos os arquivos na pasta 
    for arquivo in os.listdir(pasta1):
        # Todos arquivos têm o mesmo nome
        caminho_arquivo1 = os.path.join(pasta1, arquivo)
        caminho_arquivo2 = os.path.join(pasta2, arquivo)
        caminho_arquivo3 = os.path.join(pasta3, arquivo)

        # Carregar as imagens
        caminho_imagem1 = os.path.join(pasta1, caminho_arquivo1)
        caminho_imagem2 = os.path.join(pasta2, caminho_arquivo2)
        caminho_imagem3 = os.path.join(pasta3, caminho_arquivo3)

        imagem1 = Image.open(caminho_imagem1)
        imagem2 = Image.open(caminho_imagem2)
        imagem3 = Image.open(caminho_imagem3)

        # Calcular dimensões para a imagem combinada
        largura_total = imagem1.width + imagem2.width + imagem3.width
        altura_maxima = max(imagem1.height, imagem2.height, imagem3.height)

        # Criar uma nova imagem com a largura total e a maior altura
        imagem_combinada = Image.new('RGB', (largura_total, altura_maxima))

        # Colocar as imagens lado a lado
        imagem_combinada.paste(imagem1, (0, 0))
        imagem_combinada.paste(imagem2, (imagem1.width, 0))
        imagem_combinada.paste(imagem3, (imagem1.width + imagem2.width, 0))

        # Salvar a imagem combinada
        imagem_combinada.save(os.path.join(pasta4, arquivo))
