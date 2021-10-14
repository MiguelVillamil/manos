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
1. Cabe resaltar que para reconocer las manos primero se realizó un tratado de imagenes el cual fue:
  * invertir la imagen
  * convertirla a RGB
  * escalar a la pantalla con ayuda de imutils
2. Para el reconocimiento de las manos utilizamos la librería mediapipe. Cada gesto tiene su respectivo método el cual reconoce, diferencia y da la dirección del flujo del programa para el sistema de puntos, para cada método se siguió el siguiente procedimiento:
    ![landmarks](https://mediapipe.readthedocs.io/en/latest/_images/hand_landmarks.png)
  * Reconocer las manos
  * Convertir las coordenadas de cada punto a pixeles escalando la pantalla y asignándole este valor a diferentes variables separándolas por puntas y mitad de los dedos
  * Reconocer si la mano es derecha o izquierda para la selección del pulgar
  * Evaluar los puntos de rigor que cada gesto tiene para seleccionar si es o no este
3. Si la posición de manos del jugador es correcta se le sumara en el sistema de puntos el puntaje y así sucesivamente hasta que el usuario falle en algún momento.
