import cv2
import mediapipe
from cvzone.HandTrackingModule import HandDetector
import pyautogui

camera = cv2.VideoCapture(0) #tek kamera oldugundan sifir indexini atadik
detector = HandDetector(detectionCon=0.8, maxHands=1)
camera.set(3, 500)
camera.set(4, 500)

screen_width, screen_height = pyautogui.size()
index_y = 0
while True:##surekli frame almak icin sonsuz dongu olusturduk


    # kamerayi sectikten sonra frame'leri yakalamamiz gerekiyor
    success, img = camera.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img) # with draw

    if hands:
        for hand in hands:
            for id, hand.landmarks in enumerate(hand.landmarks):
                x = int(hand.landmarks.x * frame_width)
                y = int(hand.landmarks.y * frame_heigth)
                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 0))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_heigth * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 0))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_heigth * y

                    if abs(index_y - thumb_y) < 25:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)


    cv2.imshow("camera window", img)
    ## iki parametre ==> bir pencere ismi, digeri de gosterilecek nesne

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        ##bizden 1 ms boyunca input bekleyecek.Eger input olmazsa dongude basa donup yeniden okumaya baslayacak
        #waitKey 32 bitlik deger dondurur ve biz bunu 0xFF ile 8bit'e dondurup kontrol ediyoruz
        # q'ya basınca kapatiyoruz

