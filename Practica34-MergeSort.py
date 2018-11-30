#The Merge Sort — Python Code
#Anirudh
#https://pythonandr.com/2015/07/05/the-merge-sort-python-code/
#Modificado 29/11/18 por Leonardo Ramirez

from random import randint

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
            
    
numElem = 10000
rango = 100
opcion = 0
#Generamos un arreglo al azar
miArreglo = []

for i in range(numElem):
    miArreglo.append(randint(0,rango))
print(miArreglo)

#Menu:
while (opcion != "5"):                                      
    opcion = input("\n\nOpcion a realizar: \n\t1)Generar nuevo arreglo\n\t2)Acomodar\n\t5)Salir \t")   
    if opcion == "1":
        for i in range(numElem):
            miArreglo[i] = randint(0,rango)
        print(miArreglo)
    else:
        if opcion == "2":
            print(mergesort(miArreglo))
        else:
            if opcion != "5":
                print("Ingrese opcion valida")
  
print("Adios.")  
