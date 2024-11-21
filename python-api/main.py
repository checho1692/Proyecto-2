from  flask import Flask, jsonify, request, render_template,redirect,url_for
import pymysql
import datetime

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    port = 3306,
    database = 'personas'
)
servidor='/enviar'
users = {'admin@': '12345'}
cursor = connection.cursor()

app = Flask(__name__)

@app.route('/')
def home():
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
        # return render_template('codigo.html', codigo=codigo)
        
        # return render_template('codigo.html', codigo=codigo,fecha=fecha,servidor=servidor,name=name)
        return redirect('/personas')
    else:
        return '<script>alert("Credenciales incorrectas");</script>'+ render_template('login.html')
    
@app.route('/agregar_empleado')
def agregar_empleado():
    fecha= datetime.datetime.now()
    return render_template('agregar_empleado.html',fecha=fecha) 
   
@app.route('/personas', methods = ["GET"])
def get_personas():
    sql = "SELECT * FROM personas"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    # return jsonify(result)
    return render_template('codigo.html', empleados=result)

@app.route('/persona', methods = ["POST"])
def get_persona():
    id_persona = request.form['id_persona']
    sql = "SELECT * FROM personas WHERE id = " + str(id_persona)
    cursor.execute(sql)
    result = cursor.fetchone()
    
    return render_template('editar_empleado.html', empleados=result)

@app.route('/personasin', methods = ["POST"])
def create_persona():
    datos = request.get_json()
    nombre = datos['nombre']
    correo = datos['correo']
    fecha = datos['fecha']
    try:
        sql = f"INSERT INTO personas (id,nombre, correo,fecha) VALUES (NULL,'{nombre}', '{correo}','{fecha}')"
        cursor.execute(sql)
        connection.commit()
        
        return jsonify({
            "status": 1,
            "respond": "Persona creada correctamente"
        })
    except Exception as e:
        return jsonify({
            "status": 0,
            "respond": "Ha ocurrido un error al insertar el registro"
        })
        
@app.route('/personasedit', methods = ["POST"])
def edit_persona():
    id_persona = request.form['id_persona']
    nombre = request.form['nombre']
    correo = request.form['correo']
    fecha = request.form['fecha']
    try:
        sql = f"UPDATE personas SET nombre = '{nombre}', correo = '{correo}', fecha = '{fecha}' WHERE id = {id_persona}"
        cursor.execute(sql)
        connection.commit()
        
        return redirect('/personas')
    except Exception as e:
        return '<script>alert("Persona editada error");</script>'

@app.route('/personas/<id_persona>', methods = ["DELETE"])
def delete_persona(id_persona):
    try:
        sql = f"DELETE FROM personas WHERE _id = {id_persona}"
        cursor.execute(sql)
        connection.commit()
        
        return jsonify({
            "status": 1,
            "respond": "Persona eliminada correctamente"
        })
    except Exception as e:
        return jsonify({
            "status": 0,
            "respond": "Ha ocurrido un error al eliminar el registro"
        })
    
# Ruta para agregar empleado
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        fecha = request.form['fecha']
        cursor.execute("""
            INSERT INTO personas (id,nombre, correo,fecha) VALUES (NULL,%s, %s, %s)
        """, (nombre, correo, fecha))
        
       
        
  
        
        return redirect('/personas')
    
    return render_template('agregar_empleado.html')  
      
@app.route('/eliminar/<int:id>', methods=['GET', 'POST'] )
def eliminar_empleado(id):
   
    cursor.execute("DELETE FROM personas WHERE id = %s", (id,))
    
   
    
    return redirect('/personas')    


@app.route('/consulta', methods = ["POST",'GET' ])
def get_consulta():
    datos = request.get_json()
    nombre = datos['nombre']
    
    sql = f"SELECT * FROM personas WHERE nombre ='{nombre}'" 
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return jsonify(result)
    # return jsonify({
    #         "status": 1,
    #         "respond": "Persona creada correctamente",
    #         "datos": result
    #     })

if __name__ == '__main__':
    app.run(debug = True, port=5001)