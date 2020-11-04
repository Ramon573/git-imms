# -*- coding:utf-8 -*-
# La linea superior, nos permite decodificar en el margen de UTF-8 todo nuestro codigo


# Importar flask
import sys
from flask import Flask, render_template, request, session
import models.database_model as datamodel

db = datamodel.database('localhost','root','Adonispili2','imss_035')
app = Flask(__name__)  # Creamos unas instancia de Flask






# Creacion de rutas URLS

# Definimos nuestro pirmer endPoint para nuestra API de python (url raiz)



@app.route("/")
def index():
    titulo = "Pagina Principal"
  
    try: 
        db.connection()
        print ('La conexion es exictosa')
    except:
        print ('Sigue sin jalar esta madre')
    return render_template('login.html', titulo = titulo)
   
    
@app.route("/login", methods =["POST"])
def login():

    if request.method == "POST":
        db.connection()
       
    return('OK')        

        
        

        
        

        
            

         
    
# @app.route("/form")
# def form():
#     titulo = "Login de prueba"
#     return render_template('form.html', titulo=titulo)


# @app.route("/DatosEncuestador", methods =['POST','GET'])
# def DatosEmpleado():
#     #titulo = "DatosEncuestado"
#     if request.method == 'POST':
#         _NombreEncuestador = request.form['NombreEncuestador']
#         _Empresa = request.form['Empresa']
#         _Direccion = request.form['Direccion']
#         _Colonia = request.form['Colonia']
#         _Ciudad = request.form['Ciudad']
#         _Estado = request.form['Estado']
#         _Fax = request.form['Fax']
#         _rfc = request.form['rfc']

#         print(_NombreEncuestador, _Empresa, _Direccion, _Colonia, _Ciudad, _Estado, _Fax, _rfc)
        
        

#     else: 
#         return render_template('DatosEncuestador.html')



# @app.route("/encuesta1P1")
# def encuesta1P1():
#     titulo = "Encuesta1P1"
#     return render_template('encuesta1P1.html', titulo = titulo)


# @app.route("/encuesta1P2")
# def encuesta1P2():
#     titulo = "Encuesta1P2"
#     return render_template('encuesta1P2.html', titulo = titulo)


# @app.route("/encuesta2P1")
# def encuesta2P1():
#     titulo = "Encuesta2P1"
#     return render_template('encuesta2P1.html', titulo = titulo)
    




if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
