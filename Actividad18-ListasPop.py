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
                print("Aun no se hace.")
            else:
                if opcion != 5:
                    print("Ingrese opcion valida")
  
print("Adios.") 
