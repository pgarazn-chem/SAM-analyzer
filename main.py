import sys
import os
# Importamos las herramientas de rich para formatear la terminal
from rich.console import Console
from rich.table import Table

def procesar_sam(filename):
    """
    Lee un archivo SAM, cuenta los alineamientos totales y los que tienen MAPQ = 60,
    y muestra los resultados usando una tabla de 'rich'.
    """
    total_alineadas = 0
    mapq_60 = 0
    
    # Inicializamos la consola de rich
    console = Console()

    if os.path.exists(filename):
        console.print(f"[bold blue]Procesando el fichero SAM:[/bold blue] {filename}\n")

        with open(filename, mode="r", encoding="utf8") as f:
            for linea in f:
                if linea.startswith('@'):
                    continue
                
                total_alineadas += 1
                
                wlinea = linea.strip()
                partes = wlinea.split('\t')
                
                if len(partes) >= 5:
                    valor_mapq = partes[4] 
                    
                    if valor_mapq == '60':
                        mapq_60 += 1
        
        if total_alineadas > 0:
            porcentaje = (mapq_60 / total_alineadas) * 100
        else:
            porcentaje = 0.0

        # --- AQUÍ EMPIEZA LA MAGIA DE RICH ---
        
        # Creamos una tabla con un título y estilos
        tabla = Table(title="Resultados del Análisis SAM", show_header=True, header_style="bold magenta")
        
        # Añadimos las columnas
        tabla.add_column("Métrica", style="cyan", no_wrap=True)
        tabla.add_column("Valor", justify="right", style="green")

        # Añadimos las filas con nuestros datos (convertimos los números a texto con str())
        tabla.add_row("Total de lecturas alineadas", str(total_alineadas))
        tabla.add_row("Lecturas con MAPQ = 60", str(mapq_60))
        tabla.add_row("Porcentaje correspondiente", f"{porcentaje:.2f}%")

        # Imprimimos la tabla en la consola
        console.print(tabla)

    else:
        # Usamos rich para mostrar un mensaje de error en rojo
        console = Console()
        console.print("[bold red]Error:[/bold red] La ruta indicada no existe.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        console = Console()
        console.print("[bold yellow]Uso incorrecto.[/bold yellow] Debes ejecutarlo así: [bold white]uv run python main.py <ruta_del_archivo.sam>[/bold white]")
    else:
        ruta_archivo = sys.argv[1]
        procesar_sam(ruta_archivo)