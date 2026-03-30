# Análisis de Archivos SAM 🧬

Este es un script de Python diseñado para procesar archivos SAM (Sequence Alignment/Map) utilizados en bioinformática. El programa lee el archivo línea por línea de manera eficiente, omitiendo las cabeceras, para extraer estadísticas clave sobre la calidad del mapeo.

## Características

* Lee archivos grandes sin saturar la memoria RAM.
* Cuenta el número total de lecturas alineadas.
* Calcula cuántas lecturas tienen una calidad de mapeo perfecta (`MAPQ = 60`).
* Muestra los resultados en la terminal usando una tabla elegante y fácil de leer.

## Requisitos

Este proyecto utiliza [uv](https://github.com/astral-sh/uv) como gestor de paquetes y dependencias. La interfaz gráfica de la terminal está construida con la librería `rich`.

## Instalación y Uso

1. Clona este repositorio en tu máquina local.
2. Navega hasta la carpeta del proyecto:
   ```bash
   cd proyecto-sam
   uv run python main.py <ruta_de_tu_archivo.sam>
    ```

## Ejemplo de Salida

El script devolverá una bella tabla coloreada en tu terminal con la siguiente información:

    Total de lecturas alineadas.

    Lecturas con MAPQ = 60.

    Porcentaje correspondiente.

## Ejecución con Nextflow

Para integrar este análisis en flujos de trabajo bioinformáticos más grandes y reproducibles, este proyecto incluye un pipeline configurado con Nextflow.

El uso de Nextflow automatiza la llamada a Python mediante uv y gestiona la salida de los datos.
Instrucciones de uso con Nextflow:

Asegúrate de estar en el directorio del proyecto y ejecuta el siguiente comando, indicando la ruta de tu archivo con el parámetro --sam:
    ```nextflow run main.nf --sam <ruta_de_tu_archivo.sam>
    ```

## Salida del Pipeline:
Al usar Nextflow, el programa no solo imprimirá la tabla de resultados en tu pantalla, sino que además creará automáticamente un registro de texto limpio (sin códigos de color) en la carpeta resultados/, guardado bajo el nombre output_nombredelarchivo.txt