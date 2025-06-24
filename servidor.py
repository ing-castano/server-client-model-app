from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas_pfo2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)

# Ruta: Registro
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = generate_password_hash(datos.get('contraseña'))

    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({'mensaje': 'Usuario ya existe'}), 400

    nuevo_usuario = Usuario(usuario=usuario, contrasena=contrasena)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario registrado con éxito'})

# Ruta: Login
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    usuario_encontrado = Usuario.query.filter_by(usuario=usuario).first()

    if usuario_encontrado and check_password_hash(usuario_encontrado.contrasena, contrasena):
        return jsonify({'mensaje': 'Login exitoso'})
    else:
        return jsonify({'mensaje': 'Credenciales incorrectas'}), 401

# Ruta: Tareas
@app.route('/tareas', methods=['GET'])
def tareas():
    return '''
    <html>
      <body>
        <h1>Bienvenido al sistema de gestión de tareas</h1>
      </body>
    </html>
    '''

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)
