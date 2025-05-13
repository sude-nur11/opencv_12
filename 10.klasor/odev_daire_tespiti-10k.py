import cv2
import numpy as np

img=cv2.imread("daireler-9.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,9)

circle=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/6,param1=180,param2=15,minRadius=1,maxRadius=40)
# circle=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/6,param1=180,param2=11,minRadius=1,maxRadius=40)
if circle is not None:
    circle=np.uint16(np.around(circle))
    for i in circle[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),3)
        
cv2.imshow(f"yakalanan daireler : {circle.shape[1]}",img)    # .shape[1] ===> sayıyı verir
# cv2.imshow("blur",blur)    
cv2.waitKey(0)
cv2.destroyAllWindows()


   
