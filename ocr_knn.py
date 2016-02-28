# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:21:44 2016

@author: Oscar
"""

#Biblioteca para escribir datos en un archivo csv
import csv
#Biblioteca para funciones matemáticas
import math
#Importacion de el archivo ocr_dataset
import ocr_dataset as caracteristicasimg

#Nombre: nuevaInstancia
#Desc: Metodo para obtener caracteristicas de la nueva instancia
#Párametro: ruta de la imagen
#Regresa: Regresa las caracteristicas de la nueva instancia
def nuevaInstanciaK(ruta):
    
    #Llamar la funcion de matriz imagen para obtener el numero de filas y columnas
    (img2, filas, columnas) = caracteristicasimg.matrizimagen(ruta)
    #LLamar la funcion de Razon filas columnas
    razonfilascolumnas = caracteristicasimg.razon_filascolumnas(filas, columnas)
    #Llamar la funcion de areaimagen para obtener el area de la imagen
    area = caracteristicasimg.areaimagen(filas, columnas)
    #Llamar la funcion para calcular el numero de unos en la imagen
    (razonunos, razonceros) = caracteristicasimg.unoscerosarea(img2, filas, columnas)
    #Llamar la funcion cortesvertical para calcula cuantas veces corta al número la línea a un cuarto vertical
    cortescuartovertical = caracteristicasimg.lineacuartovertical(img2, filas, columnas)
    #Llamar la funcion lineacuartohorizontal para calcula cuantas veces corta al número la línea a un cuarto horizontal
    cortescuartohorizontal = caracteristicasimg.lineacuartohorizontal(img2, filas, columnas)
    #Llamar la funcion lineamitadvertical para calcula cuantas veces corta al número la línea a la mitad vertical
    cortesmitadvertical = caracteristicasimg.lineamitadvertical(img2, filas, columnas)
    #Llamar la funcion lineamitadhorizontal para calcula cuantas veces corta al número la línea a la mitad horizontal
    cortesmitadhorizontal = caracteristicasimg.lineamitadhorizontal(img2, filas, columnas)
    #Llamar la funcion lineatrescuartosvertical para calcula cuantas veces corta al número la línea a 3/4 vertical
    cortestrescurtovertical = caracteristicasimg.lineatrescuartosvertical(img2, filas, columnas)
    #Llamar la funcion lineatrescuartoshorizontal para calcula cuantas veces corta al número la línea a 3/4 horizontal
    cortestrescuertohorizontal = caracteristicasimg.lineatrescuartoshorizontal(img2, filas, columnas)
    #Llamar la funcion unoscerosimagen para calcula cuantos 1s y 0s hay respecto al área del imagen
    (razonunos, razonceros) = caracteristicasimg.unoscerosimagen(img2, filas, columnas)
    #Llamar la funcion cerosunoscruz para calcula cuantos 1s y 0s hay en forma de cruz respecto al área de la imagen
    (razonceroscruz, razonunoscruz) = caracteristicasimg.cerosunoscruz(img2, filas, columnas)
    #Número de k vecinos mas cercanos
    k = 11
    #Arreglo con las caracteristicas calculadas
    nuevainstancia = [razonfilascolumnas,area,razonunos,razonceros,cortescuartovertical,cortescuartohorizontal,cortesmitadvertical,cortesmitadhorizontal,cortestrescurtovertical,cortestrescuertohorizontal,razonunos,razonceros,razonceroscruz,razonunoscruz,k]
    
    #Regresa las caracteristicas obtenidas de la nueva instacia
    return nuevainstancia

#Nombre: cargarDataset
#Desc: Metodo para cargar el archivo dataset
#Párametro: nombrearchivo
#Regresa: Regresa el dataset
def cargarDataset(nombrearchivo):
	#Abrir el archivo csv con permisos de leer
    with open(nombrearchivo, 'r') as csvfile:
    	#Leer un archivo con reader()
        lineas = csv.reader(csvfile)
        #Obtener lista de de cada instancia
        dataset = list(lineas)
        #Recorrer cada instancia obtenida
        for x in range(len(dataset)):
        	#Ciclo para recorrer cada caraacteristica de la instancia
            for y in range(15):
            	#Condicion para verificar el tamaño de las caracteristicas
                if(y<14):
                	#Convierte los valores del dataset en flotantes
                    dataset[x][y] = float(dataset[x][y])
                else:
                	#Guarda el valor de la clase
                    dataset[x][y] = dataset[x][y]
                #print(dataset[x][y])
    #Regresa el dataset cargado en un arreglo
    return dataset

#Nombre: calcularDistancia
#Desc: Metodo para calcular la distancia eucladiana de la nueva instancia con el dataset
#Párametro: dataset y la nueva instancia
#Regresa: Regresa la distancia calculada
def calcularDistancia(dataset,nuevainstancia):
	#Arreglo para guardar las distancias calculadas
    distancias = []
    #Ciclo para 
    for x in range(len(dataset)):
        distancias.append([math.sqrt(pow((dataset[x][0] - float(nuevainstancia[0])),2)+pow((dataset[x][1]-float(nuevainstancia[1])),2)+pow((dataset[x][2]-float(nuevainstancia[2])),2)+pow((dataset[x][3]-float(nuevainstancia[3])),2)+pow((dataset[x][4]-float(nuevainstancia[4])),2)+pow((dataset[x][5]-float(nuevainstancia[5])),2)+pow((dataset[x][6]-float(nuevainstancia[6])),2)+pow((dataset[x][7]-float(nuevainstancia[7])),2)+pow((dataset[x][8]-float(nuevainstancia[8])),2)+pow((dataset[x][9]-float(nuevainstancia[9])),2)+pow((dataset[x][10]-float(nuevainstancia[10])),2)+pow((dataset[x][11]-float(nuevainstancia[11])),2)+pow((dataset[x][12]-float(nuevainstancia[12])),2)+pow((dataset[x][13]-float(nuevainstancia[13])),2)),dataset[x][14],(x+1)])
    #print(distancias)
    #Variable auxiliar para guardar el valor de la distancia
    auxiliar = 0
    #Variable para almacenar el tamaño del arreglo distancias
    tamaño = len(distancias)
    #Ciclo para recorrer el tamaño del arreglo
    for i in range(1, tamaño):
    	#Ciclo para recorrer las instancias
        for j in range(0,tamaño-1):
        	#Verifica el tmaño de la instancia actual
            if(distancias[j]>distancias[j+1]):
            	#Guarda el valor de la instacia posterior
               	auxiliar = distancias[j+1]
               	#Iguala el valor de la distancia posterior a la actual
               	distancias[j+1] = distancias[j]
               	#Iguala el valor de la distancia actual a la auxiliar
               	distancias[j] = auxiliar
    #Regresa las distancias ordenadas ascendentes
    return distancias     

#Nombre: clasificarInstancia
#Desc: Metodo para clasificar la nueva instancia
#Párametro: distancias y la nueva instancia
#Regresa: Regresa la distancia calculada
def clasificarInstancia(distancias,nuevainstancia):
    #Contadores para el numero de veces que se repite la clase
    clase0 = 0
    clase1 = 0
    clase2 = 0
    clase3 = 0
    clase4 = 0
    clase5 = 0
    clase6 = 0
    clase7 = 0
    clase8 = 0
    clase9 = 0
    #Arreglo para guardar los contadores
    totalclase = []
    print('\n')
    #Mensaje en pantalla de las columnas...
    print("\t  K\t     Distancias      Clase  Id") 
    print("\t___________________________________________")
    #Variable para contsar el numero de k vecinos
    contador = 1
    #Ciclo para recorrer el arreglo de la nueva instancia
    for x in range(int(nuevainstancia[14])):
    	#Imprime en pantalla las distancias k vecinas más cercanas
        print('\tI - '+str(contador)+' =\t'+str(distancias[x]))
        #Verifica si la clase es igual a 0
        if(distancias[x][1] == '0'):
            #Aumenta la clase 0 en uno
            clase0 += 1
        #Verifica si la clase es igual a 1
        if(distancias[x][1] == '1'):
            #Aumenta la clase 1 en uno
            clase1 += 1
        #Verifica si la clase es igual a 2
        if(distancias[x][1] == '2'):
            #Aumenta la clase 2 en uno
            clase2 += 1
        #Verifica si la clase es igual a 3
        if(distancias[x][1] == '3'):
            #Aumenta la clase 3 en uno
            clase3 += 1
        #Verifica si la clase es igual a 4
        if(distancias[x][1] == '4'):
            #Aumenta la clase 4 en uno
            clase4 += 1
        #Verifica si la clase es igual a 5
        if(distancias[x][1] == '5'):
            #Aumenta la clase 5 en uno
            clase5 += 1
        #Verifica si la clase es igual a 6
        if(distancias[x][1] == '6'):
            clase6 += 1
        #Verifica si la clase es igual a 7
        if(distancias[x][1] == '7'):
            #Aumenta la clase 7 en uno
            clase7 += 1
        #Verifica si la clase es igual a 8
        if(distancias[x][1] == '8'):
            #Aumenta la clase 8 en uno
            clase8 += 1
        #Verifica si la clase es igual a 9
        if(distancias[x][1] == '9'):
            #Aumenta la clase 9 en uno
            clase9 += 1
        #Aumenta el contador de k vecinos
        contador += 1
    #Guarda los contadores de las clases en un arreglo
    totalclase = [clase0, clase1,clase2,clase3,clase4,clase5,clase6,clase7,clase8,clase9]
    print("\n")
    #Contador para las clases
    contador2 = 0
    #Variable auxiliar para valor de la clase
    auxiliar = 0
    #Ciclo para recorrer el arreglo totalclase
    for x in range(len(totalclase)):
        #Mensaje en pantalla de cuants veces se repite la clase
        print('\t\tTotal de la Clase '+str(contador2)+' = '+str(totalclase[x]))
        #Condicion para verificar las veces que se repite la clase
        if(auxiliar <= totalclase[x]):
            #Guarda el valor de la clase que mas se repite
            auxiliar = totalclase[x]
            #Guarda la identidad de la clase
            claseidentidad = x
        #Aumenta el contador de las clases
        contador2 += 1
    #Mensaje en pantalla del caracter identificado
    print('\n\t\tCaracter Identificado: ' + str(claseidentidad))
    
#nuevainstancia = nuevaInstanciaK() 

#Nombre: main
#Desc: Metodo principal del programa
#Argumentos: No tiene argumentos de netrada
def main():
    #Mensaje en pantalla
    print('\n\n\t      Identificando caracteristicas!')
    #Se define la ruta de la imagen
    ruta = 'C:/Users/user/Documents/8 cuatrimestre/Mineria de Datos/ocr/test/2.png'
    #Llama al metodo nuevainstancia y le manda como parametro la ruta de la imagen
    nuevainstancia = nuevaInstanciaK(ruta)
    #Llama al metodo cargarDataset y le manda como parametro el nombre del dataset
    dataset = cargarDataset('dataset.csv')
    #Se obtiene el tamaño de instancias en el dataset
    tam = len(dataset)
    #Mensaje en pantalla total de instancias
    print("\n\t        Total de intancias: "+str(tam))
    #Llama al metodo calcularDistancia para calcular la distancia entre el dataset y la nueva instancia
    distancia = calcularDistancia(dataset,nuevainstancia)
    #Llamar al metodo clasificarInstancia para clasificar la nueva instancia 
    clasificarInstancia(distancia,nuevainstancia)

#clasificarInstancia(calcularDistancia(cargarDataset('dataset.csv'),nuevainstancia),nuevainstancia)
main()