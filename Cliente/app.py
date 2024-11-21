from flask import Flask, render_template, request, jsonify, json
import datetime

import requests


app = Flask(__name__)
# Datos de ejemplo de usuarios
users = {'empleado@atlas.com': 'password123', 'admin@': '12345'}
servidor='/enviar'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
  
    if username in users and users[username] == password:
        # return 'Inicio de sesión exitoso'
        # codigo = '12345'  # Código de ejemplo
        codigo = username
        fecha= datetime.datetime.now()
        
        if username=='empleado@atlas.com':
            name='John Doe'
        else:
            name=username
            codigo='admin@admin.com'
        
        url = 'http://127.0.0.1:5001/consulta'  # Reemplaza con la URL de tu servicio RESTful
        datos = {'nombre': name}  # Los datos que quieres enviar
        # return datos 
        response = requests.post(url, json=datos)
        
        if response.status_code == 200:
            fecha=datetime.datetime.now()
            # repuesta=response.status_code
            repuesta = response.json()
            # response.append(repuesta)
            print('Datos enviados correctamente')
            return '<script>alert("Datos enviados correctamente");</script>' + render_template('codigo.html', codigo=codigo,fecha=fecha,servidor=servidor,name=name,empleados=repuesta)
            # return jsonify(repuesta)
        else:
            print('Error al enviar los datos')
            return '<script>alert("Datos enviados incorrectamente");</script>'    
            # return render_template('codigo.html', codigo=codigo)
        # return render_template('codigo.html', codigo=codigo,fecha=fecha,servidor=servidor,name=name)
    else:
        return '<script>alert("Credenciales incorrectas");</script>'+ render_template('login.html')


@app.route('/enviar', methods=['POST'])
def enviar_datos():
    nombre = request.form['nombre']
    correo = request.form['correo']
    fecha = request.form['fecha']
    url = 'http://127.0.0.1:5001/personasin'  # Reemplaza con la URL de tu servicio RESTful
    datos = {'nombre': nombre, 'correo': correo, 'fecha': fecha}  # Los datos que quieres enviar
    # return datos 
    response = requests.post(url, json=datos)
    
    if response.status_code == 200:
        fecha=datetime.datetime.now()
        print('Datos enviados correctamente')
        url = 'http://127.0.0.1:5001/consulta'  # Reemplaza con la URL de tu servicio RESTful
        datos = {'nombre': nombre}
        response = requests.post(url, json=datos)
        repuesta = response.json()
        return '<script>alert("Datos enviados correctamente");</script>' + render_template('codigo.html', codigo=correo,fecha=fecha,servidor=servidor,name=nombre,empleados=repuesta)
    else:
        print('Error al enviar los datos')
        return '<script>alert("Datos enviados incorrectamente");</script>'
    

@app.route('/enviar1', methods=['POST'])
def enviar_datos2():
    nombre2 = request.form['nombre']
    # correo = 'b'
    # fecha = 'c'
    # url = 'http://127.0.0.1:5001/personasin'  # Reemplaza con la URL de tu servicio RESTful
    # datos = {'nombre': nombre, 'correo': correo, 'fecha':  fecha}  # Los datos que quieres enviar
    return nombre2 
    # response = requests.post(url, json=datos)
    
    # if response.status_code == 200:
    #     print('Datos enviados correctamente')
    #     return '<script>alert("Datos enviados correctamente");</script>'
    # else:
    #     print('Error al enviar los datos')
    #     return '<script>alert("Datos enviados incorrectamente");</script>'

if __name__ == '__main__':
    app.run(debug=True)       
