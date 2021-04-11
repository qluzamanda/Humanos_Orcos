# Humanos_Orcos
Ejemplo de Objetos
Ejemplo Realizado para revizar los conceptos del Paradigma de Orientacion a objetos.
En el ejemplo se agregan las monturas y los cuerpos tanto a los humanos como a los Orcos.

Con lo anterios se evidencias los siguientes principios de diseño:

	-Single Responsability: se evidencia ya que cada objeto tiene una sola responsabilidad
		ArmaOrcos
		ArmaHumanos
		EscudoOrco
		EscudoHumano... etc

	-Open/close: Vemos qeu esta abierta a la extension  pudimos agregar mas  productos sin afectar el codigo ya que se uso  el mecanismo de extension.

	-Interface segragation-<  tenemos clases especializada y pequeñas

	-Dependency inversión ->Los modulos de  estan completamente desaclopadas se pueden agregar o quitar elementos  si afectar otros modulos

	-Kiss -> Ene general el codigo es simple  facil de explicar.

Patrones de Diseño Usados:
	Patron Creacional -> 
	Se usa el "Abstract Factory: " ya que hay una interfaz para crear cada  familia de productos.
	tenemos las interfaz  FabricaHumanos()  para  todos los productos de los humanos.
                    y  FabricaOrcos()  para todos los productos de los Orcos.


	PAtron Estructrua -> 
	Se usa  el patron  "Facade"  ya  que tenemos una sola interfaz  producto  para acceder a  cada uno de los diferetes productos  ya sea de Orcos o de humano


	Patron de comportamiento ->
	se usa el patron de "template method"  por qeuu se usa un esquelo para de creacion pero realmente cada subclase es la que define que es lo qeu se debe realziar.
