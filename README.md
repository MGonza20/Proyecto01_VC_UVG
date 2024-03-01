# Proyecto de Computer Vision: Reconocimiento de Estructuras Arteriales en Imágenes Médicas

Este proyecto se centra en el procesamiento de imágenes médicas para reconocer y simplificar estructuras arteriales en imágenes de rayos X de angiogramas coronarios. Se implementaron algoritmos de binarización de imágenes y se desarrolló un método para discretizar la estructura arterial y representarla como un grafo.

## Contenido del Proyecto:

### 1. Binarización de Imágenes

- Se implementaron dos algoritmos de binarización: uno basado en un filtro de mediana y otro en Niblack adaptativo.
- Se evaluaron métricas de desempeño como Accuracy, Sensitivity, Specificity, Precision y F1 Score para comparar los resultados con imágenes groundtruth.

### 2. Discretización de la Estructura Arterial

- A partir de imágenes groundtruth, se desarrolló un algoritmo para generar una discretización de la estructura arterial.
- Se representó la discretización como un grafo de vértices y aristas, donde cada vértice se clasifica como extremo, bifurcación o trifurcación mediante un código de colores.

## Archivos del Proyecto:

- **Código Fuente:**
    - `Problema01.ipynb`: Contiene la implementación de los algoritmos de binarización de imágenes.
    - `Problema02.ipynb`: Contiene el código para la discretización de la estructura arterial y la generación del grafo.

- **Datos:**
    - Carpeta `images`: Contiene las imágenes originales y las imágenes binarias groundtruth utilizadas en el proyecto.

- **Resultados:**
    - Carpeta `results_p02`: Contiene los resultados obtenidos, como métricas de desempeño y visualizaciones de los grafos generados por el ejercicio 2.

## Instrucciones de Uso:

1. **Binarización de Imágenes:**
    - Ejecutar el script `Problema01.ipynb` con las imágenes de entrada para obtener las imágenes binarizadas.
    - Analizar las métricas de desempeño en los resultados obtenidos.

2. **Discretización de la Estructura Arterial:**
    - Ejecutar el script `Problema02.ipynb` con las imágenes groundtruth.
    - Revisar el archivo estructurado generado que describe el grafo obtenido y las visualizaciones de los grafos.

## Ejemplo de Resultados:

- Se adjunta una imagen de ejemplo de la binarización de una imagen de rayos X y su correspondiente imagen binaria resultante.

[![Problema 1 - Image 10](https://i.postimg.cc/YSCd09sg/test-prob1.png)](https://postimg.cc/yD2mrVBY)
- También se incluye una visualización del grafo generado a partir de la discretización de la estructura arterial.

[![Problema 2 - Image 1](https://i.postimg.cc/285yHNMG/1-gt.png)](https://postimg.cc/9zvcMKWw)

## Autores:

- Oscar Estrada     20565
- Sara Paguaga      20634 
- Guillermo Santos  191517
- Juan Carlos Bajan 20109
 
