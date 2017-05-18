== Sheep Problem ==
A partir de un número (N) se comienza una secuencia del tipo 1*N, 2*n, .. , n*N (donde n es cualquier
número natural) hasta que, como resultado, se consiguen todos los números naturales desde el 0 al 9.

--
USO:
--
El principal de esta aplicación es: sheep.py

Entradas necesarias:
* Archivo de texto: "c-input.in"


Se ejecuta a través de la consola utilizando el siguiente comando:

python3 sheep.py

--
DETALLES DEL DISEÑO
--
Desde el archivo sheep se realiza la llamada a la clase Sheep que conforma la solución al problema planteado.

Inicialmente se realiza el parseo del archivo, cuya extensión es .in. Esto le da cierta escalabilidad a la
aplicación para poder cambiar el formato del archivo de entrada de manera sencilla. Como resultado de esto
se obtienen los valores de entrada (N) y el número máximo de operaciones (n) permitidas.

Luego se genera una lista, db, contra la cual se compara para determinar si se han encontrado todos los números
necesarios para que la secuencia (1*N, 2*N, .. ,n*N) concluya de manera exitosa.

Finalmente se realiza la instancia de la clase Sheep en la cual, para cada valor del archivo de entrada
se realiza la secuencia de productos, con un lìmite. Si antes de alcanzar dicho límite se encuentran todos los valores
esperados, la aplicación devuelve un string del tipo "Case #x : y", donde "x" representa el número de test (n) en cual
se alcanzo la lista esperada e "y" representa el último valor que se registro.
Si luego de que se cumple el máximo de productos permitidos, no se logra el objetivo, la aplicación muestra
el siguiente mensaje por pantalla: INSOMNIA

--
 #TODO:
--
 * Agregar UT, sobre en particular al método fall_asleep.
 * Que la aplicación, sea instalable y ejecutable utilizando setuptools
 * README en inglés
