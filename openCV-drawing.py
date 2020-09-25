import cv2

dispW=640
dispH=480
flip=2
webCam = cv2.VideoCapture('/dev/video2')
webCam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
webCam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
while True:
    _, frame = webCam.read()
    frame = cv2.rectangle(frame,(140,100),(180,140),(0,0,255),-1)
    # frame = cv2.circle(frame,(320,240),50,(244,244,244),-4)
    # fnt = cv2.FONT_HERSHEY_DUPLEX
    # frame = cv2.putText(frame,'My First Text',(300,300),fnt,1,(255,0,255),2)
    # frame = cv2.line(frame,(10,10),(60,60),(0,0,0),4)
    # frame = cv2.arrowedLine(frame,(10,470),(630,10),(255,255,0),3)
    cv2.imshow('webCam',frame)
    cv2.moveWindow('webCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
webCam.release()
cv2.destroyAllWindows()