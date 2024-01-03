import cv2
img = cv2.imread('poster.jpg')
foguete = img[120:360,400:500]
img[0:240,500:600] = foguete
text = 'entao e natal oque voce fez o ano termina'
text2 = ' e come;a outra vez, entao natalllll oque voce fez o ano termina e come;a o utra vezzzzzz '

cv2.putText(img,text,(28,200),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.8,color=(0,0,255))
cv2.putText(img,text,(28,280),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(0,0,255))

cv2.imshow('natal ',img)
cv2.waitKey(0)