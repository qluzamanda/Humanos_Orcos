class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "arma de los humanos"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "arma de los orcos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "escudo de los humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "escudo de los orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.png"
        self.descripcion = "Montura de los orcos"

class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "montura de los humanos"

class Cuerpo(Producto):
    def __init__(self):
        Producto.__init__(self)

class CuerpoOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/cuerpo.png"
        self.descripcion = "Cuerpo de los orcos"

class CuerpoHumanos(Cuerpo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/cuerpo.png"
        self.descripcion = "Cuerpo de los humanos"

