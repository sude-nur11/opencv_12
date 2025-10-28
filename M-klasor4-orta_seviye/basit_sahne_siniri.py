import cv2
import imutils
import os

#GİRİŞ ve ÇIKIŞ dosyaları
video_path = "yuruyus.mp4"   # Giriş video dosyası
output_dir = "output"                     # Çıktı klasörü

#PARAMETRELER
MIN_PERCENT = 1.0     # Minimum hareket yüzdesi
MAX_PERCENT = 10.0    # Maksimum hareket yüzdesi
WARMUP_FRAMES = 200   # Arka plan ısınma süresi

#Klasör yoksa oluştur
os.makedirs(output_dir, exist_ok=True)

#Arka plan çıkarıcı başlat
fgbg = cv2.createBackgroundSubtractorMOG2()

#Takip değişkenleri
captured = False
total = 0
frames = 0

#Videoyu aç
vs = cv2.VideoCapture(video_path)
(W, H) = (None, None)

while True:
    # Kareyi oku
    grabbed, frame = vs.read()
    if not grabbed:
        break

    # Orijinali sakla ve yeniden boyutlandır
    orig = frame.copy()
    frame = imutils.resize(frame, width=600)

    # Arka plan çıkar ve maskeyi temizle
    mask = fgbg.apply(frame)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # İlk karede boyut al
    if W is None or H is None:
        (H, W) = mask.shape[:2]

    # Hareket yüzdesi hesapla
    p = (cv2.countNonZero(mask) / float(W * H)) * 100

    # Hareket durduysa paneli kaydet
    if p < MIN_PERCENT and not captured and frames > WARMUP_FRAMES:
        cv2.imshow("Captured", frame)
        captured = True

        filename = f"{total}.png"
        path = os.path.sep.join([output_dir, filename])
        total += 1

        print(f"[INFO] {path} kaydediliyor...")
        cv2.imwrite(path, orig)

    # Tekrar hareket başlarsa yakalamayı sıfırla
    elif captured and p >= MAX_PERCENT:
        captured = False

    # Görüntüleri göster (isteğe bağlı)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(1) & 0xFF

    # Q tuşuna basınca çık
    if key == ord("q"):
        break

    frames += 1

vs.release()
cv2.destroyAllWindows()
print("[INFO] İşlem tamamlandı ✅")
