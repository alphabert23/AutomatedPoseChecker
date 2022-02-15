import cv2
import time
import PoseDetectionModule as pm

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)    

cap = cv2.VideoCapture('videos/7.mp4')
prevTime = 0
detector = pm.PoseDetector()

while True:
    #capture frame by frame
    success, frame = cap.read()

    #function rescale frame is called to downscale the video
    frame = rescale_frame(frame, percent= 30)

    frame = detector.findPose(frame)
    lmList = detector.findPosition(frame)
    print(lmList)

    #to get the FPS of the video
    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    cv2.putText(frame, str(int(fps)), (35,50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    #to display the captured frame(s)
    cv2.imshow("Image", frame)
        
    #to exit from the while loop
    if cv2.waitKey(20) & 0xFF == ord('q'):
         break

#the capture will be released after everything is done
cap.release()
cv2.destroyAllWindows()