import cv2
import numpy as np
import pywt

# Carrega a imagem em escala de cinza
image = cv2.imread('./Wavelet_Fourier/imgOriginal.jpg', cv2.IMREAD_GRAYSCALE)

# Transformada de Fourier para filtrar frequências indesejadas
def apply_fourier_filter(image, radius=30):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    mask = np.zeros((rows, cols, 2), np.uint8)
    cv2.circle(mask, (center_col, center_row), radius, (1, 1), -1)
    filtered_dft = dft_shift * mask
    dft_shift_back = np.fft.ifftshift(filtered_dft)
    restored_image = cv2.idft(dft_shift_back)
    restored_image = cv2.magnitude(restored_image[:, :, 0], restored_image[:, :, 1])
    
    # Normaliza a imagem restaurada
    cv2.normalize(restored_image, restored_image, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(restored_image)

# Transformada Wavelet para remoção de ruído e melhoria de detalhes
def apply_wavelet_denoising(image, wavelet='db1', level=1):
    coeffs = pywt.wavedec2(image, wavelet, level=level)
    coeffs[1:] = [(np.zeros_like(coeff[0]), np.zeros_like(coeff[1]), np.zeros_like(coeff[2])) for coeff in coeffs[1:]]
    denoised_image = pywt.waverec2(coeffs, wavelet)
    return np.uint8(np.clip(denoised_image, 0, 255))

# Gera a imagem filtrada com Fourier    
fourier_filtered_image = apply_fourier_filter(image)
cv2.imwrite("imagem_fourier_filtrada.jpg", fourier_filtered_image)

# Gera a imagem filtrada com Wavelet
wavelet_filtered_image = apply_wavelet_denoising(image)
cv2.imwrite("imagem_wavelet_filtrada.jpg", wavelet_filtered_image)

# Exibe as imagens original e filtradas
cv2.imshow("Imagem Original", image)
cv2.imshow("Imagem Fourier Filtrada", fourier_filtered_image)
cv2.imshow("Imagem Wavelet Filtrada", wavelet_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
