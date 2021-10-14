import cv2
import random

class emojiBar():
    
    
    
    
    
    def __init__(self,emojilist=[1,2,3,4,5],infinito=True):
        self.emojiList= emojilist
        self.puntos=0
        self.imageBar= None
        self.ultimo=0
        
        
        self.actualizar()
        
    def actualizar(self):
        emojiPrint = []
        for emoji in self.emojiList:
            if(emoji==0): #vacio=0
                vacio= cv2.imread("emoji_vacio.png")
                emojiPrint.append(vacio)
                
            elif(emoji==1): #hi5=1
                hi5=cv2.imread("emoji_hi5.png")
                emojiPrint.append(hi5)
                
            elif(emoji==2): #like=2
                like=cv2.imread("emoji_like.png")
                emojiPrint.append(like)
                
            elif(emoji==3): #lose=3
                lose=cv2.imread("emoji_lose.png")
                emojiPrint.append(lose)
                
            elif(emoji==4): #nea=4
                nea=cv2.imread("emoji_nea.png")
                emojiPrint.append(nea)
                
            elif(emoji==5): #ok=5
                ok=cv2.imread("emoji_ok.png")
                emojiPrint.append(ok)
                
            elif(emoji==6): #paece=6
                peace= cv2.imread("emoji_peace.png")
                emojiPrint.append(peace)
                
            elif(emoji==7): #puño=7
                puno=cv2.imread("emoji_puno.png")
                emojiPrint.append(puno)
                
        barra=cv2.hconcat(emojiPrint)
        print(type(barra))
        score= cv2.imread("barrapunto.png")
        height, width, _  = score.shape
        cv2.putText(score, "puntos: "+ str(self.puntos), (int(0.05*width), int(0.6*height)),
                        cv2.FONT_HERSHEY_PLAIN, 3, (0,255, 0), 2, ) 
        self.imageBar= cv2.vconcat([score,barra])
        
        
        #self.mostrar()
        return self.imageBar
           
                
    def buscaEmoji(self, emojinum):
            escribir=True        
            for x in range (len(self.emojiList)):
                if (self.emojiList[x] != emojinum and self.emojiList[x] != 0 ):
                    escribir = False
                    if(emojinum != self.ultimo):
                        self.puntos=0
                
                if self.emojiList[x] == emojinum and escribir == True:
                    escribir=False
                    self.ultimo = emojinum
                    self.emojiList[x]=0
                    self.puntos=self.puntos+10 
                    
                    print(self.emojiList)
                    if (self.emojiList==[0,0,0,0,0]):
                        self.emojiList=self.randomEmoji()
                        
                    
            return self.actualizar()        
                    
    
    def randomEmoji(self):
        lista = [0] * 5
        for i in range(5):
            lista[i] = random.randint(1, 7)
        return lista
        
        
    def mostrar(self):
        cv2.imshow("image", self.imageBar)
        if(cv2.waitKey(0) and 0xFF == 27):
            
            cv2.destroyAllWindows

    def mostrarBarra(self):
        return self.imageBar
                 
            
                 
barra=emojiBar()
#print(barra.randomEmoji())



#barra.buscaEmoji(1)
    
              