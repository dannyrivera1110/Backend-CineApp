from flask import Blueprint, request, jsonify
from config.bd import bd
from Models.User import Usuario, UsuarioSchema 
from config.Token import generate_token
from config.routeProtection import token_required

usuario_bp = Blueprint('usuario_bp', __name__)


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


@usuario_bp.route('/registerU', methods=['POST'])
def register(): 
    apellido = request.json['apellido']
    telefono = request.json['telefono']
    nombre = request.json['nombre']
    direccion = request.json['direccion']
    correo = request.json['correo']
    contrasena = request.json['contrasena']  
    new_usuario = Usuario(apellido, telefono, nombre, direccion, correo, contrasena)  
    bd.session.add(new_usuario)
    bd.session.commit()  
    return "Guardado"


@usuario_bp.route('/login', methods=['POST'])
def login():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    if not correo or not contrasena:
        return jsonify({"message": "correo y contrasena son requeridos"}), 400
    
    usuario = Usuario.query.filter_by(correo=correo).first()
    if not usuario:
        return jsonify({"message": " Username or password Invalido"}), 401
    

    if usuario.contrasena!=contrasena:
         return jsonify({"message": "Password Invalido"}), 401
    
    # Generar token JWT
    token = generate_token(usuario.id, usuario.correo)
   


@usuario_bp.route('/Obtenerusuarios', methods=['GET'])
@token_required
def get_usuarios():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)
    return jsonify(result)