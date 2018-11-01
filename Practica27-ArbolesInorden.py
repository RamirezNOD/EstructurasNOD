apuntador = None

class Nodo(object):
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def push(self):
        global raiz
        apuntador = raiz
        direcc = 0        
        nodosIzq = ""
        nodosDer = ""
        nodosAct = ""        
        
        while (direcc != 4):
            if (apuntador.left == None):
                nodosIzq = ""
            else:
                nodosIzq = apuntador.left.data
                
            if (apuntador.right == None):
                nodosDer = ""  
            else:
                nodosDer = apuntador.right.data
                
            nodosAct = apuntador.data
                
            print ("("+nodosIzq+") <- "+"("+nodosAct+")"+" -> ("+nodosDer+")")
            direcc = int(input("\n\t\t1)Izquierda\n\t\t2)Derecha\n\t\t3)Regresar a la raiz\t"))
            if (direcc == 1):
                if (apuntador.left != None):
                    apuntador = apuntador.left
                else: 
                    apuntador.left = self
                    direcc = 4
                    print("Ha sido ingresado en la izquierda: " + self.data)
            else: 
                if (direcc == 2):
                    if (apuntador.right != None):
                        apuntador = apuntador.right
                    else:
                        apuntador.right = self
                        direcc = 4                  
                        print("Ha sido ingresado en la derecha: " + self.data)
                else: 
                    if (direcc == 3):
                        apuntador = raiz
                    else:
                        print("Ingresa una opcion valida")

    def inorden(self, nodoActual):
        if (nodoActual != None):
            self.inorden(nodoActual.left)
            print("("+nodoActual.data+")", end = " ")
            self.inorden(nodoActual.right)
        
                        
                    
                    
        

opcion = 0
raiz = Nodo("raiz")
apuntador = raiz
miNodo = None

while opcion != 5:
    opcion = int(input("\nMENU:\n\t1)Agregar Nodo\n\t2)Recorrido Inorden\n\t5)Salir\t  "))
    if opcion == 1:
        miNodo = Nodo(input("Ingresa nodo: "))
        miNodo.push()
    else:
        if opcion == 2:
            miNodo.inorden(raiz)
        else:
            if opcion == 5:
                print ("Goodbye :)")
            else:
                print("Ingresa una opcion valida")
