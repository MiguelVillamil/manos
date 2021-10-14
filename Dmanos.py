import cv2 
import mediapipe as mp
from mediapipe.python.solutions.drawing_styles import _HAND_LANDMARK_STYLE
import imutils
import sys, pygame
from Emoji_bar import emojiBar as eb 

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Blablabla.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

class detector():
    
    def __init__(self):
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.image = None
        self.barra = eb([1,2,3,4,5])
        self.imageBarra= self.barra.mostrarBarra()
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
    
    def mostrar(self,imagen):
        cv2.imshow("image", imagen)
        if(cv2.waitKey(0) and 0xFF == 27):
            self.cap.release()
            cv2.destroyAllWindows
    
    def mostrarvideo(self,imagen):
        cv2.imshow("image", imagen)
        if(cv2.waitKey(1) & 0xFF == 27):
            self.cap.release()
            cv2.destroyAllWindows
            return True
            
        
    def hi5(self, hand_puntos,width,height,tipo):
        
        #Puntas de los dedos
        
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
        x4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
        y8 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
        
        y12 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
        
        y16 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
        
        y20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * height)
        
        #mitad de los dedos 
        
        
        
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        
        x3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * width)
        
        y6 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * height)
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        
        if(y4<y3 and y8<y6 and y12<y10 and y16<y14 and y20<y18 and y4>y12):
            if (tipo=="Left"):
                if (x4>x3):
                    print("hi5")    
                    cv2.putText(self.image, "hi5", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(1)
            elif (tipo=="Right"):
                
                if (x4<x3):
                    print("hi5")    
                    cv2.putText(self.image, "hi5", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(1)
        
       
        
    def peace(self, hand_puntos,width,height,tipo):
            
        #Puntas de los dedos
        
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
        x4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
        y8 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
        
        y12 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
        
        y16 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
        
        y20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * height)
        
        #mitad de los dedos 
        
        
        
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        
        x3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * width)
        
        y6 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * height)
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        
        if(y8<y6 and y12<y10 and y16>y14 and y20>y18):
            if (tipo=="Left"):
                if (x4<x3):
                    print("paz")    
                    cv2.putText(self.image, "peace", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(6)
            
            elif (tipo=="Right"):
                
                if (x4>x3):
                    print("paz")    
                    cv2.putText(self.image, "peace", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(6)
                    
    def nea(self, hand_puntos,width,height,tipo):
        
        #nudillos
        
        y5 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * height)
        
        y9 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * height)
        
        y13 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * height)
        
        y17 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * height)
        
        #mitad de los dedos 
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)

        y6 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * height)

        #punta de los dedos 
        
        y8 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
        
        y12 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
        
        y16 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * height)

        y20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * height)
        
        #meÃ±ique 
        
        x18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * width)
        x20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * width)
        
        #PULGAR 
        
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
        y2 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_IP].y * height)
        
        
        
        if( y20<y18 and y6<y8 and y10<y12 and y14<y16 and y4<y3):
            if (tipo=="Left"):
                if(x18>x20):    
                    print("nea")    
                    cv2.putText(self.image, "nea", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(4)
            
            elif (tipo=="Right"):
                
                if(x18>x20):
                    print("nea")    
                    cv2.putText(self.image, "nea", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(4)
                

    def puño(self, hand_puntos,width,height,tipo):
        
        #nudillos
        
        y5 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * height)
        
        y9 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * height)
        
        y13 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * height)
        
        y17 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * height)
        
        
        
        #mitad de los dedos 
        
        
        
        
        
        y6 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * height)
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        
        
        
        #pulgar
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
        
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        
        
        if(y5<y6 and y9<y10 and y13<y14 and y17<y18 and y4>y3):
            if (tipo=="Left"):
                
                    print("puño")    
                    cv2.putText(self.image, "pu"+u'\xed'+"o", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(7)
            elif (tipo=="Right"):
                
                
                    print("puño")    
                    cv2.putText(self.image, "pu"+u'\xed'+"o", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(7)
    def like(self, hand_puntos,width,height,tipo):
        
        #nudillos
        
        y5 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * height)
        
        y9 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * height)
        
        y13 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * height)
        
        y17 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * height)
        
        #mitad de los dedos 
        
        
        
        
        
        
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        
        #PULGAR 
        
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
        
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        
        #meñique 
        x18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        x20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * height)
        
        if(y5<y9 and y5<y13 and y5<y17 and y4<y3 and y5<y10 and y5<y14 and y5<y18):
            if (tipo=="Left"):
                if(x18<x20):
                    print("like")    
                    cv2.putText(self.image, "like", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(2)
            
            elif (tipo=="Right"):
                
                if(x18>x20):
                    print("like")    
                    cv2.putText(self.image, "like", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(2)
                    
    
                    
    def lose(self, hand_puntos,width,height,tipo):
        
        #Puntas de los dedos
        
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
        x4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
        y8 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
        
        y12 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
        
        y16 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
        
        y20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * height)
        
        #mitad de los dedos 
        
        
        
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        
        x3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * width)
        
        y6 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * height)
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        
        if(y4<y3 and y8<y6 and y12>y10 and y16>y14 and y20>y18):
            if (tipo=="Left"):
                if (x4>x3):
                    print("lose")    
                    cv2.putText(self.image, "lose", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(3)
            
            elif (tipo=="Right"):
                
                if (x4<x3):
                    print("lose")    
                    cv2.putText(self.image, "lose", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(3)
        
    def ok(self, hand_puntos,width,height,tipo):
            
        #Puntas de los dedos
        
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height) 
        x4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
        y8 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
        
        y12 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
        
        y16 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
        
        y20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * height)
        
        #mitad de los dedos 
        
        
        
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        
        x3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * width)
        
        y6 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * height)
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        
        if(y4<y3 and y8>y6 and y12<y10 and y16<y14 and y20<y18 and y4>y12):
            if (tipo=="Left"):
                #if (x4>x3):
                    print("ok")    
                    cv2.putText(self.image, "ok", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(5)
            elif (tipo=="Right"):
                
                #if (x4<x3):
                    print("ok")    
                    cv2.putText(self.image, "ok", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
                    self.imageBarra=self.barra.buscaEmoji(5)
                    
    """def swag(self, hand_puntos,width,height,tipo):
            
        #Puntas de los dedos
        
        y4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
        x4 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
        y8 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
        
        y12 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
        
        y16 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
        
        y20 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * height)
        
        #mitad de los dedos 
        
        
        
        y3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * height)
        
        x3 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * width)
        
        y6 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * height)
        
        y10 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * height)
        
        y14 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * height)
        
        y18 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * height)
        
        if(y8<y6 and y12<y10 and y16>y14 and y20<y18):
            if (tipo=="Left"):
                if (x4<x3):
                    print("swag")    
                    cv2.putText(self.image, "swag", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)
            
            elif (tipo=="Right"):
                
                if (x4>x3):
                    print("swag")    
                    cv2.putText(self.image, "swag", (int(0.5*width), int(0.9*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 3)"""
    

 ########################################################################################        
    def manos_imagen(self):
        self.cap.release()
        with self.mp_hands.Hands(static_image_mode = True, max_num_hands=1 ) as hands:
    
            self.image = cv2.imread("mano_nea.jpeg")
            self.image = imutils.resize(self.image, width= 480)
            self.image = cv2.flip(self.image, 1)
            
            height, width, _  = self.image.shape
            
            imagergb= cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            results = hands.process(imagergb)
    
            
            if(results.multi_hand_landmarks is not None):
                #print("HandLansMarks", results.multi_hand_landmarks)
                
                for hand_puntos in results.multi_hand_landmarks :
                    print(hand_puntos)
                    
                    self.mp_drawing.draw_landmarks(self.image, hand_puntos, self.mp_hands.HAND_CONNECTIONS)
                    
                    tipoMano= str(results.multi_handedness)
                    if ("Left" in tipoMano):
                        tipoMano = "Left"
                        print("Left")
                        
                    if("Right" in tipoMano):
                        tipoMano= "Right"
                        print ("Right")    
                    #print("Handedness: ", results.multi_handedness)
                    
                    
                    """#prueba de coords
                    x1 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
                    y1 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
                    cv2.circle(self.image, (x1, y1), 3,(255,0,0),3)
                    
                    #fin de la prueba"""
                    
                    self.hi5(hand_puntos,width,height,tipoMano)
                    self.peace(hand_puntos,width,height,tipoMano)
                    self.nea(hand_puntos,width,height,tipoMano)
                    self.puño(hand_puntos,width,height,tipoMano)
                    self.like(hand_puntos,width,height,tipoMano)
                    self.lose(hand_puntos,width,height,tipoMano)
                    self.ok(hand_puntos,width,height,tipoMano)
                    #self.swag(hand_puntos,width,height,tipoMano)
                    
                         
                
            #self.image = cv2.flip(self.image, 1)
            self.mostrar(self.image)
    
    def manos_cam(self):
         with self.mp_hands.Hands(static_image_mode = False, max_num_hands=1, min_detection_confidence=0.7 ) as hands:       
          while True:
            ret, self.image = self.cap.read()
            if (ret == False):
                break
            self.image = imutils.resize(self.image, width= 520)
            height, width, _ = self.image.shape
            self.image = cv2.flip(self.image, 1)
            
            self.imageBarra = imutils.resize(self.imageBarra,width=width)
            self.image= cv2.vconcat([self.imageBarra,self.image]) 
            frame_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            
            if(results.multi_hand_landmarks is not None):
                #print("HandLansMarks", results.multi_hand_landmarks)
                
                for hand_puntos in results.multi_hand_landmarks :
                    #print(hand_puntos)
                    
                    self.mp_drawing.draw_landmarks(self.image, hand_puntos, self.mp_hands.HAND_CONNECTIONS)
                    
                    
                    print(self.image.shape)
                    print(self.imageBarra.shape)
                    tipoMano= str(results.multi_handedness)
                    if ("Left" in tipoMano):
                        tipoMano = "Left"
                        print("Left")
                        
                    if("Right" in tipoMano):
                        tipoMano= "Right"
                        print ("Right")  
                    
                    
                    """#prueba de coords
                    x1 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
                    y1 = int(hand_puntos.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)
                    cv2.circle(self.image, (x1, y1), 3,(255,0,0),3)
                    
                    #fin de la prueba"""
                    
                    self.hi5(hand_puntos,width,height,tipoMano)
                    self.peace(hand_puntos,width,height,tipoMano)
                    self.nea(hand_puntos,width,height,tipoMano)
                    self.puño(hand_puntos,width,height,tipoMano)
                    self.like(hand_puntos,width,height,tipoMano)
                    self.lose(hand_puntos,width,height,tipoMano)
                    self.ok(hand_puntos,width,height,tipoMano)
                    
                    
            if(self.mostrarvideo(self.image)):
                break        
    
    

dt = detector()
#dt.manos_imagen()
dt.manos_cam()

