import time

import cv2
import mediapipe as mp


class HandTrack:

    def __init__(self, static_image_mode=False, max_num_hands=2, model_complexity=1,
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.results_hands = None
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_tracking_confidence = min_tracking_confidence
        self.min_detection_confidence = min_detection_confidence
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.static_image_mode, self.max_num_hands, self.model_complexity,
                                         self.min_detection_confidence, self.min_tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame, draw=False):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results_hands = self.hands.process(rgb_frame)
        if self.results_hands.multi_hand_landmarks:
            for hand_landmarks in self.results_hands.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return frame

    def get_landmarks(self, frame, handno=0):
        ll=[]
        if self.results_hands.multi_hand_landmarks:
            myhand = self.results_hands.multi_hand_landmarks[handno]
            for id, landmark in enumerate(myhand.landmark):
                h, w, c = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                ll.append([id, cx, cy])
                if id % 4 == 0 and id != 0:
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return ll


# <-------------------------------------------- Resizing the window  (Not recommend as it reduces the frame rate)
# cv2.namedWindow("Images", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Images", 600,600)
def main():
    prev_time = 0
    curr_time = 0
    cap = cv2.VideoCapture(0)
    # Creating the object
    detector = HandTrack()
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        frame = detector.find_hands(frame, draw=True)
        ll = detector.get_landmarks(frame)
        if len(ll):
            print(ll[4])
        # Creating the FPS meter
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time + 1e-10)
        prev_time = curr_time
        cv2.putText(frame, f'{int(fps)}', (10, 70), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 255),
                    thickness=4)

        cv2.imshow("Images", frame)

        key = cv2.waitKey(10)
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

    # results_pose = poses.process(rgb_frame)
    #
    # if results_pose.pose_landmarks:
    #     for id, landmark in enumerate(results_pose.pose_landmarks.landmark):
    #         if 0 <= id <= 10:
    #             continue  # Skip drawing landmarks with IDs between 0 and 10
    #         h, w, c = frame.shape  # Get the height, width, and channels of the frame
    #         cx, cy = int(landmark.x * w), int(landmark.y * h)  # Convert normalized coordinates to pixel values
    #         cv2.circle(frame, (cx, cy), 5, (255, 0, 255), -1)
    #         cv2.line(frame, (cx, cy), cy, (0, 0, 0), 5)
    #         # mp_draw.draw_landmarks(frame, results_pose.pose_landmarks, my_pose.POSE_CONNECTIONS)
