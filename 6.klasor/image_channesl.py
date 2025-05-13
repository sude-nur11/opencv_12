# resimderki kırmızı mavi vve yeşil pikselleri çekip bunları inceliycez
import numpy as np
import matplotlib.pyplot as plt


path = 'D:\\temp\\OpenCV\\test_images\\map.jpeg'
img = plt.imread(path)


"""
[r,g,b]
[50,50,0] # 50 ye 50 lik pikseldeki kırmızı rekleri çeker
[70,70,1] # yeşil rengi çeker
[:,:,2]   # bütün resimdeki mavi renkleri çeker
r -> 0-255
g -> 0-255
b -> 0-255 
"""

r = img[:,:,0] # bütün kırmızı,yeşil ve mavi rekleri r g ve b değerlerine atarız
g = img[:,:,1]
b = img[:,:,2]

output = np.dstack((r,g,b)) # bu kısımda çekmiş olduğumuz renkleri karıştırarak gerçek resmi elde ederiz
plt.imshow(output)
plt.show()



"""
output = [img,r,g,b]
titles = ["Image","Red","Green","Blue"]

for i in range(4):
    plt.subplot(2,2,i+1) # 2 satır 2 sütun ve i+1 de hangi sıraya yerleşiceğini söyler
    plt.axis("off")
    plt.title(titles[i])                # burda resmin içerisindeki kırmızı yeşil ve mavi renkleri teker teker gösteririz
    if i ==0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap='gray')
    plt.show()


"""