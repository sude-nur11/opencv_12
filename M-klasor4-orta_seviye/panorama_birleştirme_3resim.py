import cv2
import imutils
from imutils import paths

images_path = "C:\\Users\\sude nur toprak\\Desktop\\Algoritma\\model_egitme\\M-klasor4-orta_seviye\\panorama_doga"   # örnek klasör
output_path = "output.png"          # kaydedilecek dosya


print("[INFO] Görseller yükleniyor...")
image_paths = sorted(list(paths.list_images(images_path)))
images = [cv2.imread(path) for path in image_paths]
print("Yüklenen görsel sayısı:", len(images))
for path in image_paths:
    print(path)


#Görselleri birleştir
print("[INFO] Görseller birleştiriliyor...")
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

#Başarılıysa kaydet ve göster
if status == 0:
    print("[INFO] Görüntü birleştirme başarılı!")
    cv2.imwrite(output_path, stitched)
    cv2.imshow("Panorama", imutils.resize(stitched, width=800))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"[ERROR] Görüntü birleştirme başarısız! Kod: {status}")
