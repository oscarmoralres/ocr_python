# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:45:11 2016

@author: Oscar
"""
#Biblioteca de imagenes en Python
from PIL import Image
#Biblioteca para generar matriz de la imagen
import matplotlib.image as mpimg
#Biblioteca para recorrer archivos en un árbol de directorios
import os
#Biblioteca para escribir datos en un archivo csv
import csv

#Nombre: matrizimagen
#Desc: Metodo para obtener la matriz de la imagen
#Argumentos: nombre de la imagen
#Regresa: matriz y tamaño de las filas y columnas
def matrizimagen(nombre):
    #Carga la imagen en la variable img
    img = Image.open(nombre)
    #Carga la imagen en forma de matriz
    img2 = mpimg.imread(nombre)
    #Se optiene el tamaño de la imagen
    columnas, filas = img.size
    #regresa matriz de la imagen y filas y columnas
    return img2, filas, columnas

#Nombre: razon_filascolumnas
#Desc: Metodo para calcular la razon entre filas y columnas
#Argumentos: filas y columnas
#Regresa: razon filas/columnas
def razon_filascolumnas(filas, columnas):
    #Variable para guardar la razon de filas y columnas
    razonfilascolumnas = 0
    #Caracteristica 1.. Calcula la razón de Filas/Columnas
    razonfilascolumnas = filas/columnas
    #Regresa razon  de las filas entre las columnas
    return razonfilascolumnas

#Nombre: unoscerosimagen
#Desc: Metodo para calcula cuantos 1s y 0s hay respecto al área del imagen
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos y razon de ceros respecto al area
def unosimagen(img2, filas, columnas):
    #Contadores de unos
    contadoruno = 0
    #Contadores de razon de unos y ceros respecto al área
    razonunos = 0
    #Ciclo para recorer las filas de la matriz
    for x in range(filas):
        #Ciclo para recorer las columnas de la matriz
        for y in range(columnas):
            #Condición para verificar el pixel igual a 0
            if(img2[x][y] == 1):
                contadoruno = contadoruno + 1
    #Guarda la razón entre el numero de 1s respecto al área de la imagen
    razonunos = contadoruno/(filas*columnas)
#            print(razon1)
    #Regresa la razon de unos y ceros
    return razonunos
    
    #################################

#Nombre: vectorcuartovertical
#Desc: Metodo para calcula cuantos unos hay en el vector 1/4 vertical respecto asu tamaño 
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectorcuartovertical(img2, filas, columnas):
    #Contador para el numero de unos en el vector
    contadorunos = 0
    #Variable par el tamaño del vector
    sizevector = 0
    #Variable para guardar la razon del numero de unos / tamaño del vector
    razonunoscuartovertical = 0
    #Calcula la línea a 1/4 vertical de la imagen
    cuartovectorvertical = int(columnas/4)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][cuartovectorvertical] == 1):
            #Aumenta el contador de los 1s
            contadorunos += 1
    #Obtiene el tamaño del vector
    sizevector = filas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunoscuartovertical = contadorunos/sizevector
#    print(razonunoscuartovertical)
    #Regresa el numero de cortes en a 1/4 vertical
    return razonunoscuartovertical

#Nombre: vectorcuartohorizontal
#Desc: Metodo para calcular el numero de unos en el vector 1/4 horizontal respecto asu tamaño
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectorcuartohorizontal(img2, filas, columnas):
    #Contador del numero de unos en el vector
    contadorunos = 0
    #Varible para guadar el tamaño del vector
    sizevector = 0
    #Variable para guadar la razon del numero de unos / tamaño del vector
    razonunoscuartohorizontal = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    cuartovectorhorizontal = int(filas/4)
    #Recorre la línea horizontal de la imagen
    #Ciclo para recorre la linea horizontal calculada
    for x in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[cuartovectorhorizontal][x]==1):
            #Aumenta el contador de los 1s
            contadorunos += 1
#            print(corteshc)
    sizevector = columnas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunoscuartohorizontal = contadorunos/sizevector
    #Regresa el numero de cortes en a 1/4 horizontal
    return razonunoscuartohorizontal

#Nombre: vectormitadvertical
#Desc: Metodo para calcula la razon de numero de unos que hay en el vector 1/2 / el vector
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectormitadvertical(img2, filas, columnas):
    #Contador para el numero de unos en el vector
    contadorunos = 0
    #Variable par el tamaño del vector
    sizevector = 0
    #Variable para guardar la razon del numero de unos / tamaño del vector
    razonunosmitadvertical = 0
    #Calcula la línea a 1/2 vertical de la imagen
    mitadvectorvertical = int(columnas/2)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][mitadvectorvertical] == 1):
            #Aumenta el contador de los 1s
            contadorunos += 1
    #Obtiene el tamaño del vector
    sizevector = filas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunosmitadvertical = contadorunos/sizevector
#    print(razonunoscuartovertical)
    #Regresa el numero de cortes en a 1/2 vertical
    return razonunosmitadvertical
    
#Nombre: vectormitadhorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a la mitad horizontal
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectormitadhorizontal(img2, filas, columnas):
    #Contador del numero de unos en el vector
    contadorunos = 0
    #Varible para guadar el tamaño del vector
    sizevector = 0
    #Variable para guadar la razon del numero de unos / tamaño del vector
    razonunosmitadhorizontal = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    mitadvectorhorizontal = int(filas/2)
    #Recorre la línea horizontal de la imagen
    #Ciclo para recorre la linea horizontal calculada
    for x in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[mitadvectorhorizontal][x]==1):
            #Aumenta el contador de los 1s
            contadorunos += 1
#            print(corteshc)
    sizevector = columnas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunosmitadhorizontal = contadorunos/sizevector
    #Regresa el numero de cortes en a 1/2 horizontal
    return razonunosmitadhorizontal

#Nombre: vectortrescuartosvertical
#Desc: Metodo para calcula el numero de unos en el vector 3/4 / el tamaño del vector
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectortrescuartosvertical(img2, filas, columnas):
    #Contador para el numero de unos en el vector
    contadorunos = 0
    #Variable par el tamaño del vector
    sizevector = 0
    #Variable para guardar la razon del numero de unos / tamaño del vector
    razonunostrescuartosvertical = 0
    #Calcula la línea a 1/2 vertical de la imagen
    trescuartosvectorvertical = int(columnas/2)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][trescuartosvectorvertical] == 1):
            #Aumenta el contador de los 1s
            contadorunos += 1
    #Obtiene el tamaño del vector
    sizevector = filas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunostrescuartosvertical = contadorunos/sizevector
#    print(razonunoscuartovertical)
    #Regresa el numero de cortes en a 3/4 vertical
    return razonunostrescuartosvertical

#Nombre: vectortrescuartoshorizontal
#Desc: Metodo para calcula el numero de unos en le vector 3/4 / el tamaño del vector
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectortrescuartoshorizontal(img2, filas, columnas):
   #Contador del numero de unos en el vector
    contadorunos = 0
    #Varible para guadar el tamaño del vector
    sizevector = 0
    #Variable para guadar la razon del numero de unos / tamaño del vector
    razonunostrescuartoshorizontal = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    trescuartosvectorhorizontal = int(filas/2)
    #Recorre la línea horizontal de la imagen
    #Ciclo para recorre la linea horizontal calculada
    for x in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[trescuartosvectorhorizontal][x]==1):
            #Aumenta el contador de los 1s
            contadorunos += 1
#            print(corteshc)
    sizevector = columnas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunostrescuartoshorizontal = contadorunos/sizevector
    #Regresa el numero de cortes en a 3/4 horizontal
    return razonunostrescuartoshorizontal

    ############################

#Nombre: lineacuartovertical
#Desc: Metodo para calcula cuantas veces corta al número la línea a un cuarto vertical
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineacuartovertical(img2, filas, columnas):
    #Contadores para numero de cortes
    contadorcortes1 = 0
    contadorcortes0 = 0
    cortescuartovertical = 0
    fila = 0
    #Calcula la línea a 1/4 vertical de la imagen
    cc = int(columnas/4)
    #Recorre la linea vertical seleccionada
    for x in range(filas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[x][cc]
        #Condición para verificar el rango de la fila
        if(x<filas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[x+1][cc]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][cc]==1)):
                #Aumenta el número de cortes a la imagen
                cortescuartovertical = cortescuartovertical + 1
                #Aumenta el número de la fila
                fila = fila + 1
#            print(cortesvc)
    #Regresa el numero de cortes en a 1/4 vertical
    return cortescuartovertical

#Nombre: lineacuartohorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a un cuarto horizontal
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineacuartohorizontal(img2, filas, columnas):
    #Contadores de numero de cortes
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortescuartohorizontal = 0
    #Contador de columna
    columna = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    cr = int(filas/4)
    #Recorre la línea horizontal de la imagen
    for x in range(columnas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[cr][x]
        #Condición para verificar el rango de la columna
        if(x<columnas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[cr][x+1]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[cr][0]==1)):
                #Aumenta el número de cortes a la imagen
                cortescuartohorizontal = cortescuartohorizontal + 1
                #Aumenta el número de la columna
                columna = columna + 1
#            print(corteshc)
    #Regresa el numero de cortes en a 1/4 horizontal
    return cortescuartohorizontal

#Nombre: lineamitadvertical
#Desc: Metodo para calcula cuantas veces corta al número la línea a la mitad vertical
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineamitadvertical(img2, filas, columnas):
    #Contadores de numeros de cortes
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortesmitadvertical = 0
    #Contador de numero de fila
    fila = 0
    #Calcula la línea a 1/2 vertical de la imagen
    medc = int(columnas/2)
    #Recorre la linea vertical seleccionada
    for x in range(filas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[x][medc]
        #Condición para verificar el rango de la fila
        if(x<filas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[x+1][medc]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][medc]==1)):
                #Aumenta el número de cortes a la imagen
                cortesmitadvertical = cortesmitadvertical + 1
                #Aumenta el número de la fila
                fila = fila + 1
#            print(cortesvmit)
    #Regresa el numero de cortes en a 1/2 vertical
    return cortesmitadvertical

#Nombre: lineamitadhorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a la mitad horizontal
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineamitadhorizontal(img2, filas, columnas):
    #Contadores de los cortes de unos y ceros
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortesmitadhorizontal = 0
    #Contador de la columna 
    columna = 0
    #Calcula la línea a 1/2 horizaontal de la imagen
    medr = int(filas/2)
    #Recorre la linea horizontal seleccionada
    for x in range(columnas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[medr][x]
        #Condición para verificar el rango de la columna
        if(x<columnas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[medr][x+1]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[medr][0]==1)):
                #Aumenta el número de cortes a la imagen
                cortesmitadhorizontal = cortesmitadhorizontal + 1
                #Aumenta el número de la columna
                columna = columna + 1
#            print(corteshmit)
    #Regresa el numero de cortes en a 1/2 horizontal
    return cortesmitadhorizontal

#Nombre: lineatrescuartosvertical
#Desc: Metodo para calcula cuantas veces corta al número la línea a 3/4 vertical
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineatrescuartosvertical(img2, filas, columnas):
    ##Contadores de los cortes de unos y ceros
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de cortes en la imagen
    cortestrescurtovertical = 0
    #Contador de la fila
    fila = 0
    #Calcula la línea a 3/4 vertical de la imagen
    cc = int((columnas/4)*3)
    #Recorre la linea vertical seleccionada
    for x in range(filas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[x][cc]
        #Condición para verificar el rango de la fila
        if(x<filas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[x+1][cc]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][cc]==1)):
                #Aumenta el número de cortes a la imagen
                cortestrescurtovertical = cortestrescurtovertical + 1
                #Aumenta el número de la fila
                fila = fila + 1
#            print(cortesv3c)
    #Regresa el numero de cortes en a 3/4 vertical
    return cortestrescurtovertical

#Nombre: lineatrescuartoshorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a 3/4 horizontal
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineatrescuartoshorizontal(img2, filas, columnas):
    #Contadores de cortes de unos y ceros
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortestrescuertohorizontal = 0
    #Contador de la columna
    columna = 0
    #Calcula la línea a 3/4 horizaontal de la imagen
    cr = int((filas/4)*3)
    #Recorre la linea horizontal seleccionada
    for x in range(columnas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[cr][x]
        #Condición para verificar el rango de la columna
        if(x<columnas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[cr][x+1]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[cr][0]==1)):
                #Aumenta el número de cortes a la imagen
                cortestrescuertohorizontal = cortestrescuertohorizontal + 1
                #Aumenta el número de la columna
                columna = columna + 1
#            print(cortesh3c)
    #Regresa el numero de cortes en a 3/4 horizontal
    return cortestrescuertohorizontal

#Nombre: cerosunoscruz
#Desc: Metodo para calcula cuantos 1s hay en forma de cruz respecto al área de la imagen
#Argumentos: matriz, filas y columnas
#Regresa: numero de unos
def cerosunoscruz(img2, filas, columnas):
    #Contadore de ceros
    contadoruno1 = 0
    contadoruno2 = 0
    #Calcula la línea a 1/2 vertical de la imagen
    medr = int(filas/2)
    #Calcula la línea a 1/2 horizaontal de la imagen
    medc = int(columnas/2)
#            print(medr)
#            print(medc)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][medc]==1):
            #Aumenta el contador de los 1s
            contadoruno1 = contadoruno1 + 1
    #Ciclo para recorre la linea horizontal calculada
    for y in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[medr][y]==1):
            #Aumenta el contador de los 1s
            contadoruno2 = contadoruno2 + 1
    #Guarda la razón entre el numero de 1s en forma de cruz respecto al área de la imagen 
    razonunoscruz = (contadoruno1 + contadoruno2)/(filas * columnas)
#            print(numt0)
#            print(numt1)
    #Regresa el el total de unos y ceros
    return razonunoscruz
    
#Nombre: Dataset
#Desc: Metodo leer los directorios y crear dataset
#Argumentos: no tiene argumentos de entrada
def Dataset():

    #Arreglo para juntar datos para el dataset
    dataset = []

    #Ruta de directorio de las imagenes
    rootDir= './dataset/'
    #Creación del archivo csv
    f = open('dataset.csv','w',newline='')
    #Delimitación del archivo cvs a traves de una coma.
    obj = csv.writer(f,delimiter=',')    

    #Recorer los directorios dentro de rootDir
    #dirName: El siguiente directorio en el que se encontró
    #subdirList: Una lista de los subdirectorios en el directorio actual
    #fileList: Una lista de los subdirectorios en el directorio actual.
    for dirName, subdirList, fileList in os.walk(rootDir):
        #Imprime la direccion del directorio actual
        print('Identificando clase: %s' % dirName)

        #Recore cada subdirectorio
        for fname in fileList:
            #concatena y guarda en una variable la ruta de la imagen
            nombre = dirName + '/' + fname
            #Guarda el nombre de la clase actual
            numeroclase = dirName[10]
#            print(clasenum)
            
            #Llamar la funcion de matriz imagen para obtener el numero de filas y columnas
            (img2, filas, columnas) = matrizimagen(nombre)
            #LLamar la funcion de Razon filas columnas
            razonfilascolumnas = razon_filascolumnas(filas, columnas)
            #Llamar la funcion unoscerosimagen para calcula cuantos 1s hay respecto al área del imagen
            razonunos = unosimagen(img2, filas, columnas)
            #Llamar la funcion vectorcuartovertical para calcular la razon del numero de unos / tamaño del vector1/4 vertical
            razonunoscuartovertical = vectorcuartovertical(img2, filas, columnas)
            #Llamar la funcion vectorcuartohorizontal para calcular la razon del numero de unos / tamaño del vector1/4 horizontal
            razonunoscuartohorizontal = vectorcuartohorizontal(img2, filas, columnas)
            #Llamar la funcion vectormitadvertical para calcular la razon del numero de unos / tamaño del vector1/2 vertical
            razonunosmitadvertical = vectormitadvertical(img2, filas, columnas)
            #Llamar la funcion vectormitadhorizontal para calcular la razon del numero de unos / tamaño del vector1/2 horizontal
            razonunosmitadhorizontal = vectormitadhorizontal(img2, filas, columnas)
            #Llamar la funcion vectortrescuartosvertical para calcular la razon del numero de unos / tamaño del vector3/4 vertical
            razonunostrescuartosvertical = vectortrescuartosvertical(img2, filas, columnas)
            #Llamar la funcion vectortrescuartoshorizontal para calcular la razon del numero de unos / tamaño del vector3/4 horizontal
            razonunostrescuartoshorizontal = vectortrescuartoshorizontal(img2, filas, columnas)
            #Llamar la funcion cortesvertical para calcula cuantas veces corta al número la línea a un cuarto vertical
            cortescuartovertical = lineacuartovertical(img2, filas, columnas)
            #Llamar la funcion lineacuartohorizontal para calcula cuantas veces corta al número la línea a un cuarto horizontal
            cortescuartohorizontal = lineacuartohorizontal(img2, filas, columnas)
            #Llamar la funcion lineamitadvertical para calcula cuantas veces corta al número la línea a la mitad vertical
            cortesmitadvertical = lineamitadvertical(img2, filas, columnas)
            #Llamar la funcion lineamitadhorizontal para calcula cuantas veces corta al número la línea a la mitad horizontal
            cortesmitadhorizontal = lineamitadhorizontal(img2, filas, columnas)
            #Llamar la funcion lineatrescuartosvertical para calcula cuantas veces corta al número la línea a 3/4 vertical
            cortestrescurtovertical = lineatrescuartosvertical(img2, filas, columnas)
            #Llamar la funcion lineatrescuartoshorizontal para calcula cuantas veces corta al número la línea a 3/4 horizontal
            cortestrescuertohorizontal = lineatrescuartoshorizontal(img2, filas, columnas)
            #Llamar la funcion cerosunoscruz para calcula cuantos 1s y 0s hay en forma de cruz respecto al área de la imagen
            razonunoscruz = cerosunoscruz(img2, filas, columnas)
            #append añade un elemento a la final de la lista dataset
            dataset.append([razonfilascolumnas,razonunos,razonunoscuartovertical,razonunoscuartohorizontal,razonunosmitadvertical,razonunosmitadhorizontal,razonunostrescuartosvertical,razonunostrescuartoshorizontal,cortescuartovertical,cortescuartohorizontal,cortesmitadvertical,cortesmitadhorizontal,cortestrescurtovertical,cortestrescuertohorizontal,razonunoscruz,numeroclase])
#        print(dataset)

    #Agrega una nueva línea despues de cada línea
    obj.writerows(dataset)
    #Cierra el archivo csv
    f.close()
    
#Llamar la función Dataset
Dataset()