import os
import cv2
import sys

path='C:/Users/Lenovo/Desktop/a-star-algorithm-master/a-star-algorithm-master/'
imagelist=os.listdir(path)
for imgname in imagelist:
    if(imgname.endswith(".png")):
        image=cv2.imread(path+imgname)
        cv2.imshow("picture",image)
        k=cv2.waitKey(20)
        if k == 27:
            break
cv2.destroyAllWindows()