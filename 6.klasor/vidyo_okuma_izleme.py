import cv2

cap=cv2.VideoCapture(0) # bu kısınma kameramdan anlık olarak goruntu alırız

while True:
    ret,frame=cap.read() #burdaki ret sonsuz vidyo için kullanılır ama sınırlı vidyoda ret false döndürüe buda hata verilmesine neden olur
    # bunun onlenebilmesi için ret==0 ise break diyerek donguden cıkılmalıdır
    frame=cv2.flip(frame,1) #ters olan resmi düz görmemiz için kullanılır(kendimizi aynada gördügümüz gibi gorelim diye)

    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"): #burda & 0xFF==ord("q") ifadesi klavyede q harfine basıldıgında goruntunun kaoatılmasını soyler
        break
    # bu kısımda herbir framenin kaç saniye ekranda kalacagını belirliyoruz

cap.release() # bu kisimda yaptigimiz islemi kapatiyoruzki baska islemlerde yapabilelim
cv2.destroyAllWindows()
