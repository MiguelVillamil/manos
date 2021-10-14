import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:

        while True:
            ret, frame = cap.read()
            if ret == False:
                break

            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            

            results = hands.process(frame_rgb)

            posi=[]
            dedos=[]
            eva = [4, 8, 12, 16, 20]

            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(0,255,255), thickness=3, circle_radius=5),
                        mp_drawing.DrawingSpec(color=(255,0,255), thickness=4, circle_radius=5))
                    
                    for (id, points) in enumerate(hand_landmarks.landmark):
                        xc = int(points.x * width)
                        yc = int(points.y * height)
                        posi.append([id,xc,yc])
                        #print(posi)

                        if len(posi) == 21:
                            '''
                            punto=posi[8]
                            print(punto)
                            x1,y1=punto[1],punto[2]
                            cv2.circle(frame,(x1,y1),5,(255,0,0),cv2.FILLED)
                            '''
                            
                            ## control pulgar
                            classi= str(results.multi_handedness)
                            if ("Left" in classi):                    
                                if posi[eva[0]][1]>posi[eva[0]-1][1]:
                                    dedos.append(1)
                                else:
                                    dedos.append(0)
                            elif("Right"in classi):
                                if posi[eva[0]][1]<posi[eva[0]-1][1]:
                                    dedos.append(1)
                                else:
                                    dedos.append(0)
                                    
                            
                            ## control de dedos - pulgar 
                            for id in range(1,5):
                                if posi[eva[id]][2]<posi[eva[id]-3][2]:
                                    dedos.append(1)
                                else:
                                    dedos.append(0)
                            print(dedos)

                            if dedos[0]==1 :
                                cv2.putText(frame,'bien like',(300,375),cv2.FONT_HERSHEY_PLAIN, 10, (0,255,0),25)



            cv2.imshow('Frame',frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
cap.release()
cv2.destroyAllWindows()