# Web Crawler

## 1.- Introducción

Un ​ crawler ​es un programa que explora la Web de forma automática y recursiva, habitualmente con el propósito de alimentar el índice de un buscador web pero también para la creación de un mirror ​ (una réplica de un sitio web dado). Con una política de visitas adecuadas el uso de crawlers ​ permite que las colecciones de documentos de los buscadores web estén actualizadas. 
Los ​crawlers ​tienen un comportamiento muy diferente al de un usuario explorando un sitio web por lo que tienden a consumir más recursos del sitio que están “atacando”. En consecuencia, los distintos sitios web suelen hacer uso de un fichero ​ robots.txt que indica qué ​ crawlers ​ pueden visitar qué páginas y bajo qué condiciones.

## 2.- Descripción

El programa permite el escaneo de las webs almacenadas en el archivo "links.txt", así como el número máximo de archivos a descargar, tiempo en segundos que debe esperar entre dos peticiones GET y la opción de realizar el escaneo en anchura o profundidad.

Además el programa puede localizar el archivo ​ robots.txt para los sitios que explore y actuar según sus indicaciones.

## 3.- Argumentos

A el crawler se le pueden pasar una lista de argumentos a la hora de ejecutarlo, siendo todos opcionales. En caso de no poner alguno se preguntará por el menú.

* **--file**: Nombre del archivo con las url
* **--name**: Nombre del crawler. Por defecto es payacrawler
* **--sec**: Número de segundos a esperar entre peticiones GET
* **--mx**: Número máximo de descargas
* **-a**: Si se pone esta opción se realizará un recorrido en anchura
* **-p**: Si se pone esta opción se realizará un recorrido en profundidad

### Ejemplo de ejecución del programa:

```
 _    _ ___________   _____ ______  ___  _    _ _      ___________ 
| |  | |  ___| ___ \ /  __ \| ___ \/ _ \| |  | | |    |  ___| ___ \
| |  | | |__ | |_/ / | /  \/| |_/ / /_\ \ |  | | |    | |__ | |_/ /
| |/\| |  __|| ___ \ | |    |    /|  _  | |/\| | |    |  __||    / 
\  /\  / |___| |_/ / | \__/\| |\ \| | | \  /\  / |____| |___| |\ \ 
 \/  \/\____/\____/   \____/\_| \_\_| |_/\/  \/\_____/\____/\_| \_|
===================================================================
Hecho por Antonio Paya Gonzalez

-> Inserta el numero de segundos:1
-> Inserta el numero de descargas maximo:15
-> Tipo de exploracion de semillas: Anchura (a) / Profundidad (p):p
===================================================================
Iniciando Crawler:

(ok) Crawling https://lne.es ,Max downloads 14
(ok) Crawling http://kiosco.lne.es/ ,Max downloads 13
(!) Cannot scrap http://www.facebook.com/nuevaespana
	 # Crawling http://www.facebook.com/nuevaespana is prohibited unless you have express written
(ok) Crawling https://twitter.com/lanuevaespana ,Max downloads 12
(ok) Crawling https://twitter.com/lanuevaespana#timeline ,Max downloads 11
(ok) Crawling https://help.twitter.com/rules-and-policies/twitter-cookies ,Max downloads 10
(ok) Crawling https://help.twitter.com/en ,Max downloads 9
(ok) Crawling https://help.twitter.com/en/using-twitter ,Max downloads 8
(ok) Crawling https://help.twitter.com/en/managing-your-account ,Max downloads 7
(ok) Crawling https://help.twitter.com/en/safety-and-security ,Max downloads 6
(ok) Crawling https://help.twitter.com/en/rules-and-policies ,Max downloads 5
(ok) Crawling https://help.twitter.com/en/twitter-guide ,Max downloads 4
(ok) Crawling https://help.twitter.com/en/new-user-faq ,Max downloads 3
(ok) Crawling https://help.twitter.com/en/glossary ,Max downloads 2
(ok) Crawling https://help.twitter.com/en/contact-us ,Max downloads 1
(ok) Crawling https://help.twitter.com/en/search ,Max downloads 0

```