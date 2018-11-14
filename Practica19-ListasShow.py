apuntador = None

class Nodo(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def push(self):
        global apuntador
        apuntador.next = self
        apuntador = self
        print("Se ha ingresado: "+self.data)
            
    def peek(raiz):
        global apuntador        
        mostrar = ""
        reco = raiz
        while (reco != None):
            mostrar = mostrar + "[" + str(reco.data) + "] "
            reco = reco.next     
        print (mostrar)
        
    def pop(raiz, item):
        reco = raiz
        recoAux = raiz
        encontrado = 0
        while (encontrado != 1 and reco != None):            
            if (reco.data == item):
                encontrado = 1
            else:
                recoAux = reco
                reco = reco.next
                
        if (encontrado == 1):   
            recoAux.next = reco.next
            del reco
            del recoAux
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
            print("Encontrado: "+str(reco.data)+"\n\tNext: "+str(reco.next.data))
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
                opcion = int(input("\t\t\t1)Leer todos\n\t\t\t2)Leer raiz\n\t\t\t3)Leer final\n\t\t\t4)Buscar elemento\t"))
                if (opcion == 1):
                    Nodo.peek(raiz)
                else:
                    if opcion == 2:
                        print ("Raiz: " + raiz.data)
                    else:
                        if opcion == 3:
                            print ("Final de la lista: " + apuntador.data)
                        else:
                            if opcion == 4:
                                Nodo.search(raiz, input("Elemento a bucar: "))
                            else:
                                print("Opcion invalida.")
            else:
                if opcion != 5:
                    print("Ingrese opcion valida")
  
print("Adios.") 
