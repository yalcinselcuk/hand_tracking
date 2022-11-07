import cv2
import mediapipe
from cvzone.HandTrackingModule import HandDetector


camera = cv2.VideoCapture(0) #tek kamera oldugundan sifir indexini atadik
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:##surekli frame almak icin sonsuz dongu olusturduk


    # kamerayi sectikten sonra frame'leri yakalamamiz gerekiyor
    success, img = camera.read()

    hands, img = detector.findHands(img) # with draw
    #hands = detector.findHands(img, draw=False) # no draw

    cv2.imshow("camera window", img)
    ## iki parametre ==> bir pencere ismi, digeri de gosterilecek nesne

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        ##bizden 1 ms boyunca input bekleyecek.Eger input olmazsa dongude basa donup yeniden okumaya baslayacak
        #waitKey 32 bitlik deger dondurur ve biz bunu 0xFF ile 8bit'e dondurup kontrol ediyoruz
        # q'ya basınca kapatiyoruz

