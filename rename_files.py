import os    # Importa el módulo para manejar archivos y carpetas

# Cambia esta ruta a la carpeta donde están tus archivos
CARPETA = r'C:\Users\USUARIO\Downloads\rename_files'  # En Windows usa r'...' o doble barra \\. En Linux/Mac usa la ruta normal.

# Define el nombre base que tendrán los archivos al ser renombrados
nombre_base = 'final_'   # Cambia esto como prefieras
extension_destino = '.txt' # Cambia esto a la extensión de tus archivos (.png, .txt, .pdf...)

# Lista solo los archivos con una determinada extensión
archivos = [f for f in os.listdir(CARPETA) if f.endswith(extension_destino)]

# Ordenar los archivos para que queden numerados en orden (alfabético por defecto)
archivos.sort()

# Recorrer cada archivo y renombrarlo
for i, nombre_original in enumerate(archivos, start=1):
    nuevo_nombre = f"{nombre_base}{i:03d}{extension_destino}"  # archivo_001.jpg, archivo_002.jpg, etc.
    ruta_original = os.path.join(CARPETA, nombre_original)
    ruta_nueva = os.path.join(CARPETA, nuevo_nombre)
    os.rename(ruta_original, ruta_nueva)
    print(f'Renombrado: {nombre_original} -> {nuevo_nombre}')


import os

# Cambia esto a la ruta de tu carpeta
CARPETA = r'C:\Users\USUARIO\Downloads\rename_files'  # En Windows usa r'...' o doble barra \\. En Linux/Mac usa la ruta normal.

# --- Borra todos los archivos que terminan en .cfg, incluyendo los del ejemplo de la imagen ---
for nombre_archivo in os.listdir(CARPETA):
    if nombre_archivo.endswith('.cfg'):
        ruta_completa = os.path.join(CARPETA, nombre_archivo)
        try:
            os.remove(ruta_completa)
            print(f'Borrado: {nombre_archivo}')
        except Exception as e:
            print(f'No se pudo borrar {nombre_archivo}: {e}')

