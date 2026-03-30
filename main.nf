#!/usr/bin/env nextflow

nextflow.enable.dsl=2

/*
 * Parámetros
 */
params.sam = "WT.sam"

/*
 * Proceso
 */
process analyze_sam {

    // Mostramos la salida en la terminal
    debug true
    
    // Guardamos el archivo final en la carpeta 'resultados'
    publishDir "${projectDir}/resultados", mode: 'copy'

    input:
    path sam_file

    // Definimos el nuevo nombre del archivo de salida
    output:
    path "output_${sam_file.baseName}.txt"

    script:
    """
    # 1. Ejecutamos Python y guardamos la tabla en el archivo output_NOMBREDELARCHIVO.txt
    uv run python ${projectDir}/main.py ${sam_file} | tee output_${sam_file.baseName}.txt
    
    # 2. Imprimimos una línea en blanco para que quede bonito
    echo ""
    
    # 3. Imprimimos el mensaje final de confirmación
    echo "Resultados guardados también en resultados/output_${sam_file.baseName}.txt"
    """
}

/*
 * Flujo de trabajo principal
 */
workflow {
    
    canal_sam = Channel.fromPath(params.sam)
    analyze_sam(canal_sam)

}