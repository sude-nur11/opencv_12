import cv2
import numpy as np

img=cv2.imread("3.1 h_line.png.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,75,150)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200) 
# maxLineGap=200 degeri çizgi boslugu dolduruyor ve 200 degeri degistirilebilir

for line in lines:
    x1,y1,x2,y2=line[0]   # nurdaki 0 sayesinde kordinatlara ulaşıyoruz
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
