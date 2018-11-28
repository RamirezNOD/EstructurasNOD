from random import randint

def shellSort():
    global miArreglo
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
            print(miArreglo)
        else:
            if opcion != "5":
                print("Ingrese opcion valida")
  
print("Adios.") 





