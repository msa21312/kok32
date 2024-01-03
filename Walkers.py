import cv2



body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


cap = cv2.VideoCapture('walking.avi')


while True:
    
  
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY )
 
    body = body_cascade.detectMultiScale(gray,1.1, 5)
    

    for(x,y,w,h) in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(2,3,123),2)
        cv2.imshow('pwseatres',frame)
        

    if cv2.waitKey(1) == 32: 
        break

cap.release()
cv2.destroyAllWindows()
