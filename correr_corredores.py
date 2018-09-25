import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = 'H:/NODO/corredoresJujuy/acumulados'
carpeta = env.workspace
listaRaster = arcpy.ListRasters()
listaDim = []
for i in listaRaster:
    listaDim.append(i)
for i in listaRaster:
    raster1 = '{0}/{1}'.format(carpeta,i)
    nombre1 = i[:-9]
    listaDim.remove(i)
    for j in listaDim:
        raster2 = '{0}/{1}'.format(carpeta,j)
        nombre2 = j[:-9]
        corredores = '{0}/{1}_{2}.tif'.format(carpeta,nombre1,nombre2)
        outCorr = Corridor(raster_1, raster_2)
	outCorr.save(corredores)
        
    



    
    

