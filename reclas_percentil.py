## SCRIPT PARA RECLASIFICAR AUTOMATICAMENTE LOS CORREDORES SEGUN EL PERCENTIL 1
## Corre bien pero la lista de corredores tiene que estar limpia sin calculos intermedios
import arcpy
import numpy as np
import os
from arcpy import env
env.overwriteOutput = True
env.workspace = 'D:/Dropbox (SIGA)/Carpeta del equipo SIGA/shapes/NodoNorte1/jujuy/corredores/21corredores'
carpeta = env.workspace
lista = arcpy.ListRasters()
listaPoligonos = []
for i in lista:
    array = arcpy.RasterToNumPyArray(i)
    array[array<=0]= np.nan
    percent = np.nanpercentile(array, 1)
    percentil = int(percent)
    nombre = i[:-9]
    nombreOutput = "{0}_reclas.tif".format(nombre)
    donde = "VALUE <= {0}".format(percentil)
    print donde
    reclas = arcpy.sa.Con(i, 1, 0,donde)
    reclas.save(os.path.join(carpeta,nombreOutput))
    nombrePol = "{0}_pol.shp".format(nombre)
    nombreLayer = "{0}_layer".format(nombre)
    corredores = os.path.join(carpeta,nombrePol)
    poligonos = arcpy.RasterToPolygon_conversion(reclas,corredores, "NO_SIMPLIFY")
    layers = arcpy.MakeFeatureLayer_management(poligonos, nombreLayer, "gridcode = 1")
    arcpy.AddField_management(layers, 'corredor', "TEXT")
    arcpy.AddField_management(layers, 'percentil', "LONG")
    expresion = '"{0}"'.format(nombre)
    arcpy.CalculateField_management(layers,'corredor',expresion, "PYTHON")
    arcpy.CalculateField_management(layers,'percentil',percentil, "PYTHON")
    listaPoligonos.append(nombreLayer)
    
print listaPoligonos    
merge = arcpy.Merge_management(listaPoligonos, os.path.join(carpeta,'corredores.shp'))
    
    

