
import cv2
import mediapipe as mp

## initialize pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
def update():
        if not cap.isOpened():
            return 
    # read frame
        _, frame = cap.read()
    #try:
        # resize the frame for portrait video
        frame = cv2.resize(frame, (600, 400))
        # convert to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         
        # process the frame for pose detection
        pose_results = pose.process(frame_rgb)
        # print(pose_results.pose_landmarks)
         
        # draw skeleton on the frame
        mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        #print(type(frame))
        # display the frame
        #print(pose_results.pose_landmarks.landmark[16])
        if pose_results.pose_landmarks is not None:

            #print("HI")
            lm = pose_results.pose_landmarks.landmark[16]
        #print(lm.x)
            frame = cv2.circle(frame, (int(lm.x*600), int(lm.y*400)), 20, (0,0,255), -1)
        #frame = cv2.circle(frame, (63, 63), 63, (0, 0, 255), -1)
        cv2.imshow('Output', frame)
    #except:
        #break
for i in range(10000):
    update()
    if cv2.waitKey(1) == ord('q'):
        break
          
cap.release()
cv2.destroyAllWindows()
