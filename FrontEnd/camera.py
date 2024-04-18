import cv2
import mediapipe

class Camera:
     
    def __init__(self):
        ## initialize pose estimator
        self.mp_drawing = mediapipe.solutions.drawing_utils
        self.mp_drawing = mediapipe.solutions.drawing_utils
        self.mp_pose = mediapipe.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.cam = cv2.VideoCapture(0)

    def update(self):

        if not self.cam.isOpened():
            return 
        # read frame
        a, frame = self.cam.read()
         
        # process the frame for pose detection
        pose_results = self.pose.process(frame)
        self.mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        self.mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
         
        cv2.imshow("a",frame) 
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

            mouth_a = pose_results.pose_landmarks.landmark[10]
            mouth_b = pose_results.pose_landmarks.landmark[9]
            head_start = ((mouth_a.x + mouth_b.x) / 2, (mouth_a.y + mouth_b.y) / 2, 5) # (mouth_a.z + mouth_b.z) / 2)

            return {
                "chest": (chest_x, chest_y, chest_z),
                  "right shoulder": (right_shoulder.x, right_shoulder.y, right_shoulder.z),
                    "right elbow": (right_elbow.x, right_elbow.y, right_elbow.z),
                      "right fist": (right_fist.x, right_fist.y, right_fist.z),
                  "left shoulder": (left_shoulder.x, left_shoulder.y, left_shoulder.z),
                    "left elbow": (left_elbow.x, left_elbow.y, left_elbow.z),
                      "left fist": (left_fist.x, left_fist.y, left_fist.z),
                "head": (head.x, head.y, head.z),
                #"head start": head_start,#(head.x, head.y, head.z),
            }

          

        return {}
        
    def close(self):
        self.cam.release()
        cv2.destroyAllWindows()


