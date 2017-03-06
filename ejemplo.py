__author__ = "Mac"

#Si mientras trabajan en Python alguna vez les arroja un "IndentationError" es porque en alguna linea, los tabs al inicio de la sentencia estan erroneos, por ejemplo:
#Esto es valido:
#class Usuario():
#    def __init__(self, nombre):
#        self.nombre = nombre
#        self.password = password
#Esto NO es valido y arroja un "IndentationError":
#class Usuario():
#    def __init__(self, nombre):
#        self.nombre = nombre
#       self.password = password
#       ^
#       Esto no deberia de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#


import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./')
#Importo la Clase
#from nodos import Claseuno
from flask import Flask, request, Response
from nodos import Claseuno
from nodos import Clasedos
from lista import ClaseLista
from lista import ClaseListaDoble
from listaPila import ClaseListaPila
from listaCola import ClaseListaCola
from matrizDispersa import ClassMatriz
app = Flask("Practica 2")
lista = ClaseListaDoble()
pila = ClaseListaPila()
cola = ClaseListaCola()
matriz = ClassMatriz()
#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class Usuario():
    def __init__(self, password, correo, nombre):
        self.nombre = nombre
        self.password = password
        self.correo = correo
        self.lista = ClaseListaDoble()
        self.pila = ClaseListaPila()
        self.cola = ClaseListaCola()
        self.matriz = ClassMatriz()
@app.route('/prueba',methods=['POST']) 
def h1i():
    #return "hola"
    parametro = str(request.form['dato'])
    ##self.lista.insertarAlFinal(parametro);
    return "Se inicio correctamente " + str(parametro) + "!"
@app.route('/insertarLista',methods=['POST']) 
def h1():
    parametro = str(request.form['dato'])
    lista.insertarAlFinal(str(parametro));
    return "Se inserto correctamente " + str(parametro) + "!"
@app.route('/borrarLista',methods=['POST']) 
def h11():
    parametro = str(request.form['dato'])
    print "borrar "+parametro
    lista.mostrar()
    valor = lista.delbypos(parametro)
    if valor is "null":
        return "No se encontro dato"
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/buscarLista',methods=['POST']) 
def h111():
    parametro = str(request.form['dato'])
    valor = lista.byvalue(parametro)
    if valor == "null":
        return "No se encontro dato"
    return "Se encontro correctamente en pos: " + str(valor) + "!"
@app.route('/insertarMatriz',methods=['POST']) 
def h14():
    parametro = str(request.form['dato'])
    dato = str(request.form['dato2'])
    print matriz.insertarCorreo(parametro,dato)
    print matriz.insertarDatos(parametro,dato)
    return "Se inserto correctamente " + str(parametro) +"@"+ str(dato)+ "!"
@app.route('/borrarMatriz',methods=['POST']) 
def h114():
    parametro = str(request.form['dato'])
    print "borrar "+parametro
    parametro = str(request.form['dato'])
    dato = str(request.form['dato2'])
    valor = matriz.borrarDatos(parametro,dato)
    if valor is "null":
        return "No se encontro dato"
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/buscarMatrizL',methods=['POST']) 
def h1114():
    parametro = str(request.form['dato'])
    valor = matriz.findbyl(str(parametro))
    if valor == "null":
        return "No se encontro dato"
    return str(valor)
@app.route('/buscarMatrizD',methods=['POST']) 
def h11145():
    parametro = str(request.form['dato'])
    valor = matriz.findbyd(str(parametro))
    if valor == "null":
        return "No se encontro dato"
    return str(valor)
@app.route('/insertarPila',methods=['POST']) 
def h12():
    parametro = str(request.form['dato'])
    pila.push(parametro);
    return "Se inserto correctamente " + str(parametro) + "!"
@app.route('/borrarPila',methods=['POST']) 
def h112():
    #parametro = str(request.form['dato'])
    valor = pila.pop()
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/insertarCola',methods=['POST']) 
def h13():
    parametro = str(request.form['dato'])
    cola.enqueue(parametro);
    return "Se inserto correctamente " + str(parametro) + "!"
@app.route('/borrarCola',methods=['POST']) 
def h113():
    #parametro = str(request.form['dato'])
    valor = cola.dequeue()
    return "Se elimino correctamente " + str(valor) + "!"
@app.route('/metodoWeb',methods=['POST']) 
def hello():
    parametro = str(request.form['dato'])
    dato2 = str(request.form['dato2'])
    return "Hola " + str(parametro) + "!"
@app.route('/metodoWeb1',methods=['POST']) 
def helloq():
    return "Hola mundo !"

@app.route("/e")
def hellof():
    return "Hello World2!"
def function():
    pass
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

#################################/
#                               #/
#   Carlos Eduardo Cordon Hdez  #/
#                               #/
#          201504427            #/
#                               #/
#################################/