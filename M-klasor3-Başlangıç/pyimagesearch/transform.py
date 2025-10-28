import numpy as np
import cv2

def order_points(pts):
    # 4 noktayı sıralamak için (sol üst, sağ üst, sağ alt, sol alt)
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # sol üst
    rect[2] = pts[np.argmax(s)]  # sağ alt

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # sağ üst
    rect[3] = pts[np.argmax(diff)]  # sol alt

    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Yeni görüntü boyutlarını hesapla
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    # Hedef nokta koordinatları (üstten görünüm için)
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # Perspektif dönüşüm matrisi ve uygulama
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped
