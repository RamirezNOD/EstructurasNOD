from random import shuffle
import copy
import time
#######################################Ordenamiento Burbuja######################################
def burbuja(miArreglo):
    for i in range (0, len(miArreglo)-1):
        for j in range (0, len(miArreglo)-1-i):
            if (miArreglo[j] > miArreglo[j+1]):
                miArreglo[j], miArreglo[j+1] = miArreglo[j+1], miArreglo[j]

#######################################Ordenamiento quicksort######################################
def quicksort(arreglo):    
    #Si la longitud del arreglo recivido es mayor a 1, dale
    if len(arreglo) > 1:
        #Declarar los tres arreglos a usar
        arrMayores = []
        arrMenores = []
        arrMedios = []
        #Asignamos el pivote en el primer elemento
        piv = arreglo[0]

        #Comparamos los elementos con el pivote
        #Asignamos a cada arreglo los menores/mayores
        #Respecto a nuestro pivote
        for i in range(0, len(arreglo)):
            if arreglo[i] < piv:
                arrMenores.append(arreglo[i])
            elif  arreglo[i] > piv:
                arrMayores.append(arreglo[i])
            else:
                arrMedios.append(arreglo[i])
                
        #Retornamos los tres arreglos concatenados
        return quicksort(arrMenores) + arrMedios + quicksort(arrMayores)
    else:
        #En caso de el arreglo solo tener un elemento
        #retornamos el mismo arreglo sin alterarlo
        return arreglo

#######################################Ordenamiento shelsort######################################
def shellsort(miArreglo):
    reco = len(miArreglo)//2

    #Hasta que reco sera 0.
    while(reco!=0):
        #Decimos que hay cambio para entrar al ciclo
        cambio = 1
        #Mientras haya cambio, seguiremos iterando
        while cambio == 1:
            cambio = 0
            #Comparamos los elementos usando el reco para tomarlos.
            for index in range(0,len(miArreglo)-reco):
                #Si es mayor, se intercambian
                if (miArreglo[index] > miArreglo[index+reco]):
                    miArreglo[index],miArreglo[index+reco]=miArreglo[index+reco],miArreglo[index]
                    cambio = 1
        #Dividimos nuevamente el reco
        reco = reco//2

######################################Ordenamiento mergesort######################################
def mergesort(ahri):
    #Si el arreglo tiene mas de 1 elemento entraremos al proceso
    if (len(ahri)>1):
        med = len(ahri)//2
        
        #Partimos en mitades hasta llegar a 1 elemento por arreglo
        ahriLeft = mergesort(ahri[:med])
        ahriRight = mergesort(ahri[med:])

        #Empezamos a comparar los elementos y los vamos ingresando al nuevo arreglo
        ahriOrd = []
        
        while(len(ahriLeft) != 0 and len(ahriRight) != 0):
            if ahriLeft[0]< ahriRight[0]: #Ingresamos del arreglo correspondiente al arreglo ordenado
               ahriOrd.append(ahriLeft[0]) #Y quitamos del arreglo que corresponda
               ahriLeft.remove(ahriLeft[0])
            else:
                ahriOrd.append(ahriRight[0])
                ahriRight.remove(ahriRight[0])
                
        #Para evitar problemas de desbordamiento, usamos una comparacion fuera del ciclo
        #Ya que puede darse el caso de que sobre un elemento en alguno de los dos arreglos
        #De ser asi lo agregamos al arreglo.
        if len(ahriLeft) !=0:
            ahriOrd += ahriLeft
        else:
            ahriOrd += ahriRight

        return ahriOrd #Y retornamos el arreglo ya ordenado
    else:
        return (ahri) #En caso de que el arreglo sea de 1 elemento, lo retornamos tal cual llego


##################################################################################################

rep = 50 #Cuantas repeticiones queremos probar
numElem = 2500 #Numero de elementos que se usaran en el arreglo

