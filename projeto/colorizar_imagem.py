import cv2
import numpy as np

class ColorizarImagem:
    def __init__(self):
        """
            Método contrutor da classe, define a rede com modelo treinado
        """
        # Define os caminhos para os pontos, protobuffer e modelo
        points = 'modelo/pts_in_hull.npy'
        prototxt = 'modelo/colorization_deploy_v2.prototxt'
        model = 'modelo/colorization_release_v2.caffemodel'

        # Carrega o modelo da rede neural e matriz de pontos
        self.net = cv2.dnn.readNetFromCaffe(prototxt, model)
        pts = np.load(points)

        # Adiciona os kernels do cluster como convoluções 1x1 ao modelo
        class8 = self.net.getLayerId('class8_ab')
        conv8 = self.net.getLayerId('conv8_313_rh')
        pts = pts.transpose().reshape(2, 313, 1, 1)
        self.net.getLayer(class8).blobs = [pts.astype('float32')]
        self.net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype='float32')]

    def colorizar_imagem(self, image_filename):
        """
            Etapa de pré-processamento 
        """
        # Carrega a imagem de entrada 
        image = cv2.imread(image_filename) 
        # Dimensiona os valores no intervalo de 0 a 1 
        scaled = image.astype('float32') / 255.0
        # Converte a imagem de BGR para o espaço de cores LAB
        lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
        
        # Redimensiona a imagem para 224x224 (padrão do algoritmo)
        resized = cv2.resize(lab, (224, 224))
        # Extrai o canal L
        L = cv2.split(resized)[0]
        # Centralização média
        L -= 50

        """
            Etapa de processamento 
        """
        # Manda o canal L para a rede fazer a predição dos novos canais A e B
        self.net.setInput(cv2.dnn.blobFromImage(L))
        ab = self.net.forward()[0, :, :, :].transpose((1, 2, 0))

        """
            Etapa de pós-processamento
        """
        # Redimensiona AB previsto para as mesmas dimensões da imagem original
        ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

        # Pega o canal L da imagem de original convertida
        L = cv2.split(lab)[0]
        # Concatena o canal L original com os canais AB previstos
        colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

        # Converte a imagem de saída de LAB para RGB 
        colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
        # Tira os valores que não estão no intervalo de 0 a 1
        colorized = np.clip(colorized, 0, 1)
        # Converte para 8 bits no intervalo de 0 a 255
        colorized = (255 * colorized).astype('uint8')
        
        return colorized

if __name__ == '__main__':
    # Nome do arquivo de imagem
    name_img = 'cachoeira_gray.jpg'

    # Cria o objeto da classe de colorização
    colorizador = ColorizarImagem()

    # Chama o algoritmo de colorização
    img_cor = colorizador.colorizar_imagem(name_img)

    # Pega o nome e extensão do arquivo original 
    arq_ori = str(name_img).split('.')
    # Cria novo nome para a imagem colorizada
    arq_cor = arq_ori[0] + '_cor.' + arq_ori[1]
    # Salva a imagem colorizada 
    cv2.imwrite(arq_cor, img_cor)
