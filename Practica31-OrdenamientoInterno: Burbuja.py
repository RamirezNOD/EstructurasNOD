        
def burbuja():
    burbuja = 0
    wea = 0
    global miArreglo
    for i in range (0, len(miArreglo)-1):
        for j in range (0, len(miArreglo)-1-i):
            if (miArreglo[j] > miArreglo[j+1]):
                burbuja = miArreglo[j]
                miArreglo[j] = miArreglo[j+1]
                miArreglo[j+1] = burbuja
    print(miArreglo)
            
    
opcion = 0
miArreglo = []


while (opcion != "5"):                                      
    opcion = input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t2)Acomodar\n\t5)Salir \t")   
    if opcion == "1":
        miArreglo.append(str(input("Ingresar elemento: ")))
        print(miArreglo)
    else:
        if opcion == "2":
            burbuja()
        else:
            if opcion != "5":
                print("Ingrese opcion valida")
  
print("Adios.") 
