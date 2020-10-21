# -*- coding:utf-8 -*-
# La linea superior, nos permite decodificar en el margen de UTF-8 todo nuestro codigo


# Importar flask
from flask import Flask, render_template, request

app = Flask(__name__)  # Creamos unas instancia de Flask

# Creacion de rutas URLS


def checkLogin(name, password):
    if name == "admin" and password == "123":
        return "El usuario es correcto"
    else:
        return "Los datos del usuario son incorrectos"


# Definimos nuestro pirmer endPoint para nuestra API de python (url raiz)
@app.route("/")
def index():

    titulo = "Proyecto de prueba"
    return render_template('Index.html', titulo=titulo)


@app.route("/form")
def form():
    titulo = "Login de prueba"
    return render_template('form.html', titulo=titulo)


@app.route("/login", methods= ['POST', 'GET'])
def login():
    # If user == "admin"
    # If pass == "123456" 
    # Recibir el tipo de metodo -> request.method
    #titulo = "Login"
    if request.method == 'POST':
        # _userData : {
        #     user:request.form['user'],
        #     password:request.form['pass']
        # }
        # base de datos: 
        # Select * from users where user =  _user
        # si existe, seguimos, sino, mandamos un error diciendo que no existe
        # password == _pass --> Simón, estas autorizado. Return render_template('home.html')

        _user = request.form['user']
        _pass = request.form['pass']
        print(_user, _pass)
        # If usuario == "admin" -> Correct
        # if password == "123" --> Correct
        # return index.html, usuario 
        # Bienvenido {{ usuario }}
       
        try:
            result = checkLogin(_user, _pass)   
            print(result)      
            return render_template('index.html', user = _user)
        except:

            return "Algo sucedio durante el login"
    else:
        return render_template("login.html")
            
        
            

        
    
    
    
    


@app.route("/DatosEncuestador")
def DatosEmpleado():
    titulo = "DatosEncuestado"
    return render_template('DatosEncuestador.html', titulo=titulo)



@app.route("/encuesta1P1")
def encuesta1P1():
    titulo = "Encuesta1P1"
    return render_template('encuesta1P1.html', titulo = titulo)


@app.route("/encuesta1P2")
def encuesta1P2():
    titulo = "Encuesta1P2"
    return render_template('encuesta1P2.html', titulo = titulo)


@app.route("/encuesta2P1")
def encuesta2P1():
    titulo = "Encuesta2P1"
    return render_template('encuesta2P1.html', titulo = titulo)
    




if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
