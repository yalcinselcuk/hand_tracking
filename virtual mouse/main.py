import cv2
import mediapipe
import pyautogui

mpHands = mediapipe.solutions.hands
hand_detector = mpHands.Hands(max_num_hands=1)
drawing_utils = mediapipe.solutions.drawing_utils

camera = cv2.VideoCapture(0)
camera.set(3, 500)
camera.set(4, 500)

screen_width, screen_height = pyautogui.size()

index_y = 0
while True:
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    frame_heigth, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hand_detector.process(rgb_frame)
    handes = result.multi_hand_landmarks
    if handes:
        for hand in handes:
            drawing_utils.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)
            landmarks = hand.landmark
            for id, landmarks in enumerate(landmarks):
                x = int(landmarks.x * frame_width)
                y = int(landmarks.y * frame_heigth)
                if id == 12:
                    cv2.circle(img = frame, center=(x, y), radius = 15, color = (0, 255, 0))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_heigth * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 8:
                    cv2.circle(img = frame, center=(x, y), radius = 15, color = (0, 255, 0))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_heigth * y

                    if abs(index_y - thumb_y) < 25:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)
    cv2.imshow("camera", frame)
    cv2.waitKey(1)