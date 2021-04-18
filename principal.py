from flask import Flask, render_template
from fabricas import *
from random import choice
from productos import *

app = Flask(__name__)


@app.route('/')
def principal():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma= fabrica.crear_producto(Arma())
    escudo = fabrica.crear_producto(Escudo())
    montura= fabrica.crear_producto(Montura())
    cuerpo= fabrica.crear_producto(Cuerpo())

    productos = []

    productos.append(arma)
    productos.append(escudo)
    productos.append(montura)
    productos.append(cuerpo)

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)
