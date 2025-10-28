import numpy as np
import cv2
import imutils

class Stitcher:
    def __init__(self):
        # OpenCV sürümünü kontrol et (bazı fonksiyonlar sürüme göre değişir)
        self.isv3 = imutils.is_cv3(or_better=True)

    def stitch(self, images, ratio=0.75, reprojThresh=4.0, showMatches=False):
        # Görselleri (soldaki ve sağdaki) unpack et
        (imageB, imageA) = images

        # Görsellerdeki anahtar noktaları (keypoints) ve özellik vektörlerini (descriptors) çıkar
        (kpsA, featuresA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB) = self.detectAndDescribe(imageB)

        # İki görüntü arasındaki özellikleri eşleştir
        M = self.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh)

        # Eğer eşleşme başarısızsa panorama oluşturulamaz
        if M is None:
            return None

        # Elde edilen eşleşmeleri, homografi matrisini ve durum bilgilerini ayır
        (matches, H, status) = M

        # Perspektif dönüşüm (warp) işlemi — iki görüntüyü tek panoramada birleştirir
        result = cv2.warpPerspective(imageA, H, 
                                     (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

        # Eşleşme çizimlerini göstermek istersek:
        if showMatches:
            vis = self.drawMatches(imageA, imageB, kpsA, kpsB, matches, status)
            return (result, vis)

        return result

    def detectAndDescribe(self, image):
        # Görseli gri tona dönüştür (özellik tespiti genelde gri tonda yapılır)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Eğer OpenCV 3.x veya üstü sürüm kullanılıyorsa
        if self.isv3:
            # SIFT (Scale-Invariant Feature Transform) oluştur
            descriptor = cv2.SIFT_create()
            (kps, features) = descriptor.detectAndCompute(image, None)
        else:
            # Eski OpenCV sürümleri için
            detector = cv2.FeatureDetector_create("SIFT")
            kps = detector.detect(gray)
            extractor = cv2.DescriptorExtractor_create("SIFT")
            (kps, features) = extractor.compute(gray, kps)

        # KeyPoint nesnelerini NumPy dizisine çevir
        kps = np.float32([kp.pt for kp in kps])
        return (kps, features)

    def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh):
        # Brute Force (kaba kuvvet) eşleştirici oluştur
        matcher = cv2.DescriptorMatcher_create("BruteForce")
        # En yakın 2 eşleşmeyi al
        rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
        matches = []

        # Eşleşmeler üzerinde dön — Lowe oran testini uygula
        for m in rawMatches:
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))

        # En az 4 iyi eşleşme gerekiyorsa homografi hesaplanabilir
        if len(matches) > 4:
            # Eşleşen noktaları al
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])

            # Homografi matrisini (dönüşüm) hesapla — RANSAC ile
            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)
            return (matches, H, status)

        # Yeterli eşleşme yoksa None döndür
        return None

    def drawMatches(self, imageA, imageB, kpsA, kpsB, matches, status):
        # Görselleştirme için boş bir tuval (canvas) oluştur
        (hA, wA) = imageA.shape[:2]
        (hB, wB) = imageB.shape[:2]
        vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")

        # Görselleri yan yana yerleştir
        vis[0:hA, 0:wA] = imageA
        vis[0:hB, wA:] = imageB

        # Doğru eşleşmeleri yeşil çizgilerle göster
        for ((trainIdx, queryIdx), s) in zip(matches, status):
            if s == 1:
                ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
                ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
                cv2.line(vis, ptA, ptB, (0, 255, 0), 1)
        return vis
