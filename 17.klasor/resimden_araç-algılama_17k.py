import cv2


img = cv2.imread('2.2 car.jpg.jpg')

# Araba tespiti için eğitilmiş sınıflandırıcıyı yükle 
car_cascade = cv2.CascadeClassifier('2.3 car.xml.xml')
# Görüntüyü gri tonlama
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Arabaları tespit et:
# 1.1 - ölçek faktörü (ne kadar küçükse o kadar hassas, ancak daha yavaş)
# 1 - minimum komşu sayısı (daha yüksek değerler yanlış pozitifleri azaltır)
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

#araba için dikdörtgen çiz
for (x, y, w, h) in cars:
    # (x,y) - sol üst köşe koordinatları
    # (x+w, y+h) - sağ alt köşe koordinatları 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
    

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()