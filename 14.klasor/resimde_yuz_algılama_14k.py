import cv2   

img = cv2.imread("4.2 face.png.png")
face_cascade = cv2.CascadeClassifier("4.1 frontalface.xml.xml")
# Haar-like özellikleri kolay algılayabilmek için resmimizi boz(gri) tonlara çevirelim.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Şimdi de cascade dosyamızı kullanarak resim üzerindeki yüzlerin koordinatlarını bulalım.
faces = face_cascade.detectMultiScale(gray, 1.3, 7)

# "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()