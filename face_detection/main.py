import cv2
import numpy as np
from PIL import Image
import os

path = "./images/"
save_path = './faces/'
img_list = []
#get images list
for x in os.listdir(path):
        if x.endswith((".jpg",".png" ,".jpeg")):
                img_list.append(x)
#use haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
num_image = 0
for img_name in img_list:
        #unload image
        image = Image.open(path + img_name)
        #convert PIL image to Opencv Image
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image= cv2.resize(image, (800, 600))
        #detect faces
        faces = face_cascade.detectMultiScale(image, 1.1, 4)
        for (x, y, w, h) in faces:
                num_image +=1
                #crop faces in image
                image1 = image[y:y+h, x:x+w]
                # cv2.imshow(str(num_image), image1)
                #write image
                cv2.imwrite(save_path + '/face_' + str(num_image) + '.jpg', image1)
print('The number of faces is: {0}'.format(num_image))

