== Campaign Selector ==
Selecciona la mejor campaña para un determinado usuario

--
USO:
--
El principal de esta aplicación es: campaing_classificator.py

Entradas necesarios:
* Archivo json de usuario: "user.json"
* Arcvhivo json de campañas: "campagins.json"

Se ejecuta a través de la consola utilizando el siguiente comando:

python campaigns_classificator.py

--
DETALLES DEL DISEÑO
--
Desde el archivo campaigns_classificator se realizan las llamadas a las difentes clases que conforman
la solución al problema planteado.

Inicialmente se realiza el parseo de los archivos, cuya extensión es .json. El hecho de que el parseo
de dichos archivos se realice mediante una clase (InputParser) es por que de esa manera, un cambio en la
extension de los archivos de entrada no afectaría al diseño del la solución propuesta

Luego del parseo se realiza la llamada a la clase principal de esta aplicación CampaignSelector.

El primer criterio para comenzar el filtrado es la plataforma, asumiendo que las aplicaciones solo
se desarrollan para un plataforma en particular se reduce el número de campañas disponibles.

Luego se realiza el filtrado por las claves connection y gender. Estas dos claves tienen la particularidad que
además de tener sus valores determinados (Male, Female, Wifi, Mobile Data) puede tomar el valor All, el
cual es considerado a la hora de realizar el filtrado. Con respecto a este valor, el método campaigns_filter de
la clase CampaignSelector, posee la posibilidad de no incluir los valores All en la busqueda. Esto con el
objetivo de permitir que busquedas mas específicas.

Finalmente, se tiene en cuenta la edad del usuario y los valores min y max de cada campaña para seleccionar
la mas adecuada. Para tomar el mismo criterio en todas las selecciones se considero que los valores null tomarían
los valores 0 y 110 según pertenecezcan a la clave min_age o max_age respectivamente. Con esta consideracion y
a través de la formúla  |(max_age - min_age)/2 + min_age| - user_age se obtiene en que posición respecto del mínimo
 y el máximo se ubica la edad del usuario.

--
 #TODO:
--
 * Agregar UT para asegurar que los métodos de filtrado funcionan correctamente. Especialmente
  el método filter_age.
 * Agregar manejo de exepciones y errores (ej: en el parseo de los archivos json)
 * Depende del entorno de uso se podría realizar el parseo de argumentos de entrada por consola
 * Que la aplicación, sea instalable y ejecutable utilizando setuptools
 * README en inglés