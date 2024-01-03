import cv2
img = cv2.imread('otan.webp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY )
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray,1.1, 5)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(2,3,123),2)
    roi_color = img[y:y+h,x:x+w]
    cv2.imwrite('rosto.jpg',roi_color)
cv2.imshow('rosto',img)
cv2.waitKey(0)
    
