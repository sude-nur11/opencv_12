# beyaz tuval oluşturma

import cv2
import numpy as np
tuval=np.zeros((512,512,3),dtype=np.uint8) +255  # kanal verisi 3 girdik renkli çizimler yapabilmek için
                                                  # 100 gry 255 beyaz renk verir 
cv2.imshow("canvas",tuval)
cv2.waitKey(0)
cv2.derstroyAllWindows()