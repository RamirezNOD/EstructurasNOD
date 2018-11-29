from random import randint

def buscarBinario(arr, item, end):
    med = len(arr)//2 #Obtenemos la mitad del arreglo
    if (not end and med != 0): #Si no se ha encontrado y no se ha terminado el arreglo.
        if (str(arr[med]) == str(item)): #Verificamos si es el buscado
            end = True
            print("El elemento "+str(item)+" existe en el arreglo.") 
        else:
            if int(item) < arr[med]: #Verificamos en que lado esta el elemento buscado
                buscarBinario(arr[:med], item, end)
            else:
                buscarBinario(arr[med:], item, end)
    else:
        if (med == 0): #Si se acabo el arreglo, no se encuentra.
            print("\""+item+"\" no se encuentra en el arreglo")
                
    
opcion = 0

#Generamos un arreglo al azar
miArreglo = []
for i in range(50):
    miArreglo.append(randint(0,50))
#Acomodamos el arreglo para buscar el elemento
miArreglo.sort()
print(miArreglo)

#Menu:
while (opcion != "5"):                                      
    opcion = input("\n\nOpcion a realizar: \n\t1)Buscar elemento\n\t5)Salir \t")   
    if opcion == "1":
        buscarBinario(miArreglo, input("Elemento a buscar: "),False)
    else:
        if opcion != "5":
            print("Ingrese opcion valida")
  
print("Adios.") 
