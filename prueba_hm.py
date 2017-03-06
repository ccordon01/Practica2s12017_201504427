import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
from nodos import Claseuno
from nodos import Clasedos
from lista import ClaseLista
from lista import ClaseListaDoble
from listaPila import ClaseListaPila
from listaCola import ClaseListaCola
from matrizDispersa import ClassMatriz
test = ClaseLista()
test.insertarAlFrente("hola")
test.insertarAlFrente("adios")
test.insertarAlFinal("hi")
test.insertarAlFinal("ciao")
test.mostrar()
print"Nodo 1 " + str(test.primerNodo.datos) 
test.eliminarDelFrente()
test.mostrar()
test.estaVacia() 
test2 = ClaseListaDoble()
test2.insertarAlFrente("hola")
test2.insertarAlFrente("adios")
test2.insertarAlFrente("hi")
test2.insertarAlFinal("ciao")
print test2.byvalue(str("hola"))
print"Nodo ultimo " + str(test2.ultimoNodo.datos) 
print"Nodo ultimo anterior " + str(test2.ultimoNodo.nodoAnterior.datos) 
print "size: " + str(test2.size())
test2.mostrar()
#print "Se elimino "+ str(test2.delbyvalue("hola"))
test2.mostrar()
print "--Prueba Pila--"
pila = ClaseListaPila()
pila.push("1")
pila.push("2")
pila.push("3")
pila.push("4")
pila.push("5")
pila.mostrar()
print "--Prueba Cola--"
cola = ClaseListaCola()
cola.enqueue("1")
cola.enqueue("2")
cola.enqueue("3")
cola.enqueue("4")
cola.enqueue("5")
cola.mostrar()
print "--Matriz Dispersa--Cabecera--"
matriz = ClassMatriz()
print matriz.insertarCabeceraLetras("c")
print matriz.insertarCabeceraLetras("a")
print matriz.insertarCabeceraLetras("b")
print matriz.insertarCabeceraLetras("d")
print matriz.insertarCabeceraLetras("d")
print matriz.insertarCabeceraLetras("x")
print "--Inicio Cabecera Letras--"
matriz.mostrarCabeceraLetras()
print "--Matriz Dispersa--Dominios--"
#print matriz.insertarCabeceraDominios("car.com")
#print matriz.insertarCabeceraDominios("all.com")
#print matriz.insertarCabeceraDominios("bee.com")
print matriz.insertarCabeceraDominios("dzi.com")
print matriz.insertarCabeceraDominios("dll.com")
print matriz.insertarCabeceraDominios("dla.com")
print matriz.insertarCabeceraDominios("dli.com")
print matriz.insertarCabeceraDominios("dl.com")
#print matriz.insertarCabeceraDominios("xfg.com")
print "--Inicio Cabecera Dominios--"
matriz.mostrarCabeceraDominios()
print "--Inicio Matriz Dispersa--"
matrizD = ClassMatriz()
print matrizD.insertarCorreo("carlos","gmail")
print matrizD.insertarCorreo("carlos","hotmail")
print matrizD.insertarCorreo("diego","hotmail")
print matrizD.insertarDatos("carlos","gmail")
print matrizD.insertarDatos("carlos","hotmail")
print matrizD.insertarDatos("diego","hotmail")
print "--Inicio Cabecera Letras--"
matrizD.mostrarCabeceraLetras()
print "--Inicio Cabecera Dominios--"
matrizD.mostrarCabeceraDominios()
print "--Inicio Cabecera Letras--"
print matrizD.findbyl("c")
print "--Inicio Cabecera Dominios--"
print matrizD.findbyd("hotmail")
print matrizD.borrarDatos("carlos","hotmail")
print "--Inicio Cabecera Letras--"
print matrizD.findbyl("c")
print "--Inicio Cabecera Dominios--"
print matrizD.findbyd("hotmail")
#print "Hola Mundo"
#hi= "hi"
#print hi[1]
#print len(hi)
#print len(".")
#Claseuno();
#Clasedos();