import cv2
import matplotlib.pyplot as plt


image = cv2.imread('CHEF.jpg', cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(image, 100, 200)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Detecção de Bordas')
plt.imshow(edges, cmap='gray')

plt.show()





