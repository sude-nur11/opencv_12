import cv2   

img = cv2.imread("3.2 body.jpg.jpg")

body_cascade = cv2.CascadeClassifier("3.3 fullbody.xml.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
bodies = body_cascade.detectMultiScale(gray,1.1,5)

# "bodies" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
         
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()