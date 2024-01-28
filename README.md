
# __Los espíritus del pueblo__

Trabajo Práctico Kodland, Enero 2024, Maia Curti Pérez

## Descripción del juego

Cuenta una corta historia de un pueblo que se enfrenta a fenómenos destructivos de la naturaleza: un terremoto, una erupción volcánica y una nube de cenizas. A cada fenómeno se sobrevive de manera diferente.

Para cada partida (los tres fenómenos) el jugador tiene tres vidas. Cuando se pierde la tercera termina la partida.

## Funcionamiento del juego

### Introducción

Al iniciar el programa aparece una animación de modo introductorio, seguida con el menú de inicio. En este se puede iniciar la partida, ver los controles y cerrar el juego.

Antes de comenzar la batalla con cada enemigo aparece una animación introductoria. Una vez termina, en la pantalla permanecen los controles hasta que el jugador confirma que está listo para el enfrentamiento.

Al perder una batalla, el jugador tiene la opción de volver al mismo enemigo o rendirse y pasar al siguiente.

### Primer enemigo: __terremoto__

* __Durante la batalla__: en la pantalla aparecen teclas de una en una. Hay que mantener presionada la tecla en el teclado hasta que aparezca la siguiente. Si no se presiona la tecla de la pantalla antes de que termine el márgen de reacción (1500 milisegundos) se pierde una vida.

* __Para ganar__: mantener, sin perder vidas, seis teclas consecutivas.

### Segundo enemigo: __lava__

* __Durante la batalla__: aparecerán sobre el fondo naranja algunas formas negras. Hay que mantener el puntero del mouse sobre ellas. Si el mouse toca la lava se pierde una vida.

* __Para ganar__: mantener el mouse sobre las formas negras en todo momento.

### Tercer enemigo: __nube__

* __Durante la batalla__: las nubes negras de la pantalla crecen y decrecen con el movimiento del mouse. Hay que mover el mouse amplia y rápidamente para disiparlas. Si el movimiento no es lo suficientemente amplio, las nubes se acercan hasta que se pierde una vida.

* __Para ganar__: mover el mouse con rapidez y amplitud.

### Al ganar o perder la partida

Aparece el menú final, con la imagen correspondiente, y el jugador tiene la opción de volver a jugar (una nueva partida) o cerrar el juego.

## Utilización y funciones

El programa emplea las librerías math, pygame, random y sys.

` python  espiritus.py ` para iniciar el programa.

### Funciones __recurrentes__

` cerrar_juego() `: Cierra la ventana de pygame y termina el programa.

` display_menu() `: Carga y muestra los botones del menú principal.

` jugador_listo() `: Muestra un botón y espera que el jugador lo presione para volver y confirmar.

` display_vidas() `: Muestra las vidas restantes y perdidas que tiene el jugador.

` batalla_perdida() `: Muestra el menú. ` return True ` si el jugador selecciona reintentar la batalla. ` return False ` si el jugador se rinde.

` perder() `: Muestra la pantalla "Game Over". Llama ` main() ` si el jugador elige jugar de nuevo. Llama ` cerrar_juego() ` si no.

### __Hilo del juego__

Una vez haya ocurrido la presentación y el jugador haya comenzado la partida, ` main() ` llama en orden las funciones de los enemigos.

### ` enemigo_terremoto() `

* Verifica que el jugador siga teniendo al menos una vida.

* Muestra la introducción.

