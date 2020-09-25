import cv2

dispW=640
dispH=480
flip=2
webCam = cv2.VideoCapture('/dev/video2')
webCam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
webCam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
dx = 2
dy = 2
posX = 0
posY = 0
while True:
    _, frame = webCam.read()
    frame = cv2.rectangle(frame,(posX,posY),(posX+30,posY+30),(0,0,255),-1)
    cv2.imshow('webCam',frame)
    cv2.moveWindow('webCam',0,0)
    posX += dx
    posY += dy
    if posX + 30 > dispW or posX < 0:
        dx = dx * (-1)
    if posY + 30 > dispH or posY < 0:
        dy = dy * (-1) 
    if cv2.waitKey(1)==ord('q'):
        break
webCam.release()
cv2.destroyAllWindows()