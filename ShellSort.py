def shellSort():
    global miArreglo
    reco = len(miArreglo)//2
    index = 0
    aux = 0
    while(reco!=0):
        for index in range(0,len(miArreglo)-1):
            if (index+reco < len(miArreglo)):
                if (miArreglo[index] > miArreglo[index+reco]):
                    print(miArreglo)
                    aux = miArreglo[index]
                    miArreglo[index] = miArreglo[index+reco]
                    miArreglo[index+reco] = aux
        reco = reco//2    
    print(miArreglo)
    
    
opcion = 0
miArreglo = [10,4,7,1,3,6,5,2,9,8]


while (opcion != "5"):                                      
    opcion = input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t2)Acomodar\n\t5)Salir \t")   
    if opcion == "1":
        miArreglo.append(str(input("Ingresar elemento: ")))
        print(miArreglo)
    else:
        if opcion == "2":
            shellSort()
        else:
            if opcion != "5":
                print("Ingrese opcion valida")
  
print("Adios.") 
