# Motor_de_Busqueda

- [Motor_de_Busqueda](#motordebusqueda)
    - [1.- Introducción](#1--introducci%C3%B3n)
    - [2.- Similitud booleana de documentos](#2--similitud-booleana-de-documentos)
        - [2.1.- Coeficiente de Dice](#21--coeficiente-de-dice)
        - [2.2.- Coeficiente de Jaccard](#22--coeficiente-de-jaccard)
        - [2.3.- Coeficiente del Coseno](#23--coeficiente-del-coseno)
        - [2.4.- Coeficiente de Dice](#24--coeficiente-de-dice)
    - [3.- Ejecución:](#3--ejecuci%C3%B3n)

## 1.- Introducción

Este motor de búsqueda realiza una comparación entre un archivo de documentos
y otro archivo con las consultas, mostrando el resultado que corresponde a cada uno de los diferentes coeficientes (Dice, Jaccard, Coseno y Solapamiento).


## 2.- Similitud booleana de documentos
Para mejorar la búsqueda, se realizan las siguientes acciones antes de aplicar los coeficientes:

1. Paso a minúsculas.
2. Eliminar símbolos de puntuación.
3. Eliminar palabras vacías.
4. Lematización.
5. Se almacena cada token con el número de apariciones del mismo.

### 2.1.- Coeficiente de Dice
Siendo X e Y dos conjuntos (documentos,consultas, textos...) : $2\frac{|X\cap Y|}{|X|+|Y|}$

### 2.2.- Coeficiente de Jaccard
Siendo X e Y dos conjuntos (documentos,consultas, textos...) : $\frac{|X\cap Y|}{|X\cup Y|}$

### 2.3.- Coeficiente del Coseno
Siendo X e Y dos conjuntos (documentos,consultas, textos...) : $\frac{|X\cap Y|}{|X|\cdot|Y|}$

### 2.4.- Coeficiente de Dice
Siendo X e Y dos conjuntos (documentos,consultas, textos...) : $\frac{|X\cap Y|}{min(|X|,|Y|)}$

## 3.- Ejecución:

Para ejecutar el motor de búsqueda debes usar el siguiente formato:

```python
python motor_busqueda_v1 cran-1400.txt cran-queries.txt
```

Siendo:

* cran-1400.txt : Un fichero con los documentos con el formato de un documento por línea.
* cran-queries.txt : Un fichero con las consultas con el formato de una consulta por línea.