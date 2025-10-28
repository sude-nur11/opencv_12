# detect_blur.py
# OpenCV ile bulanıklık tespiti

from imutils import paths
# import argparse
import cv2

# Laplacian varyansını hesapla
def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

# # Argümanları al
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", required=True, help="Görüntü klasör yolu")
# ap.add_argument("-t", "--threshold", type=float, default=100.0, help="Eşik değeri")
# args = vars(ap.parse_args())

images_path = "dog_resimler_bulanik"   # Görsellerin olduğu klasör
threshold = 100.0        # Bulanıklık eşiği

# Görselleri sırayla işle
for imagePath in paths.list_images(images_path):
    image = cv2.imread(imagePath)                     # Görüntüyü oku
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    # Griye çevir
    fm = variance_of_laplacian(gray)                  # Odak ölçüsünü al
    text = "Bulanık Degil" if fm >=threshold else "Bulanik"

    # Sonucu yazdır
    cv2.putText(image, f"{text}: {fm:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)                        # Görüntüyü göster
    key = cv2.waitKey(0)                              # Tuş bekle
