import cv2   

img = cv2.imread("5.3 eye.png.png")

# Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("4.1 frontalface.xml.xml")
eye_cascade = cv2.CascadeClassifier("5.1 eye.xml.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
faces = face_cascade.detectMultiScale(gray,1.3,5)

# "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# Şimdi de, bulduğum yüzler içinde göz arayacağım. 
gray2 = gray[y:y+h, x:x+w]
img2 = img[y:y+h, x:x+w]

# eye cascade dosyasını kullanarak gözlerin koordinatlarını bulalım.
eyes = eye_cascade.detectMultiScale(gray2)

# bu koordinatlara dikdörtgen çizelim.
for (ex,ey,ew,eh) in eyes:
	cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
         
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()