import cv2
import datetime
import argparse
import imutils
from imutils.video import WebcamVideoStream

class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240), framerate=32):
        # PiCamera mı USB/yerleşik mi kontrolü
        if usePiCamera:
            from imutils.video.pivideostream import PiVideoStream
            self.stream = PiVideoStream(resolution=resolution, framerate=framerate)
        else:
            self.stream = WebcamVideoStream(src=src)

    def start(self):
        self.stream.start()
        return self

    def update(self):
        self.stream.update()

    def read(self):
        return self.stream.read()

    def stop(self):
        self.stream.stop()


# Komut satırı argümanı
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1, help="1=PiCamera, 0=USB/yerleşik")
args = vars(ap.parse_args())

# Video başlat ve sensörün ısınmasını bekle
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
import time
time.sleep(2.0)

# Kareleri göster
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    ts = datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,255), 1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
