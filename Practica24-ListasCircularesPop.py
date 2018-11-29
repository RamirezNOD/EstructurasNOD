apuntador = None

class Nodo(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def push(self,raiz):
        global apuntador
        apuntador.next = self #Enlazamos el nodo creado al ultimo que tenemos
        apuntador = self
        apuntador.next = raiz #Asignamos siempre la raiz como el next del ultimo elemento.
        print("Se ha ingresado: "+self.data)
        
    def pop(raiz, item):
        reco = raiz
        recoAux = raiz
        encontrado = 0
        while (True):            
            if (reco.data == item): #Si se encuentra se termina el ciclo
                encontrado = 1
                break;
            else:
                if (reco.next == raiz): #Si se acaba salimos del ciclo
                    break
                recoAux = reco
                reco = reco.next
                
        if (encontrado == 1):   #Perder el enlace del nodo
            recoAux.next = reco.next
            del reco #Borrar el nodo
            del recoAux
            print ("Se ha eliminado: " + str(item))            
        else:
            print("No encontrado.")

            
opcion = 0
raiz = Nodo(input("Ingrese raiz: "))
apuntador = raiz
miNodo = None

#Menu:
while (opcion != 5):                                      
    opcion = int(input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t2)Eliminar elemento\n\t5)Salir \t"))   
    if opcion == 1:
        miNodo = Nodo(input("Ingresa elemento: "))
        miNodo.push(raiz)
    else:
        if opcion == 2:
            Nodo.pop(raiz, input("Ingresa elemento a borrar: "))
        else:           
            if opcion != 5:
                print("Ingrese opcion valida")
  
print("Adios.") 
