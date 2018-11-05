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
            

opcion = 0
raiz = Nodo("raiz")
apuntador = raiz
miNodo = None

while (opcion != 5):                                      
    opcion = int(input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t2)Eliminar elemento\n\t5)Salir \t"))   
    if opcion == 1:
        miNodo = Nodo(input("Ingresa elemento: "))
        miNodo.push()
    else:
        if opcion == 2:
            Nodo.pop(raiz, input("Ingresa elemento a borrar: "))
        else:            
            if opcion != 5:
                print("Ingrese opcion valida")
  
print("Adios.") 
