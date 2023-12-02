# import time
#
# import cv2
# import socket
# from Custom_Handtracker import HandTrack
#
#
# # <-------------------------------------------- Resizing the window  (Not recommend as it reduces the frame rate)
#
#
# def main():
#     prev_time = 0
#     curr_time = 0
#     cap = cv2.VideoCapture(0)
#     # Creating the object
#     detector = HandTrack()
#
#     # Communication Part
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM is used for UDP transferring
#     serverAddress = ("127.0.0.1", 5052)
#
#     while True:
#         ret, frame = cap.read()
#         # frame = cv2.flip(frame, 1)
#         frame = detector.find_hands(frame, draw=True)
#         ll = detector.get_landmarks(frame)
#         one_d_ll = []
#         # Since this landmark list is 2d, but we need 1-D for our game engine hence let's convert them
#         if len(ll):
#             for lm in ll:
#                 # Subtracting height from y-axis as game engine works opposite to opencv
#                 one_d_ll.extend([lm[0], frame.shape[0] - lm[1], lm[2]])
#             # print(one_d_ll)
#             sock.sendto(str.encode(str(one_d_ll)), serverAddress)
#         # Creating the FPS meter
#         curr_time = time.time()
#         fps = 1 / (curr_time - prev_time + 1e-10)
#         prev_time = curr_time
#         cv2.putText(frame, f'{int(fps)}', (10, 70), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 255),
#                     thickness=4)
#
#         cv2.imshow("Images", frame)
#
#         key = cv2.waitKey(10)
#         if key == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     main()


import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()