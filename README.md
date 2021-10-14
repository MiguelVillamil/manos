# Reconocimiento manos (Reto Tik tok)
Como todos saben, la pandemia y posterior cuarentena cambió el mundo y la manera de ver el mundo y el entretenimiento, una de esas formas fue Tik Tok que por medio de diferentes retos,
bailes y "trends" fue la principal manera de pasar el encierro obligatorio para muchas personas. Uno de estos trends en especifico fue el 
[emoji challenge](https://youtu.be/jboo0vWe4_U?t=34) o [hands challenge](https://youtu.be/jboo0vWe4_U?t=93) que consistía en hacer los siguientes emojis al ritmo de una canción de moda en el momento.

![emojis del reto](https://ih1.redbubble.net/image.1189462814.0273/st,small,507x507-pad,600x600,f8f8f8.jpg)

Al ejecutar el programa, una ventana o frame aparece con 3 secciones:
* Puntaje obtenido por el jugador.
* Emojis que el jugador tendrá que imitar.
* Imagen de la cámara del jugador.

![Primera reacción del programa](https://cdn.discordapp.com/attachments/618970096815046659/898065149481615370/unknown.png)

Apenas aparece esta ventana el jugador puede empezar a jugar, esto al **recrear** con sus manos los emojis que vayan apareciendo en la barra superior (pueden salir 7 emojis de manera
 aleatoria), cada vez que recrea un emoji de manera exitosa se le otorgan los puntos correspondientes de la siguiente manera:
* Si hace bien un emoji tiene 10 puntos.
* Si termina todos los emoji se le dan 100 puntos de bonificación.
* Si no recrea el emoji con exactitud el juego se acaba y pierde sus puntos.

![Primera reacción del programa](https://cdn.discordapp.com/attachments/618970096815046659/898064838645940245/unknown.png)

## ¿Cómo se diferencia cada gesto?
1. Diferenciar entre mano izquierda y derecha.
  * 
2. Extraer las coordenadas de cada punto de la mano en la posicion deseada.
    ![landmarks](https://mediapipe.readthedocs.io/en/latest/_images/hand_landmarks.png)
  * Gracias a la libreria mediapipe se pueden modelar las manos como un conjunto de puntos, estos puntos se encuentran en una posicion diferente dependiendo de la forma que la mano
  tenga en ese momento, con estos puntos se trabajó.
3. Con las coordenadas, definir cada emoji como un conjunto de coordenadas.
