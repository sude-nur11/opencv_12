import cv2
import numpy as np
from collections import deque  # Sabit uzunlukta liste yapısı
#bu kısıma noktalar eklenicek bu yüzden kullandık

# Kamerayı aç 
cap = cv2.VideoCapture(0)

# Mavi rengi tanımlamak için HSV renk aralığı
lower_blue = np.array([100, 60, 60])
upper_blue = np.array([140, 255, 255])

# Her renk için noktaları saklamak için deque (çizim noktaları birikir)
blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

# Her rengin indeksini takip et
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# Renkler: BGR formatında
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]  # Mavi, Yeşil, Kırmızı, Sarı
color_index = 0  # Başlangıçta mavi seçili

# Beyaz zeminli bir "paint" ekranı oluştur
paintWindow = np.zeros((471, 636, 3)) + 255

# Üst kısımda butonlar için kutucuklar çiz
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)  # Temizle butonu
paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), colors[0], -1)  # Mavi
paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), colors[1], -1)  # Yeşil
paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), colors[2], -1)  # Kırmızı
paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), colors[3], -1)  # Sarı

# Buton isimleri
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(paintWindow, "CLEAR ALL", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

# Çizim penceresini oluştur
cv2.namedWindow("Paint")

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Ayna görüntüsü için çevir
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR'den HSV'ye dönüştür

    # Butonları çerçeveye yeniden çiz
    frame = cv2.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (160, 1), (255, 65), colors[0], -1)
    frame = cv2.rectangle(frame, (275, 1), (370, 65), colors[1], -1)
    frame = cv2.rectangle(frame, (390, 1), (485, 65), colors[2], -1)
    frame = cv2.rectangle(frame, (505, 1), (600, 65), colors[3], -1)

    # Buton yazıları
    cv2.putText(frame, "CLEAR ALL", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    if not ret:
        break

    # Maskeyi oluştur: sadece mavi renkleri algıla
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Gürültüyü azaltmak için morfolojik işlemler
    mask = cv2.erode(mask, (5, 5), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5, 5))
    mask = cv2.dilate(mask, (5, 5), iterations=1)

    # Maskede konturlar (nesne sınırları) bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if len(contours) > 0:
        # En büyük konturu al (mavi kalem gibi düşünülebilir)
        max_contours = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        ((x, y), radius) = cv2.minEnclosingCircle(max_contours)
        cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 0), 3)

        # Konturun merkezini hesapla
        M = cv2.moments(max_contours)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Üstteki butonlar bölgesine tıklanmışsa
        if center[1] <= 65:
            # Temizle
            if 40 <= center[0] <= 140:
                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]

                blue_index = green_index = red_index = yellow_index = 0
                paintWindow[67:, :, :] = 255  # Tüm çizimi temizle

            # Renk seçimleri
            elif 160 <= center[0] <= 255:
                color_index = 0  # Mavi
            elif 275 <= center[0] <= 370:
                color_index = 1  # Yeşil
            elif 390 <= center[0] <= 485:
                color_index = 2  # Kırmızı
            elif 505 <= center[0] <= 600:
                color_index = 3  # Sarı

        else:
            # Ekrana çizim yapılması
            if color_index == 0:
                blue_points[blue_index].appendleft(center)
            elif color_index == 1:
                green_points[green_index].appendleft(center)
            elif color_index == 2:
                red_points[red_index].appendleft(center)
            elif color_index == 3:
                yellow_points[yellow_index].appendleft(center)

    else:
        # Kalem ekranda değilse yeni bir çizgi başlat
        blue_points.append(deque(maxlen=512))
        blue_index += 1

        green_points.append(deque(maxlen=512))
        green_index += 1

        red_points.append(deque(maxlen=512))
        red_index += 1

        yellow_points.append(deque(maxlen=512))
        yellow_index += 1

    # Tüm noktaları çiz
    points = [blue_points, green_points, red_points, yellow_points]

    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue

                # Kameradaki görüntüye ve çizim ekranına çizgi çiz
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



