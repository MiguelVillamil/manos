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

        posi = []
        dedos = []
        eva = [4, 8, 12, 16, 20]

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(
                        color=(0, 255, 255), thickness=3, circle_radius=5),
                    mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=4, circle_radius=5))

                for (id, points) in enumerate(hand_landmarks.landmark):
                    xc = int(points.x * width)
                    yc = int(points.y * height)
                    posi.append([id, xc, yc])
                    # print(posi)

                    if len(posi) == 21:

                        if posi[eva[0]][1] > posi[eva[0]-2][2]:
                            dedos.append(1)
                        else:
                            dedos.append(0)

                        for id in range(1, 5):
                            if posi[eva[id]][2] < posi[eva[id]-2][2]:
                                dedos.append(1)
                            else:
                                dedos.append(0)
                        print(dedos)

                        if dedos[4] == 1 and dedos[0] == 0 and dedos[1] == 0 and dedos[2] == 0 and dedos[3] == 0:
                            cv2.putText(frame, "Bien nea", (245, 375),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

                        if dedos[0] == 0 and dedos[1] == 1 and dedos[2] == 1 and dedos[3] == 1 and dedos[4] == 1:
                            cv2.putText(frame, "Bien puÃ±o", (245, 375),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

                        if dedos[0] == 1 and dedos[1] == 1 and dedos[2] == 1 and dedos[3] == 1 and dedos[4] == 1:
                            cv2.putText(frame, "Bien hi5", (245, 375),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

                        if dedos[0] == 0 and dedos[1] == 1 and dedos[2] == 1 and dedos[3] == 0 and dedos[4] == 0:
                            cv2.putText(frame, "Bien peace", (245, 375),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

                        if dedos[0] == 1 and dedos[1] == 0 and dedos[2] == 0 and dedos[3] == 0 and dedos[4] == 0:
                            cv2.putText(frame, "Bien like", (245, 375),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

                        if dedos[0] == 0 and dedos[1] == 1 and dedos[2] == 1 and dedos[3] == 1 and dedos[4] == 0:
                            cv2.putText(frame, "Bien no me like", (245, 375),
                                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv2.imshow('Juego tik tok', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()