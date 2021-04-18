class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

    def getProductoHumano(self):
        pass

    def getProductoOrco(self):
        pass

class Arma(Producto):
    
    def __init__(self):
        Producto.__init__(self)

    def getProductoHumano(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "arma de los humanos"
       
    
    def getProductoOrco(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "arma de los orcos"
        

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

    def getProductoHumano(self):
        print("metodo humano de escucdo")
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "escudo de los humanos"
    
    def getProductoOrco(self):
        print("metodo orco de escucdo")
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "escudo de los orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)
    
    def getProductoHumano(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "montura de los humanos"
    
    def getProductoOrco(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.png"
        self.descripcion = "Montura de los orcos"

class Cuerpo(Producto):
    def __init__(self):
        Producto.__init__(self)

    def getProductoHumano(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/cuerpo.png"
        self.descripcion = "Cuerpo de los humanos"
    
    def getProductoOrco(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/cuerpo.png"
        self.descripcion = "Montura de los orcos"
        




