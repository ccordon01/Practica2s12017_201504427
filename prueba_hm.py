import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
from nodos import Clasedos
from lista import ClaseLista
from listaPila import ClaseListaPila
test = ClaseLista()
test.insertarAlFrente("hola")
test.insertarAlFrente("adios")
test.insertarAlFinal("hi")
test.insertarAlFinal("ciao")
print"Nodo 1 " + str(test.primerNodo.datos) 
test.mostrar()
test.eliminarDelFrente()
test.mostrar()
test.estaVacia() 
pila = ClaseListaPila()
pila.push("NA")
pila.mostrar()
print "Hola Mundo"
#Claseuno();
#Clasedos();