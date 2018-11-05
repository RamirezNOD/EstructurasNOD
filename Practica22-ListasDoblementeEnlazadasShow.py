apuntador = None

class Nodo(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def push(self):
        global apuntador
        apuntadorAux = apuntador
        apuntador.next = self        
        apuntador = self
        apuntador.prev = apuntadorAux
        print("Se ha ingresado: "+self.data)
            
    def peek(raiz, sentido):
        global apuntador        
        mostrar = ""
        if (sentido == 1):
            reco = raiz
            while (reco != None):
                mostrar = mostrar + "[" + str(reco.data) + "] "
                reco = reco.next
        else:
            reco = apuntador
            while (reco != None):
                mostrar = mostrar + "[" + str(reco.data) + "] "
                reco = reco.prev      
        print (mostrar)
        
    def pop(raiz, item):
        reco = raiz
        encontrado = 0
        while (encontrado != 1 and reco != None):            
            if (reco.data == item):
                encontrado = 1
            else:
                reco = reco.next
                
        if (encontrado == 1):   
            reco.prev.next = reco.next
            reco.next.prev = reco.prev
            del reco
            print ("Se ha eliminado: " + str(item))            
        else:
            print("No encontrado.")
            
    def search(raiz, item):        
        reco = raiz
        encontrado = 0
        while (encontrado != 1 and reco != None):            
            if (reco.data == item):
                encontrado = 1
            else:
                reco = reco.next
        if (encontrado == 1):
            print("Encontrado: "+str(reco.data)+" \n\tPrev: "+str(reco.prev.data)+" \n\tNext: "+str(reco.next.data))
        else:
            print(item +" No encontrado.")


opcion = 0
raiz = Nodo("raiz")
apuntador = raiz
miNodo = None

while (opcion != 5):                                      
    opcion = int(input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t2)Eliminar elemento\n\t3)Mostrar\n\t5)Salir \t"))   
    if opcion == 1:
        miNodo = Nodo(input("Ingresa elemento: "))
        miNodo.push()
    else:
        if opcion == 2:
            Nodo.pop(raiz, input("Ingresa elemento a borrar: "))
        else:
            if opcion == 3:
                opcion = int(input("\t\t\t1)Leer de izquierda a derecha\n\t\t\t2)Leer de derecha a izquierda\n\t\t\t3)Leer raiz\n\t\t\t4)Final de cada lado \t"))
                if (opcion == 1 or opcion == 2):
                    Nodo.peek(raiz, opcion)
                else:
                    if opcion == 3:
                        print ("Raiz: " + raiz.data)
                    else:
                        if opcion == 4:
                            print ("Final de la lista lado derecho: " + apuntador.data + "\nFinal de la lista lado izquierdo: " + raiz.next.data)
                        else:
                            print("Opcion invalida.")
            else:
                if opcion != 5:
                    print("Ingrese opcion valida")
  
print("Adios.") 
