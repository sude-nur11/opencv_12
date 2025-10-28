# pyimagesearch/keyclipwriter.py
from collections import deque
from threading import Thread
from queue import Queue
import time
import cv2

class KeyClipWriter:
    def __init__(self, bufSize=64, timeout=1.0):
        # Arabellek boyutu ve yazma gecikmesi
        self.bufSize = bufSize
        self.timeout = timeout
        # Kare arabelleği, yazılacak kare kuyruğu, video yazıcı ve iş parçacığı
        self.frames = deque(maxlen=bufSize)
        self.Q = None
        self.writer = None
        self.thread = None
        self.recording = False

    def update(self, frame):
        # Arabellek ve kayıt kuyruğunu güncelle
        self.frames.appendleft(frame)
        if self.recording:
            self.Q.put(frame)

    def start(self, outputPath, fourcc, fps):
        # Kayıt başlat
        self.recording = True
        self.writer = cv2.VideoWriter(outputPath, fourcc, fps,(self.frames[0].shape[1], self.frames[0].shape[0]), True)
        self.Q = Queue()
        # Önceki arabellek karelerini kuyruğa ekle
        for i in range(len(self.frames), 0, -1):
            self.Q.put(self.frames[i - 1])
        # Yazma iş parçacığını başlat
        self.thread = Thread(target=self.write, args=())
        self.thread.daemon = True
        self.thread.start()

    def write(self):
        # Kuyruktaki kareleri dosyaya yaz
        while True:
            if not self.recording:
                return
            if not self.Q.empty():
                frame = self.Q.get()
                self.writer.write(frame)
            else:
                time.sleep(self.timeout)

    def flush(self):
        # Kalan kareleri yaz
        while not self.Q.empty():
            frame = self.Q.get()
            self.writer.write(frame)

    def finish(self):
        # Kayıt bitir ve temizle
        self.recording = False
        self.thread.join()
        self.flush()
        self.writer.release()
