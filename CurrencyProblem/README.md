== Currency Problem ==
Calcula las recudación total de un un grupo de campañas, teniendo en cuenta las diferentes monedas

--
USO:
--
El principal de esta aplicación es: currency.py

Entradas necesarias:
* Archivo json de campañas: "campaigns_data.json"

Salidas esperadas:
* Archivo json de campañas agrupadas por nombre y considerando un único beneficio.

Se ejecuta a través de la consola utilizando el siguiente comando:

python currency.py

--
DETALLES DEL DISEÑO
--
Desde el archivo currency se realizan las llamadas a las difentes clases que conforman
la solución al problema planteado.

Inicialmente se hace instancia de las clases encargadas de realizar la query de conversión y analizar
su resultado. Para eso se utilizando dos clases: URLOperations (Clase encargada de realizar la consulta
y devolver el factor de conversión en tipo flotante) y NewHtmlParser (Clase encargada de parsear la respuesta
y ubicar le factor de conversión en el tag currency_converter_result).
URLOperations, arroja mensaje un de error "There was an error in url query" cuando no es posible conectarse a
la url especificada, en este caso el archivo json de salida mostrará, para todas las campañas, los beneficios en 0.

Luego se realiza el parseo de los archivos, cuya extensión es .json. Esto le da cierta escalabilidad a la
aplicación para poder cambiar el formato del archivo de entrada de manera sencilla.

Luego del parseo se realiza la llamada a la clase principal de esta aplicación CampaignsProfit.
Dentro de esta clase, lo primero a realizar es contar la cantidad de campañas y cuantas veces se encuentra cada
campaña dentro del archivo de entrada. Con esta información se realiza, por cada grupo de campañas, la conversión de
la moneda original a dolar y el posterior cálculo de la recaudación total por campaña.

Finalmente se realiza la escritura de cada campaña con su recaudación total, en un archivo tipo .json.

--
 #TODO:
--
 * Agregar UT para asegurar que el método que agrupa las campañas y el que realiza
 la consulta funcionen correctamente.
 * Agregar manejo de exepciones y errores.
 * Que la aplicación, sea instalable y ejecutable utilizando setuptools
 * README en inglés