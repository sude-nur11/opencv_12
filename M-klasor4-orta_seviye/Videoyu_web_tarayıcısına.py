# gerekli paketleri içe aktar
from pyimagesearch.motion_detection import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2

# çıktı karesi (outputFrame) ve kilit (lock) değişkenlerini başlat
# bu kilit, birden fazla tarayıcı veya sekme akışı izlerken
# karelerin güvenli bir şekilde paylaşılmasını sağlar
outputFrame = None
lock = threading.Lock()

# flask uygulamasını başlat
app = Flask(__name__)

# video akışını başlat ve kameranın ısınması için biraz bekle
vs = VideoStream(src=0).start()
time.sleep(2.0)

@app.route("/")
def index():
    # ana sayfayı (index.html) döndür
    return render_template("index.html")

def detect_motion(frameCount):
    global vs, outputFrame, lock

    # hareket algılayıcısını ve okunan toplam kare sayısını başlat
    md = SingleMotionDetector(accumWeight=0.1)
    total = 0

    # video akışından gelen kareleri döngüyle işle
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        # geçerli zamanı al ve görüntü üzerine yazdır
        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.35, (0, 0, 255), 1)

        # eğer yeterli sayıda kare okunmuşsa,
        # arka plan modeli oluşturulmuştur, hareket algılama yapılabilir
        if total > frameCount:
            motion = md.detect(gray)

            # karede hareket algılandı mı kontrol et
            if motion is not None:
                # hareket alanını içeren dikdörtgeni (kutuyu) çiz
                (thresh, (minX, minY, maxX, maxY)) = motion
                cv2.rectangle(frame, (minX, minY), (maxX, maxY),
                              (0, 0, 255), 2)

        # arka plan modelini güncelle ve kare sayısını artır
        md.update(gray)
        total += 1

        # kilidi al, çıktı karesini güncelle, ardından kilidi bırak
        with lock:
            outputFrame = frame.copy()

def generate():
    global outputFrame, lock

    # çıktı akışından kareleri döngüyle üret
    while True:
        with lock:
            if outputFrame is None:
                continue

            # kareyi JPEG formatında kodla
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

            # kare başarıyla kodlandı mı kontrol et
            if not flag:
                continue

        # kareyi bayt formatında döndür
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
    # oluşturulan video akışını (MIME tipi belirtilmiş şekilde) döndür
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=False,
                    help="cihazın IP adresi")
    ap.add_argument("-o", "--port", type=int, required=False,
                    help="sunucunun port numarası (1024 - 65535 arası)")
    ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="arka plan modelini oluşturmak için kullanılacak kare sayısı")
    args = vars(ap.parse_args())

    # hareket algılama işlemini başlatacak bir thread (iş parçacığı) oluştur
    t = threading.Thread(target=detect_motion, args=(args["frame_count"],))
    t.daemon = True
    t.start()

    # flask uygulamasını başlat
    app.run(host=args["ip"],
            port=args["port"],
            debug=True,
            threaded=True,
            use_reloader=False)

# uygulama durduğunda video akışını kapat
vs.stop()
