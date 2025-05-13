import cv2
import numpy as np

img=cv2.imread("9.1 star.png.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,0)
contours,_=cv2.findContours(thresh,2,1)
cnt=contours[0] #===> contourstaki istenilen yerlere ulasabilmek için / contours[0] / kullanılır 

hull=cv2.convexHull(cnt,returnPoints=False) #returnPoints=False dedigimiz icin inndis degerlerine ulasıcaz
defects=cv2.convexityDefects(cnt,hull) # dış bukeylere burdan ulasicaz

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]
    star=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])
    cv2.line(img,star,end,(255,0,0),2)
    cv2.circle(img,far,6,(255,0,0),-1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()    

