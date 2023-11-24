import os
from PIL import Image

if __name__ == '__main__':
    pasta = os.path.join(os.getcwd(), 'melhores')
    #pasta = os.path.join(os.getcwd(), 'piores')
    
    # Dimensões para a imagem combinada 255*5x255*3*2
    largura = 1530
    altura  = 1275
    
    # Criar uma nova imagem com a largura total e a maior altura
    imagem_combinada = Image.new('RGB', (largura, altura))

    # pivos
    x = y = cont = 0

    # Percorre todos arquivos da pasta
    for arquivo in os.listdir(pasta):
        # Define o caminho da imagem
        caminho_arquivo = os.path.join(pasta, arquivo)
        caminho_imagem = os.path.join(pasta, caminho_arquivo)
        imagem = Image.open(caminho_imagem)

        # Colocar as imagens lado a lado
        imagem_combinada.paste(imagem, (x, y))

        # add contador e tamanho da imagem para a proxima
        cont += 1
        y += imagem.height

        # na metade altura zero e dobra a largura
        if cont == 5:
            x += imagem.width
            y = 0

    # Salvar a imagem combinada
    imagem_combinada.save(os.path.join(pasta, 'melhores.jpg'))
    #imagem_combinada.save(os.path.join(pasta, 'piores.jpg'))
