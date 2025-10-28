import cv2
import time
from pyimagesearch.keyclipwriter import KeyClipWriter

# Ayarlar
OUTPUT_PATH = "output.mp4"
FPS = 30
CODEC = cv2.VideoWriter_fourcc(*"MJPG")
BUFFER_SIZE = 64

print("[INFO] Kamera açılıyor...")
camera = cv2.VideoCapture(0)
time.sleep(1.0)

# KeyClipWriter nesnesi
kcw = KeyClipWriter(bufSize=BUFFER_SIZE)
recording = False

print("[INFO] 'k' = kayıt başlat/durdur | 'q' = çıkış")

while True:
    grabbed, frame = camera.read()
    if not grabbed:
        break

    cv2.imshow("Video Kaydı", frame)
    key = cv2.waitKey(1) & 0xFF
    kcw.update(frame)

    # 'k' → kayıt başlat/durdur
    if key == ord("k"):
        if not recording:
            print("[INFO] Kayıt başladı...")
            kcw.start(OUTPUT_PATH, CODEC, FPS)
            recording = True
        else:
            print("[INFO] Kayıt durdu, dosya kaydediliyor...")
            kcw.finish()
            recording = False

    # 'q' → çıkış
    elif key == ord("q"):
        break

if recording:
    kcw.finish()
camera.release()
cv2.destroyAllWindows()
print("[INFO] Program kapandı.")
