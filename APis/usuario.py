from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from werkzeug.security import check_password_hash
from config.bd import bd
from Models.User import Usuario, usuario_schema, usuarios_schema 

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios/register', methods=['POST'])
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

@usuario_bp.route('/usuarios/login', methods=['POST'])
def login():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    
    usuario = Usuario.query.filter_by(correo=correo).first()
    
    if usuario and check_password_hash(usuario.contrasena, contrasena):
        access_token = create_access_token(identity={'id': usuario.id, 'correo': usuario.correo})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Correo o contraseña incorrectos"}), 401

@usuario_bp.route('/usuarios', methods=['GET'])
@jwt_required()
def get_usuarios():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)
    return jsonify(result)