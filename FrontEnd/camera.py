import cv2
import mediapipe
from math import sqrt

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

            #arms
            arm_len = abs(right_shoulder.x - left_shoulder.x)*1.25
            upperarm_len = abs(right_shoulder.x - left_shoulder.x)*0.6

            rupperarm_len = self.dist(right_shoulder, right_elbow)
            rforearm_len = self.dist(right_fist, right_elbow)
            rshown_len = rupperarm_len + rforearm_len

            lupperarm_len = self.dist(left_shoulder, left_elbow)
            lforearm_len = self.dist(left_fist, left_elbow)
            lshown_len = lupperarm_len + lforearm_len

            arm_len = max(arm_len, rshown_len, lshown_len)

            
            right_elbow_z = -max( upperarm_len - rupperarm_len, 0) / upperarm_len
            right_fist_z = -max(arm_len - rshown_len, 0) / arm_len
            
            left_elbow_z = -max(upperarm_len - lupperarm_len, 0) / upperarm_len
            left_fist_z = -max(arm_len - lshown_len, 0) / arm_len
            
            '''
            #  left
            lz_len = sqrt(abs(arm_len*arm_len - lshown_len*lshown_len))
            left_fist_z = -lz_len
            left_elbow_z = -(lz_len*(lupperarm_len/lshown_len))


            #  left
            rz_len = sqrt(abs(arm_len*arm_len - rshown_len*rshown_len))
            right_fist_z = -rz_len
            right_elbow_z = -(rz_len*(rupperarm_len/rshown_len))
            '''
            lfist_z = left_fist_z
            lelbow_z = left_elbow_z
            rfist_z = right_fist_z
            relbow_z = right_elbow_z


            return {
                "chest": (chest_x, chest_y, 0),# chest_z),
                  "right shoulder": (right_shoulder.x, right_shoulder.y, 0),# right_shoulder.z),
                    "right elbow": (right_elbow.x, right_elbow.y, 0.1),#  -abs(right_elbow.z - chest_z)),# relbow_z),
                      "right fist": (right_fist.x, right_fist.y, 0.1),#  -abs(right_fist.z - chest_z)),#  rfist_z),
                  "left shoulder": (left_shoulder.x, left_shoulder.y, 0),# left_shoulder.z),
                    "left elbow": (left_elbow.x, left_elbow.y, 0.1),# -abs(left_elbow.z - chest_z)),# lelbow_z),
                      "left fist": (left_fist.x, left_fist.y, 0.1),#-abs(left_fist.z - chest_z)),#lfist_z),
                "head": (head.x, head.y, -0.2),# head.z),
                #"head start": head_start,#(head.x, head.y, head.z),
            }

          

        return {}
        
    def close(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def dist(self, p1, p2) -> float:
        return sqrt((p2.x-p1.x)*(p2.x-p1.x) + (p2.y-p1.y)*(p2.y-p1.y))


