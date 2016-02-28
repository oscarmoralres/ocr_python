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
   
#Nombre: areaimagen
#Desc: Metodo para obtener el área de la imagen
#Argumentos: filas y columnas
#Regresa: razon filas/columnas
def areaimagen(filas, columnas):
    #Variable para almacenar el area de la imagen
    area = 0
    #Caracteristica 2.. Calcula el area de la imagen
    area = filas*columnas
    #Regresa el área de la imagen
    return area
#    print(razonfilcol)

#Nombre: unoscerosarea 
#Desc: Metodo para calcular el numero de unos en la imagen
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos y razon de ceros
def unoscerosarea(img2, filas, columnas):
    #Contadores del numero de ceros y unos
    contadorcero = 0
    contadoruno = 0
    #Calcula la mitad de la imagen respecto a las filas
    med = int(filas/2)
    #print(med)
    #Recorre la solo la fila seleccionada
    for x in range(med):
        #Recorre todas las columnas de la matriz
        for y in range(columnas):
            #Condicion para verificar si el pixel es igual a 0
            if(img2[x][y]==0):
                #Aumenta el contador de los 0s
                contadorcero = contadorcero + 1
            else:
                #Aumenta el contador de los 1s
                contadoruno = contadoruno + 1
#            print(cont0_1)
#            print(cont1_1)
    #Guarda la razón entre el numero de 1s respecto al mitad del área de la imagen
    razonunos = contadoruno
    #Guarda la razón entre el numero de 0s respecto al mitad del área de la imagen
    razonceros = contadorcero
    #regresa el razon de unos y ceros
    return razonunos, razonceros

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

#Nombre: unoscerosimagen
#Desc: Metodo para calcula cuantos 1s y 0s hay respecto al área del imagen
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos y razon de ceros respecto al area
def unoscerosimagen(img2, filas, columnas):
    #Contadores de unos y ceros
    contadorcero = 0
    contadoruno = 0
    #Contadores de razon de unos y ceros respecto al área
    razonunos = 0
    razonceros = 0
    #Ciclo para recorer las filas de la matriz
    for x in range(filas):
        #Ciclo para recorer las columnas de la matriz
        for y in range(columnas):
            #Condición para verificar el pixel igual a 0
            if(img2[x][y]==0):
                #Aumenta el contador de los ceros
                contadorcero = contadorcero + 1
            else:
                #Aumenta el contador de los unos
                contadoruno = contadoruno + 1
    #Guarda la razón entre el numero de 1s respecto al área de la imagen
    razonunos = contadoruno/(filas*columnas)
    #Guarda la razón entre el numero de 0s respecto al área de la imagen
    razonceros = contadorcero/(filas*columnas)
#            print(razon1)
#            print(razon0)
    #Regresa la razon de unos y ceros
    return razonunos, razonceros

#Nombre: cerosunoscruz
#Desc: Metodo para calcula cuantos 1s y 0s hay en forma de cruz respecto al área de la imagen
#Argumentos: matriz, filas y columnas
#Regresa: numero de unos y numeros de ceros
def cerosunoscruz(img2, filas, columnas):
    #Contadores de ceros y unos 
    contadorcero1 = 0
    contadorcero2 = 0
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
        if(img2[x][medc]==0):
            #Aumenta el contador de los 0s
            contadorcero1 = contadorcero1 + 1
        else:
            #Aumenta el contador de los 1s
            contadoruno1 = contadoruno1 + 1
    #Ciclo para recorre la linea horizontal calculada
    for y in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[medr][y]==0):
            #Aumenta el contador de los 0s
            contadorcero2 = contadorcero2 + 1
        else:
            #Aumenta el contador de los 1s
            contadoruno2 = contadoruno2 + 1
    #Guarda la razón entre el numero de 0s en forma de cruz respecto al área de la imagen
    razonceroscruz = (contadorcero1 + contadorcero2)
    #Guarda la razón entre el numero de 1s en forma de cruz respecto al área de la imagen 
    razonunoscruz = (contadoruno1 + contadoruno2)
#            print(numt0)
#            print(numt1)
    #Regresa el el total de unos y ceros
    return razonceroscruz, razonunoscruz
    
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
            #Llamar la funcion de areaimagen para obtener el area de la imagen
            area = areaimagen(filas, columnas)
            #Llamar la funcion para calcular el numero de unos en la imagen
            (razonunos, razonceros) = unoscerosarea(img2, filas, columnas)
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
            #Llamar la funcion unoscerosimagen para calcula cuantos 1s y 0s hay respecto al área del imagen
            (razonunos, razonceros) = unoscerosimagen(img2, filas, columnas)
            #Llamar la funcion cerosunoscruz para calcula cuantos 1s y 0s hay en forma de cruz respecto al área de la imagen
            (razonceroscruz, razonunoscruz) = cerosunoscruz(img2, filas, columnas)
            #c11 = especial(img2, filas, columnas);
            #append añade un elemento a la final de la lista dataset
            dataset.append([razonfilascolumnas,area,razonunos,razonceros,cortescuartovertical,cortescuartohorizontal,cortesmitadvertical,cortesmitadhorizontal,cortestrescurtovertical,cortestrescuertohorizontal,razonunos,razonceros,razonceroscruz,razonunoscruz,numeroclase])
#        print(dataset)

    #Agrega una nueva línea despues de cada línea
    obj.writerows(dataset)
    #Cierra el archivo csv
    f.close()
    
#Llamar la función Dataset
#Dataset()