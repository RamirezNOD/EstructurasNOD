from random import randint

def shellSort():
    global miArreglo
    reco = len(miArreglo)//2
    index = 0
    aux = 0
    cambio = 0
    #Hasta que la mitad de la longitud sea 0
    while(reco!=0):
        #Iteramos para recorrer el indice, de ser posible
        for salto in range(0, len(miArreglo)//reco -1):
            #Comparamos segun el salto reco
            for index in range(salto,len(miArreglo)-reco,reco):
                #Si es mayor se intercambian
                if (miArreglo[index] > miArreglo[index+reco]):
                    aux = miArreglo[index]
                    miArreglo[index] = miArreglo[index+reco]
                    miArreglo[index+reco] = aux
        reco = reco//2

    #Damos una ultima pasada para asegurarnos.
    for i in range(0,len(miArreglo)-1):
        if miArreglo[i] > miArreglo[i+1]:
            aux = miArreglo[i]
            miArreglo[i] = miArreglo[i+1]
            miArreglo[i+1] = aux
                
    print(miArreglo)
    
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
            shellSort()
        else:
            if opcion != "5":
                print("Ingrese opcion valida")
  
print("Adios.") 
