from random import randint

def buscar(item):
    global miArreglo
    reco = len(miArreglo)//2
    i = 0
    encontrado = False

    #Mientras no se encuentre el elemento y no terminemos el arreglo seguira.
    while(encontrado != True and i < len(miArreglo)):
        #Si es el item buscado, nos detendremos y mostraremos en que posicion esta.
        if (str(miArreglo[i])==str(item)):
            encontrado = True
            print ("Elemeto encontrado en posicion: "+str(i))
        i += 1
        
                
    
opcion = 0

#Generamos un arreglo al azar
miArreglo = []
for i in range(10):
    miArreglo.append(randint(0,10))
print(miArreglo)

#Menu:
while (opcion != "5"):                                      
    opcion = input("\n\nOpcion a realizar: \n\t1)Buscar elemento\n\t5)Salir \t")   
    if opcion == "1":
        buscar(input("Elemento a buscar: "))
    else:
        if opcion != "5":
            print("Ingrese opcion valida")
  
print("Adios.") 
