import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
escolha = int(input("Escolha o numero e uma imagem ira passar nos filtros \n"))

if escolha == 1:
    imagem = cv2.imread('./Todos/imgOriginal.jpg')
elif escolha == 2:
    imagem = cv2.imread('./Todos/calma.jpg')
elif escolha == 3:
    imagem = cv2.imread('./Todos/emoji.jpg')

imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # Converter de BGR para RGB

# Filtro de suavização (Gaussiano)
filtro_gaussiano = cv2.GaussianBlur(imagem_rgb, (5, 5), 0)

# Filtro de Média (Blur)
filtro_media = cv2.blur(imagem_rgb, (5, 5))

# Filtro de Mediana
filtro_mediana = cv2.medianBlur(imagem_rgb, 5)

# Filtro Bilateral
filtro_bilateral = cv2.bilateralFilter(imagem_rgb, 9, 75, 75)

# Filtro de realce de bordas (Sobel)
sobel_x = cv2.Sobel(imagem_rgb, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(imagem_rgb, cv2.CV_64F, 0, 1, ksize=5)
filtro_sobel = cv2.magnitude(sobel_x, sobel_y)

# Filtro Laplaciano
filtro_laplaciano = cv2.Laplacian(imagem_rgb, cv2.CV_64F)

# Filtro de aguçamento (Kernel)
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
filtro_aguçamento = cv2.filter2D(imagem_rgb, -1, kernel)

# Mostrar os resultados
plt.figure(figsize=(12,12))

# Imagem Original
plt.subplot(331)
plt.title('Imagem Original')
plt.imshow(imagem_rgb)
plt.axis('off')

# Filtro Gaussiano
plt.subplot(332)
plt.title('Filtro Gaussiano')
plt.imshow(filtro_gaussiano)
plt.axis('off')

# Filtro de Média
plt.subplot(333)
plt.title('Filtro Média')
plt.imshow(filtro_media)
plt.axis('off')

# Filtro de Mediana
plt.subplot(334)
plt.title('Filtro Mediana')
plt.imshow(filtro_mediana)
plt.axis('off')

# Filtro Bilateral
plt.subplot(335)
plt.title('Filtro Bilateral')
plt.imshow(filtro_bilateral)
plt.axis('off')

# Filtro Sobel
plt.subplot(336)
plt.title('Filtro Sobel')
plt.imshow(filtro_sobel, cmap='gray')
plt.axis('off')

# Filtro Laplaciano
plt.subplot(337)
plt.title('Filtro Laplaciano')
plt.imshow(filtro_laplaciano, cmap='gray')
plt.axis('off')

# Filtro de Aguçamento
plt.subplot(338)
plt.title('Filtro de Aguçamento')
plt.imshow(filtro_aguçamento)
plt.axis('off')

plt.tight_layout()
plt.show()
