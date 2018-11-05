class Queue:    
    def __init__(self,nElems):
        self.queue = []
        self.rear=0
        self.rearDer=nElems-1
        self.maxElem=nElems
        self.elemDer=0
        self.elemIzq=0
            
    def create(self):
        for i in range (0, self.maxElem):                    
            self.queue.append(0)
        
    def add (self, dato, flujo):
        if(self.rear-1 != self.rearDer):
            if flujo == 1:
                self.queue[self.rear] = dato
                self.rear += 1
            else:
                self.queue[self.rearDer] = dato
                self.rearDer -= 1
                
        else:
            print("Cola llena.")

        print(self.queue)

    def delete(self, flujo):
        if flujo == 1:
            if self.rear != 0:                
                for i in range(0,self.rear):
                    self.queue[i]=self.queue[i+1]                
                self.rear -= 1
                self.queue[self.rear] = 0
                print(self.queue)
            else:
                print("Flujo vacío")
        else:
            if self.rearDer != self.maxElem-1:
                for i in range(maxElem-1,self.rear,-1):
                    self.queue[i]=self.queue[i-1]                
                self.rearDer += 1
                self.queue[self.rearDer] = 0
                print(self.queue)
            else:
                print("Flujo vacío")

opcion = 0

maxElem = int(input("Ingrese numero de indices: "))    
cola = Queue(maxElem)  
cola.create()

while (opcion != 5):                                      
    opcion = int(input("\n\nOpcion a realizar: \n\t1)Ingresar elemento\n\t2)Eliminar\n\t5)Salir \t"))   
    if opcion == 1:
        opcion = int(input("\t\t\t1)Ingresar por derecha\n\t\t\t2)Ingresar por izquierda \t"))
        if opcion == 1:
            cola.add(input("Ingresar elemento: "),1)
        else:
            if opcion == 2:
                cola.add(input("Ingresar elemento: "),2)
            else:
                print("Opcion invalida")
    else:
        if opcion == 2:
            opcion = int(input("\t\t\t1)Eliminar por izquierda\n\t\t\t2)Eliminar por derecha\t"))
            if opcion == 1:
                cola.delete(1)
            else:
                cola.delete(2)
        else:
            if opcion != 5:
                print("Ingrese opcion valida")
  
print("Adios.") 
