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
      bash
      cd proyecto-sam
3. Ejecuta el programa pasándole la ruta de tu archivo .sam:
uv run python main.py <ruta_de_tu_archivo.sam>

## Ejemplo de Salida

El script devolverá una bella tabla coloreada con:

    -Total de lecturas alineadas.

    -Lecturas con MAPQ = 60.

    -Porcentaje correspondiente.
