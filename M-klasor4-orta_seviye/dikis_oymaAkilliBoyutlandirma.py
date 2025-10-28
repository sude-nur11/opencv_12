import cv2
import numpy as np
from skimage import filters

#Girdi görseli ve yönü doğrudan belirt
image_path = "dikis_ag.jpg"   
direction = "vertical"     # "vertical" veya "horizontal"

image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Görsel bulunamadı, dosya yolunu kontrol et!")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype("float32")

#Enerji haritası oluştur (Sobel filtresi)
def compute_energy(gray):
    return filters.sobel(gray)

#Minimum enerji dikiş yolunu bul
def find_seam(energy):
    h, w = energy.shape
    M = energy.copy()
    backtrack = np.zeros_like(M, dtype=np.int32)

    for i in range(1, h):
        for j in range(w):
            # sol-üst, üst, sağ-üst piksellerin maliyetini al
            left = max(j - 1, 0)
            right = min(j + 1, w - 1)
            idx = np.argmin(M[i - 1, left:right + 1])
            backtrack[i, j] = left + idx
            M[i, j] += M[i - 1, left + idx]
    return M, backtrack

#Dikişi kaldır
def remove_seam(image, backtrack):
    h, w, _ = image.shape
    mask = np.ones((h, w), dtype=np.bool_)
    j = np.argmin(backtrack[-1])
    for i in reversed(range(h)):
        mask[i, j] = False
        j = backtrack[i, j]
    mask = np.stack([mask]*3, axis=2)
    return image[mask].reshape((h, w - 1, 3))

#Tekrarlı dikiş kaldırma
def seam_carve_manual(image, num_seams, direction="vertical"):
    output = image.copy()
    for n in range(num_seams):
        if direction == "horizontal":
            output = np.rot90(output, 1, (0, 1))  # geçici olarak döndür
        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY).astype("float32")
        energy = compute_energy(gray)
        _, backtrack = find_seam(energy)
        output = remove_seam(output, backtrack)
        if direction == "horizontal":
            output = np.rot90(output, 3, (0, 1))  # eski haline döndür
    return output

#Orijinal görüntü
cv2.imshow("Orijinal", image)

#Farklı dikiş sayıları için dene
for numSeams in range(20, 61, 20):
    carved = seam_carve_manual(image, numSeams, direction)
    print(f"[INFO] {numSeams} dikiş kaldırıldı; Yeni boyut: w={carved.shape[1]}, h={carved.shape[0]}")
    cv2.imshow(f"{numSeams} Dikiş Sonrası", carved)
    cv2.waitKey(0)

cv2.destroyAllWindows()
