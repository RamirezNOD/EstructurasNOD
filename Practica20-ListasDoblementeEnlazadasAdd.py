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
        print("Se ingreso: "+ self.data)
              

opcion = 0
raiz = Nodo("raiz")
apuntador = raiz
miNodo = None

while (opcion != 5):                                      
    opcion = int(input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t5)Salir \t"))   
    if opcion == 1:
        miNodo = Nodo(input("Ingresa elemento: "))
        miNodo.push()
    else:
        if opcion != 5:
            print("Ingrese opcion valida")
  
print("Adios.") 