* Espera la confirmación de ` jugador_listo() ` para llamar ` batalla1() `.

  ### ` batalla1() `

  * Carga las imágenes para la animación de fondo y añade el evento que controla los cambios.

  * Genera una lista de 6 teclas aleatorias de la lista de teclas posibles y otra con las constantes de pygame correspondientes.

  * Añade los eventos que controlan los temporizadores correspondientes a mantener y no mantener teclas.

  * Loop del juego:

    * Muestra en la pantalla la letra a mantener.

    * Evento ` cambiar_frame `: cambia la imagen del fondo para crear la animación.

    * Evento ` siguiente_tecla `: cambia la letra de la pantalla, y ralentiza el intervalo del evento ` cambiar_frame `.

    * Evento ` perder_por_tiempo `: da márgen de reacción al jugador para presionar la tecla de la pantalla. Si el temporizador del evento termina, ` return False `, el jugador perdió la batalla.

    * Cuando la tecla de la lista que está en la pantalla es presionada, empieza el temporizador del evento ` siguiente_tecla ` y para el del evento ` perder_por_tiempo `.

    * Si la tecla es soltada, empieza el temporizador del evento ` perder_por_tiempo ` y para el del evento ` siguiente_tecla `.

    * Al pasar por todas las teclas de la lista, el jugador gana la batalla. Para todos los temporizadores de eventos y ` return True `.

* Si la batalla fue ganada llama ` batalla1_ganada() ` (muestra imagen final de la batalla).

* Si la batalla fue perdida:

  * El jugador tiene vidas: llama ` batalla_perdida() `. Sale del bucle si el jugador se rinde.

  * El jugador no tiene vidas: llama ` perder() `.

### ` enemigo_lava() `

* Verifica que el jugador siga teniendo al menos una vida.

* Muestra la introducción.

* Espera la confirmación de ` jugador_listo() ` para llamar ` batalla2() `.

  ### ` batalla2() `

  * Carga las imágenes para la animación de fondo y añade el evento que controla los cambios.

  * Carga la lista de formas y añade el evento que controla la generación.

  * Añade el evento que controla la verificación de la ubicación del mouse.

  * Loop del juego:

    * Muestra en la pantalla la letra a mantener.

    * Evento ` cambiar_frame `: cambia la imagen del fondo para crear la animación.

    * Evento ` generar_solido `: llama ` generar() `.

      ` generar() `: toma la lista de formas y la lista de coordenadas de estas. Genera un par de coordenadas nuevas en una dirección aleatoria a distancia ` radio ` del par de coordenadas más reciente. Muestra las formas en las coordenadas. Actualiza y devuelve la lista de coordenadas con FIFO.

    * Evento ` chequear_mouse `: verifica que el mouse esté sobre las formas. Si no lo está, ` return False `, el jugador perdió la batalla.

    * Cuando las formas fueron generadas 20 veces, ` return True `, el jugador ganó la batalla.

* Si la batalla fue ganada llama ` batalla2_ganada() ` (muestra imagen final de la batalla).

* Si la batalla fue perdida:

  * El jugador tiene vidas: llama ` batalla_perdida() `. Sale del bucle si el jugador se rinde.

  * El jugador no tiene vidas: llama ` perder() `.

### ` enemigo_nube() `

* Verifica que el jugador siga teniendo al menos una vida.

* Muestra la introducción.

* Espera la confirmación de ` jugador_listo() ` para llamar ` batalla3() `.

  ### ` batalla3() `

  * Carga las imágenes para la animación de fondo.

  * Establece ` movimientos = 150 `.

  * Loop del juego:

    * Si ` movimientos == 0 `, ` return True `, el jugador ganó la batalla.

    * Si ` movimientos > 300 `, ` return False `, el jugador perdió la batalla.

    * Según el valor de ` movimientos ` actualiza el fondo.

    * Calcula la distancia del movimiento del mouse del jugador:

      * Si es mayor a 30: ` movimientos -= 1 `.

      * Si es igual o menor a 30: ` movimientos += 1 `.

* Si la batalla fue ganada llama ` batalla3_ganada() ` (muestra imagen final de la batalla).

* Si la batalla fue perdida:

  * El jugador tiene vidas: llama ` batalla_perdida() `. Sale del bucle si el jugador se rinde.

  * El jugador no tiene vidas: llama ` perder() `.

### ` ganar() `

* Verifica que el jugador tenga al menos una vida.

* Muestra la animación final.

* Llama ` main() ` si el jugador elige jugar de nuevo.

* Llama ` cerrar_juego() ` si el jugador elige salir.
