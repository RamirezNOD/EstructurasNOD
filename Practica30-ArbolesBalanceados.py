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
                
            print ("("+str(nodosIzq)+") <- "+"("+str(nodosAct)+")"+" -> ("+str(nodosDer)+")")
            if (self.data < apuntador.data):
                direcc = 1
            else:
                direcc = 2

            
            if (direcc == 1):
                if (apuntador.left != None):
                    apuntador = apuntador.left
                else: 
                    apuntador.left = self
                    direcc = 4
                    print("Ha sido ingresado en la izquierda: " + str(self.data))
            else: 
                if (direcc == 2):
                    if (apuntador.right != None):
                        apuntador = apuntador.right
                    else:
                        apuntador.right = self
                        direcc = 4                  
                        print("Ha sido ingresado en la derecha: " + str(self.data))
                else: 
                    if (direcc == 3):
                        apuntador = raiz
                    else:
                        print("Ingresa una opcion valida")

    def inorden(self, nodoActual):
        if (nodoActual != None):
            self.inorden(nodoActual.left)
            print("("+str(nodoActual.data)+")", end = " ")
            self.inorden(nodoActual.right)

    def preorden(self, nodoActual):
        if (nodoActual != None):            
            print("("+str(nodoActual.data)+")", end = " ")
            self.inorden(nodoActual.left)
            self.inorden(nodoActual.right)

    def postorden(self, nodoActual):
        if (nodoActual != None):     
            self.inorden(nodoActual.left)
            self.inorden(nodoActual.right)
            print("("+str(nodoActual.data)+")", end = " ")         
        

opcion = 0
raiz = Nodo(int(input("Ingrese raiz: ")))
apuntador = raiz
miNodo = None

while opcion != 5:
    opcion = int(input("\nMENU:\n\t1)Agregar Nodo\n\t2)Recorrido Inorden\n\t3)Recorrido Preorden\n\t4)Recorrido Postorden\n\t5)Salir\t  "))
    if opcion == 1:
        miNodo = Nodo(int(input("Ingresa nodo: ")))
        miNodo.push()
    else:
        if opcion == 2:
            miNodo.inorden(raiz)
        else:
            if opcion == 3:
                miNodo.preorden(raiz)
            else:
                if opcion == 4:
                    miNodo.postorden(raiz)
                else:
                    if opcion == 5:
                        print ("Goodbye :)")
                    else:
                        print("Ingresa una opcion valida")
