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
            print("Aun no se hace.")
        else:
            if opcion == 3:
                print("Aun no se hace.")
            else:
                if opcion != 5:
                    print("Ingrese opcion valida")
  
print("Adios.") 
