import cv2
alg= "haarcascade_frontalface_default.xml"  #algorithm for detection
haar_cascade = cv2.CascadeClassifier(alg)
cam =cv2.VideoCapture(0) #primary_camera

while True:
    text = "No face detected"
    ret,img=cam.read()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayimg, 1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
        text = "face detected"
    cv2.putText(img, text, (10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    cv2.imshow("facedetected", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
