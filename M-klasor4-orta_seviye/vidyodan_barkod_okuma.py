# Gerekli kütüphaneler
from pyimagesearch.simple_barcode_detection.BarkodFonk import detect
from imutils.video import VideoStream
import argparse
import time
import cv2

# Komut satırından video dosyası alınabilir (veya webcam)
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="(isteğe bağlı) video dosyasının yolu")
args = vars(ap.parse_args())

# Video yolu yoksa webcam başlat
if not args.get("video", False):
    vs = VideoStream(src=0).start()
    time.sleep(2.0)  # Kamera başlatma süresi
else:
    vs = cv2.VideoCapture(args["video"])

print("[INFO] Barkod tarama başlatıldı. 'q' tuşuna basarak çıkabilirsin.")

# Kareleri tek tek işle
while True:
    # VideoStream veya VideoCapture durumuna göre kare oku
    frame = vs.read()
    frame = frame[1] if args.get("video", False) else frame
    # frame=cv2.flip(frame,1)

    # Video bitmişse çık
    if frame is None:
        break

    # Barkodu algıla
    box =detect(frame)
    
    if box is not None:
        cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
        print(f"[INFO] Barkod bulundu: {box}")
    else:
        print("[INFO] Barkod bulunamadı")

    # Görüntüyü göster
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Q tuşuna basılırsa çık
    if key == ord("q"):
        break

# Kaynakları serbest bırak
if not args.get("video", False):
    vs.stop()
else:
    vs.release()

cv2.destroyAllWindows()
