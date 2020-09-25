import cv2

dispW=640
dispH=480
flip=2
webCam = cv2.VideoCapture('/dev/video2')
webCam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
webCam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
while True:
    _, frame3 = webCam.read()
    cv2.imshow('webCam',frame3)
    cv2.moveWindow('webCam',0,0)
    gray=cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayCam', gray)
    cv2.moveWindow('grayCam',0,510)
    smallColor = cv2.resize(frame3, (320,240))
    cv2.imshow('smallColor', smallColor)
    cv2.moveWindow('smallColor',700,0)

    if cv2.waitKey(1)==ord('q'):
        break
webCam.release()
cv2.destroyAllWindows()