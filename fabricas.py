from productos import *

class Fabrica:
    def crear_producto(self):
        pass



class FabricaHumanos(Fabrica):
    def crear_producto(self,producto):
        producto.getProductoHumano()
        return producto

   

class FabricaOrcos(Fabrica):
    def crear_producto(self,producto):
        producto.getProductoOrco()      
        return producto

    