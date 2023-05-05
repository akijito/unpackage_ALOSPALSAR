import os
import zipfile
import shutil

path = "C:/Users/jccol/Desktop/Oviedo SAS/Guania/DEM/ALOS_PALSAR"
pathfiles = os.listdir("../Guania/DEM/ALOS_PALSAR")

folder = []
for file in range(0, len(pathfiles), 1):
    folder.append(path+r"/"+pathfiles[file])
    
folder_dem = "C:/Users/jccol/Desktop/Oviedo SAS/Guania/DEM/img_DEM"
try:
    os.mkdir(folder_dem)
    print(f"Se creó la carpeta '{folder_dem}' correctamente.")
except FileExistsError:
    print(f"La carpeta '{folder_dem}' ya existe.")
except Exception as e:
    print(f"Ocurrió un error al crear la carpeta: {e}")
    
for archivo in folder:
    if zipfile.is_zipfile(archivo):
        with zipfile.ZipFile(archivo, 'r') as zip_ref:
            zip_ref.extractall(folder_dem)

folders_dem = os.listdir(folder_dem)
carpetas_me = []
for i in folders_dem:
    carpetas_me.append(folder_dem+'/'+i)
    
carpeta_destino = "C:/Users/jccol/Desktop/Oviedo SAS/Guania/DEM/Dem_analisis"
try:
    os.mkdir(carpeta_destino)
    print(f"Se creó la carpeta '{carpeta_destino}' correctamente.")
except FileExistsError:
    print(f"La carpeta '{carpeta_destino}' ya existe.")
except Exception as e:
    print(f"Ocurrió un error al crear la carpeta: {e}")
    
for j in range(0, len(carpetas_me),1):
    archivos = os.listdir(carpetas_me[j])
    for files in range(0, len(archivos), 1):
        if archivos[files].endswith('.dem.tif'):
            imagen_dem = os.path.join(carpetas_me[j], archivos[files])
            try:
                shutil.copy(imagen_dem, carpeta_destino)
            except Exception as e:
                print(f"Ocurrió un error al copiar el archivo: {e}")
