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

            
opcion = 0
raiz = Nodo(input("Ingrese raiz: "))
apuntador = raiz
miNodo = None

#Menu:
while (opcion != 5):                                      
    opcion = int(input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t5)Salir \t"))   
    if opcion == 1:
        miNodo = Nodo(input("Ingresa elemento: "))
        miNodo.push(raiz)
    else:           
        if opcion != 5:
            print("Ingrese opcion valida")
  
print("Adios.") 
