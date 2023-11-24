import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('cachoeira.jpg')

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Converter a imagem para o espaço de cores LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Extrair os canais L, A e B
L, A, B = cv2.split(lab_image)

# Configurar o layout do matplotlib
fig, axs = plt.subplots(1, 4, figsize=(25, 15)) # Agora com 5 subplots

# Mostrar a imagem original colorida
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original')
axs[0].axis('off')

# Mostrar o canal L
axs[1].imshow(L, cmap='gray')
axs[1].set_title('Canal L')
axs[1].axis('off')

# Mostrar o canal A
axs[2].imshow(A, cmap='gray')
axs[2].set_title('Canal A')
axs[2].axis('off')

# Mostrar o canal B
axs[3].imshow(B, cmap='gray')
axs[3].set_title('Canal B')
axs[3].axis('off')

# Adicionar descrições e mostrar o plot
plt.suptitle('Comparação da Imagem Original e Canais LAB')
plt.show()
