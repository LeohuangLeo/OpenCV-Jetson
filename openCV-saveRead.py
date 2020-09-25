import cv2

dispW=640
dispH=480
flip=2
# webCam = cv2.VideoCapture('/dev/video2')
webCam = cv2.VideoCapture('videos/myCam.avi')
webCam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
webCam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
# outVid = cv2.VideoWriter('videos/myCam.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (dispW,dispH))
while True:
    _, frame = webCam.read()
    cv2.imshow('webCam',frame)
    cv2.moveWindow('webCam',0,0)
    # outVid.write(frame)
    if cv2.waitKey(50)==ord('q'):
        break
webCam.release()
outVid.release()
cv2.destroyAllWindows()