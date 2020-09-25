import cv2
print(cv2.__version__)

dispW=640
dispH=480
flip=2

# camSet='nvarguscamerasrc sensor-id=0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# camSet2='nvarguscamerasrc sensor-id=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam=cv2.VideoCapture(camSet)
# cam2=cv2.VideoCapture(camSet2)
webCam = cv2.VideoCapture('/dev/video2')
webCam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
webCam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
while True:
    # _, frame = cam.read()
    # _, frame2 = cam2.read()
    # cv2.imshow('myCam',frame)
    # cv2.imshow('myCam2',frame2)
    # cv2.moveWindow('myCam',0,0)
    # cv2.moveWindow('myCam2',100,100)
    _, frame3 = webCam.read()
    cv2.imshow('webCam',frame3)
    cv2.moveWindow('webCam',0,0)
    gray=cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayCam', gray)
    cv2.moveWindow('grayCam',0,500)
    if cv2.waitKey(1)==ord('q'):
        break
# cam.release()
# cam2.release()
webCam.release()
cv2.destroyAllWindows()
