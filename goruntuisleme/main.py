import cv2
import mediapipe

camera = cv2.VideoCapture(0) #tek kamera oldugundan sifir indexini atadik
mpHands = mediapipe.solutions.hands##elimizde noktalar cizmek icin kullanicaz
hands = mpHands.Hands()# el objesi olusturmus oluyoruz ve icine de elde ettigimiz frame'i gondericez
#o da frame icindeki eli tarayacak ve noktalari gondericek



mpDraw = mediapipe.solutions.drawing_utils
## elde ettigimiz noktalari cam ustune bastirmak icin kullaniyoruz

while True:##surekli frame almak icin sonsuz dongu olusturduk


    # kamerayi sectikten sonra frame'leri yakalamamiz gerekiyor
    success, img = camera.read()
    ##read() metodu iki sey dondurur
    # bir boolean bir de img dondurur ==> yakalanan frame'i
    # cam bir sey yakaladiysa true, yoksa false dondurur success'e

    #elde ettigimiz resmi RGB formata donusturmemiz lazim.Bizim resmimiz BGR formatinda
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#resim, format donusumu

    hlms = hands.process(imgRGB)
    #el icindeki noktalari bize bulucak

    height, width, channel = img.shape
    #penceremin yuksekligi, genisligi, channel'ı
    #bunu yapmamizin nedeni parmaklarimizin olculerini bulmak icin koordinat*pencere boyutu yapmak
    if hlms.multi_hand_landmarks:
        for handlanmarks in hlms.multi_hand_landmarks:# 21 elemanli bir array.Elde 21 nokta var cunku

            for fingerNum, landmark in enumerate(handlanmarks.landmark):
                positionX, positionY =  int(landmark.x * width), int(landmark.y * height)
                #print(fingerNum, landmark)

                #parmaklara nokta num'larini yazdirdik
                #bunu yapmamizin amaci noktalara gore kosul yazmak ve noktalari net gormek
                cv2.putText(img, str(fingerNum), (positionX, positionY), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 0), 2)

            mpDraw.draw_landmarks(img, handlanmarks, mpHands.HAND_CONNECTIONS)#alacagi degerler : frame, landmarkslist, connections
            #boylelikle ellerimiz arasindaki noktalarin cizgilerini gorebiliyor olucaz

    cv2.imshow("camera window", img)
    ## iki parametre ==> bir pencere ismi, digeri de gosterilecek nesne

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        ##bizden 1 ms boyunca input bekleyecek.Eger input olmazsa dongude basa donup yeniden okumaya baslayacak
        #waitKey 32 bitlik deger dondurur ve biz bunu 0xFF ile 8bit'e dondurup kontrol ediyoruz
        # q'ya basınca kapatiyoruz

