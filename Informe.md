

#Proyecto Alfa

#Grupo DCCCAC6



#RESUMEN INFORME


Nuestra aplicación realiza operaciones de scraping sobre la página del servicio meteorológico nacional. Dicha web, construida sobre tecnología PHP y con gran parte de la info enviada a través de APIs, presentó impedimentos para trabajar enteramente sobre los módulos de Rquests y BeautifulSoup, idea principal del proyecto, puesto que era imposible acceder a las APIs para hacer las consultas y scrapear y las respuestas a posterior. En su lugar empleamos la tecnología Selenium y ChromeDriver para inicializar un navegador web que pudiera interactuar con el JS de la página y llegar a pasar como parámetros de solicitud las ciudades foco (las 23 capitales provinciales) y luego devolver un html más completo con la información que necesitábamos de cada zona como variable parseada y lista para ser utilizada por Soups. Conseguido este objetivo, y solucionados algunos inconvenientes relacionados al tipo de información ofrecida por la página (que no presenta datos numéricos del clima para todoas las fechas y a toda hora, sino que a veces carece de datos y en su lugar ofrece el caracter " -° " lo que complica el correcto funcionamiento del parseo) almacenamos la información obtenida en cada instancia de scraping en un objeto que compara Máximos, Mínimos y media Semanal y luego transformamos ese objeto en un Panda DataFrame almacenado en carpetas específicas dependiendo de la necesidad.
 
Una vez recibidos los datos del Web Scraping, se procedió a crear la base de datos mediantes consultas en MySQL con formato scv.
Durante la elaboración del informe tuvimos varios desafíos, el principal, ordenar los datos de la base. En la misma había mucha 
redundancia y por defecto nos arrojaba la fecha como fila y columna a la vez, por lo que se tuvieron que reorganizar los datos en un excel, dicho archivo lo dejamos a continuación.
 
[https://docs.google.com/spreadsheets/d/1rmFz1AhgJOQqiKkqX4Ii1KT0Wv2-g5aWrVdeyS_mUTI/edit#gid=0]

El siguiente gran desafío fue la presentación del informe, ya que para poder presentar el mismo de manera virtual se necesita una licencia para lector, por lo que dejamos imagenes del mismo a continuación: 


[Presentacion + Integrantes]   https://drive.google.com/file/d/1O2mhw9_W7Ygx2kHbtKzFT8T8AicD2mvi/view?usp=share_link

[Introduccion]   https://drive.google.com/file/d/1-zplWh9HyrSqHBLx8ICOuUovxDynVaaX/view?usp=sharing

[Primer Analisis]  https://drive.google.com/file/d/1T2Ti-gK5dH1Vpbon5rTNZS0dO75gUVI4/view?usp=sharing

[Segundo Analisis]  https://drive.google.com/file/d/1r-GmxkBZEiLJ9v5Lo5Gq1HUnCZENbtCX/view?usp=sharing


En el siguiente enlace se encuentra guardado el informe original creado con la aplicacion Power BI, donde se puede visualizar solo con la debida licencia: 
https://app.powerbi.com/links/mvS7cxHMbV?ctid=e715177a-8963-49dc-a267-25aa1ff36521&pbi_source=linkShare

Tambien adjuntamos un archivo de tipo ZIP, donde se encuentra el documento original para su descarga. 
[Proyecto Alfa.BI.zip](https://github.com/ispc-programador2022/DCCCAC6/files/10041669/Proyecto.Alfa.BI.zip)

Para la realización del informe se realizó una amplia investigación, desde las tecnologías para su análisis y visualización hasta el tipo de análisis que se realiza en este tipo de datos. Para realizar un informe exhaustivo y completo en los datos meteorológicos se necesitan muchas variables, tales como temperatura, presión atmosférica, humedad, precipitaciones, etc. 
Por lo que para el tipo de datos recogidos por la API, optamos por medir la desviación estándar de los picos de temperatura y medianas.
Con la primera podemos medir la volatilidad de la temperatura máxima y mínima de un determinado periodo de días y aplicable a todas las ciudades capitales. Esto nos permite identificar que tan cambiante es la temperatura en el país.
Con la media de la temperatura podemos analizar la temperatura media del periodo de días, lo cual luego realizando una comparativa más amplia, nos permite realizar comparaciones con otros periodos o países y de esa forma poder darle una clasificación al clima.
 Las tecnologías que principalmente se destacan para la realización del informe son Excel, Power Query y Power BI. Las cuales nos permitieron mediante sus fórmulas y herramientas (Excel) organizar y calcular la temperatura mínimas y máximas del periodo de días analizado, junto con sus respectivas temperaturas medias y el promedio entre ambas.
La segunda tecnología es Power BI, la cual nos permitio mediante su editor de datos (Power Query), clasificar las distintas columnas y seguir quitando redundancias, para luego finalmente con Power BI graficar los datos y poder realizar el análisis de la dispersión de los datos mediante la desviación estándar y la media de las temperaturas.


Para finalizar se compartió el archivo en un documento de GitHub para su presentación y visualización mediante acceso público.
 












