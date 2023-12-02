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
        ll = []
        if self.results_hands.multi_hand_landmarks:
            myhand = self.results_hands.multi_hand_landmarks[handno]
            for id, landmark in enumerate(myhand.landmark):
                h, w, c = frame.shape
                cx, cy, cz = int(landmark.x * w), int(landmark.y * h), int(landmark.z * w)
                ll.append([cx, cy, cz])
                if id % 4 == 0 and id != 0:
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return ll