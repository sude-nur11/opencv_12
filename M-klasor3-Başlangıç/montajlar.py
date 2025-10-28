from imutils import build_montages  # Montaj fonksiyonu
from imutils import paths           # Klasördeki resim yollarını almak için
import cv2                          
import random                       # Rastgele örnekleme için

#Montaj yapmak istediğin resimlerin klasörünü belirt
image_folder = "dogaa"  # Buraya kendi klasörünü yazabilirsin

#Klasördeki tüm resimlerin yollarını al
imagePaths = list(paths.list_images(image_folder))

#Resimleri rastgele karıştır ve örnek sayısı kadar seç
sample_count = 21  # Kaç tane resim seçileceğini belirliyoruz
random.shuffle(imagePaths)
imagePaths = imagePaths[:sample_count]

#Resimleri yüklemek için boş bir liste oluştur
images = []

#Her bir resim yolunu sırayla yükle
for imagePath in imagePaths:
    image = cv2.imread(imagePath)  # Resmi oku
    if image is not None:
        images.append(image)        # Listeye ekle

# MONTAJ OLUŞTUR
# Her resim 128x196 piksel olacak, montaj 7 sütun x 3 satır şeklinde
montages = build_montages(images, (128, 196), (7, 3))

#Oluşan her montajı ekranda göster
for montage in montages:
    cv2.imshow("Montaj", montage)
    cv2.waitKey(0)  

cv2.destroyAllWindows()
