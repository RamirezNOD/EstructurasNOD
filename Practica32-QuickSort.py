#Quicksort in Python
#Elliot Forbes
#https://tutorialedge.net/compsci/sorting/quicksort-in-python/
#Editado por Leo Ramirez (23/11/18)
from random import randint

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
        #
        return quicksort(arrMenores) + arrMedios + quicksort(arrMayores)
    else:
        #En caso de el arreglo solo tener un elemento
        #retornamos el mismo arreglo sin alterarlo
        return arreglo
                
    
    
opcion = 0
#Generamos un arreglo al azar
miArreglo = []
for i in range(10):
    miArreglo.append(randint(0,10))
print(miArreglo)

#Menu:
while (opcion != "5"):                                      
    opcion = input("\n\nOpcion a realizar: \n\t1)Generar nuevo arreglo\n\t2)Acomodar\n\t5)Salir \t")   
    if opcion == "1":
        for i in range(10):
            miArreglo[i] = randint(0,10)
        print(miArreglo)
    else:
        if opcion == "2":
            print(miArreglo)
            print(quicksort(miArreglo))
        else:
            if opcion != "5":
                print("Ingrese opcion valida")
  
print("Adios.") 
