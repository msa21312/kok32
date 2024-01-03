import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
freme= cv2.imread(images[0])
height,width,channels = freme.shape
size=(width,height)
alt=cv2.VideoWriter('por do sol.mp4',cv2.VideoWriter_fourcc(*'DIVX'),15,size)
for i in range(0,count-1):
    freme=cv2.imread(images[i])
    alt.write(freme)
alt.release()
print('fim acbou ja era fim de tudo the end')