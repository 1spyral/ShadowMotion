import cv2
import mediapipe

## initialize pose estimator
mp_drawing = mediapipe.solutions.drawing_utils
mp_pose = mediapipe.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

class Camera:
     
    def __init__(self):
          
        self.cam = cv2.VideoCapture(0)

    def update(self):

        if not self.cam.isOpened():
            return 
        # read frame
        _, frame = self.cam.read()
         
        # process the frame for pose detection
        pose_results = pose.process(frame)
         
        if pose_results.pose_landmarks is not None:
            right_fist = pose_results.pose_landmarks.landmark[16]
            right_elbow = pose_results.pose_landmarks.landmark[14]
            left_fist = pose_results.pose_landmarks.landmark[15]
            left_elbow = pose_results.pose_landmarks.landmark[13]
            head = pose_results.pose_landmarks.landmark[0]
            left_shoulder = pose_results.pose_landmarks.landmark[11]
            right_shoulder = pose_results.pose_landmarks.landmark[12]
            chest_x = (left_shoulder.x + right_shoulder.x) / 2
            chest_y = (left_shoulder.y + right_shoulder.y) / 2
            chest_z = (left_shoulder.z + right_shoulder.z) / 2

            return [
                (right_fist.x, right_fist.y, right_fist.z),
                (right_elbow.x, right_elbow.y, right_elbow.z),
                (left_fist.x, left_fist.y, left_fist.z),
                (left_elbow.x, left_elbow.y, left_elbow.z),
                (head.x, head.y, head.z),
                (chest_x, chest_y, chest_z),
            ]

        return []
        
    def close(self):
        self.cam.release()
        cv2.destroyAllWindows()
