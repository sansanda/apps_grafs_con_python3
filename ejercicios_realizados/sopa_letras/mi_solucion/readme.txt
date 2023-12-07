Descripción: en este ejercicio intentaremos crear una aplicación que nos
proponga la resolución de sopas de letras. En nuestro caso tendremos que encontrar
cinco palabras relacionadas con productos del campo (frutas, verduras, legumbres...)
en un tablero de letras de 15x15.
Las palabras que podemos elegir para que aparezcan en la sopa de letras están
en las líneas del fichero de texto productos_campo.txt. Tambien podemos elegir una alternativa
para la carga de dichas palabras.

En la pantalla se nos indica el número de palabras que nos quedan para
resolver la sopa de letras, siendo inicialmente 5.
Cuando pulsamos en el botón “Nueva sopa de letras” elegimos al azar 5
palabras del fichero productos_campo.txt y las representamos en el tablero. Esa
representación puede estar orientada de 8 formas distintas (2 horizontal , 2 vertical
y 4 oblicuamente) y en nuestra aplicación no se solapará ninguna letra de ninguna
palabra, es decir, no habrá ninguna letra compartida por dos palabras.
Al hacer clic sobre cualquier celda del tablero esta adquirirá un color de
fondo azul claro. Cuando hacemos clic en “Marcar palabra” indicamos que vamos
a ir marcando consecutivamente las letras de una palabra que hemos identificado
265
. Tras hacerlo pulsaremos en el botón “Comprobar” y si es correcta
266 nos lo indicará
por pantalla, decrementenado en una unidad el número de palabras restantes. Si este
valor llega a cero, hemos completado la sopa de letras y nos lo indicará por pantalla.
