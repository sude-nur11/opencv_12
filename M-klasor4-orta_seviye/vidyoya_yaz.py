# OpenCV ile videoya yazma (RGB kanallarını gösterir)

import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import time

print("[INFO] Kamera başlatılıyor...")
vs = VideoStream(src=0).start()   # Kamerayı başlat
time.sleep(2.0)                   # Isınma süresi

fourcc = cv2.VideoWriter_fourcc(*"MJPG")  # Codec ayarı
output_path = "ornek_video.avi"           # Çıkış dosyası
fps = 20
writer = None
(h, w) = (None, None)
zeros = None

while True:
    frame = vs.read()                    
    frame = imutils.resize(frame, width=300)  

    if writer is None:
        (h, w) = frame.shape[:2]         # Genişlik-yükseklik al
        writer = cv2.VideoWriter(output_path, fourcc, fps, (w * 2, h * 2), True)
        zeros = np.zeros((h, w), dtype="uint8")  # Boş matris

    (B, G, R) = cv2.split(frame)         # RGB ayır
    R = cv2.merge([zeros, zeros, R])     # Kırmızı kanal
    G = cv2.merge([zeros, G, zeros])     # Yeşil kanal
    B = cv2.merge([B, zeros, zeros])     # Mavi kanal

    output = np.zeros((h * 2, w * 2, 3), dtype="uint8")  
    output[0:h, 0:w] = frame             # Sol üst: orijinal
    output[0:h, w:w*2] = R               # Sağ üst: kırmızı
    output[h:h*2, 0:w] = B               # Sol alt: mavi
    output[h:h*2, w:w*2] = G             # Sağ alt: yeşil

    cv2.imshow("Kamera", frame)          
    cv2.imshow("Çıktı", output)          
    writer.write(output)                 # Videoya yaz

    if cv2.waitKey(1) & 0xFF == ord("q"):  
        break

print("[INFO] Temizleniyor...")
cv2.destroyAllWindows()                  
vs.stop()                                # Kamerayı durdur
writer.release()                         # Videoyu kaydet ve kapat
