from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
 	 print "Acabas de instanciar la Clase Clasedos"
     print "E instanciando de esta"
     Claseuno()
    return 'Hello World!'

if __name__ == '__main__':
    app.run()