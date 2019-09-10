#!/usr/bin/python

#Las carpetas fotos,fotos2 y fotos3 deben haber sido creadas previamente
#Programado por: Jose Luis Araya Lopez

import sys,os,shutil 

__version__ = 1.2


def gifanimn(numero_imagenes,numero_imagenes2,extension):
    extension=str(extension)
    n=sys.platform

    if n == 'linux2':     
       info=os.getcwd()
       os.chdir('fotos2') 
       top=os.getcwd()
         
    else:
       os.chdir('fotos2')
       top=os.getcwd()
    

    #Primero Eliminamos los archivos de la carpeta fotos2 para que siempre haya solo un numero
    #predefinido:
    
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
     
    os.chdir('../fotos3') 
     
    #Segundo Eliminamos los archivos de la carpeta fotos3 para que siempre haya solo un numero
    #predefinido:
    
    for root, dirs, files in os.walk('../fotos3', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))  
    

    # En carpeta fotos se procede a tomar el numero de imagenes indicados por "numero_imagenes"
    os.chdir('../fotos')
    lista=os.listdir('.')
    lista=sorted(filter(os.path.isfile, os.listdir('.')),key=lambda p: os.stat(p).st_mtime)
    #lista.sort()
    lenlista=len(lista)
    lista2=lista[lenlista-numero_imagenes::] 
    lista3=lista[lenlista-numero_imagenes2::] 

    #Copiando archivos a carpeta fotos2 y fotos3:
    print "Copiando en fotos2..."
    for file in lista2:
        if os.path.splitext(file)[1] == extension :
           print file
           shutil.copy(file, os.path.join("../fotos2", file))
    print "Copiando en fotos3..."       
    for file in lista3:
        if os.path.splitext(file)[1] == extension :
           print file
           shutil.copy(file, os.path.join("../fotos3", file))

    #print "***Compilacion exitosa gifanim.pyc***"
    
    return
 
