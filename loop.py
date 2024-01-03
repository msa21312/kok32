
import cv2

# Leia a imagem
img = cv2.imread("butterfly.jpg")
for i in range(500):
    cv2.imshow(f'imagen{i+1}',img)
    cv2.waitKey(0)
cv2.destroyAllWindows()