arregloPrincipal = [[i] for i in range(numElem)] #Generar un arreglo de numElem elementos
shuffle(arregloPrincipal) #Revolvemos el arreglo generado antes

tiempoInicio = 0 #Marca el inicio del programa
tiempoTest = 0 #Es el total calculado desde el inicio hasta que se detuvo el programa
tiempoPromedio = 0 #El promedio de todos los tiempos capturados del metodo

print("Bubblesort: ")
for i in range(0,rep): #Iteramos el numero dado de repeticiones
    arr = arregloPrincipal.copy() #Cargamos el metodo generado a un auxiliar
    tiempoInicio = time.time() #tomamos el tiempo inicial
    burbuja(arr) #Invocamos al metodo
    tiempoTest = float("{0:.4f}".format(time.time() - tiempoInicio)) #Capturamos el tiempo del test
    print("Test "+str(i+1)+": "+str(tiempoTest)) #imprimimos el tiempo medido en i prueba
    tiempoPromedio += tiempoTest #Sumaremos cada tiempo que se mida
tiempoPromedio = tiempoPromedio / rep #Promediamos los tiempos obtenidos
print("\tPromedio: "+"{0:.4f}".format(tiempoPromedio)+" s") #Desplegamos el promedio


print("\n******************************************\nQuicksort: ")
tiempoPromedio = 0 #Reiniciamos el promedio
for i in range(0,rep): #Iteramos el numero dado de repeticiones
    arr = arregloPrincipal.copy() #Cargamos el metodo generado a un auxiliar
    tiempoInicio = time.time() #tomamos el tiempo inicial
    quicksort(arr) #Invocamos al metodo
    tiempoTest = float("{0:.4f}".format(time.time() - tiempoInicio)) #Capturamos el tiempo del test
    print("Test "+str(i+1)+": "+str(tiempoTest)) #imprimimos el tiempo medido en i prueba
    tiempoPromedio += tiempoTest #Sumaremos cada tiempo que se mida
tiempoPromedio = tiempoPromedio / rep #Promediamos los tiempos obtenidos
print("\tPromedio: "+"{0:.4f}".format(tiempoPromedio)+" s") #Desplegamos el promedio


print("\n******************************************\nShellsort: ")
tiempoPromedio = 0 #Reiniciamos el promedio
for i in range(0,rep): #Iteramos el numero dado de repeticiones
    arr = arregloPrincipal.copy() #Cargamos el metodo generado a un auxiliar
    tiempoInicio = time.time() #tomamos el tiempo inicial
    shellsort(arr) #Invocamos al metodo
    tiempoTest = float("{0:.4f}".format(time.time() - tiempoInicio)) #Capturamos el tiempo del test
    print("Test "+str(i+1)+": "+str(tiempoTest)) #imprimimos el tiempo medido en i prueba
    tiempoPromedio += tiempoTest #Sumaremos cada tiempo que se mida
tiempoPromedio = tiempoPromedio / rep #Promediamos los tiempos obtenidos
print("\tPromedio: "+"{0:.4f}".format(tiempoPromedio)+" s") #Desplegamos el promedio



print("\n******************************************\nMergesort: ")
tiempoPromedio = 0 #Reiniciamos el promedio
for i in range(0,rep): #Iteramos el numero dado de repeticiones
    arr = arregloPrincipal.copy() #Cargamos el metodo generado a un auxiliar
    tiempoInicio = time.time() #tomamos el tiempo inicial
    mergesort(arr) #Invocamos al metodo
    tiempoTest = float("{0:.4f}".format(time.time() - tiempoInicio)) #Capturamos el tiempo del test
    print("Test "+str(i+1)+": "+str(tiempoTest)) #imprimimos el tiempo medido en i prueba
    tiempoPromedio += tiempoTest #Sumaremos cada tiempo que se mida
tiempoPromedio = tiempoPromedio / rep #Promediamos los tiempos obtenidos
print("\tPromedio: "+"{0:.4f}".format(tiempoPromedio)+" s") #Desplegamos el promedio

