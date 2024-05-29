from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from config.bd import bd
from Models.Cines import Cines, cines_schema, cineses_schema

cines_bp = Blueprint('cines_bp', __name__)

@cines_bp.route('/cines', methods=['POST'])
@jwt_required()
def add_cine():
    nombre = request.json['nombre']
    latitud = request.json['latitud']
    longitud = request.json['longitud']
    resenas = request.json['resenas']
    pelicula_proyectandose = request.json['pelicula_proyectandose']
    horainicio = request.json['horainicio']
    imagen = request.json['imagen']
    horarios = request.json['horarios']
    IdCartelera = request.json['IdCartelera']
    
    new_cine = Cines(nombre, latitud, longitud, resenas, pelicula_proyectandose, horainicio, imagen, horarios, IdCartelera)
    
    bd.session.add(new_cine)
    bd.session.commit()
    
    return cines_schema.jsonify(new_cine)

@cines_bp.route('/cines', methods=['GET'])
@jwt_required()
def get_cines():
    all_cines = Cines.query.all()
    result = cineses_schema.dump(all_cines)
    return jsonify(result)

@cines_bp.route('/cines/<id>', methods=['GET'])
@jwt_required()
def get_cine(id):
    cine = Cines.query.get(id)
    return cines_schema.jsonify(cine)

@cines_bp.route('/cines/<id>', methods=['PUT'])
@jwt_required()
def update_cine(id):
    cine = Cines.query.get(id)
    
    nombre = request.json['nombre']
    latitud = request.json['latitud']
    longitud = request.json['longitud']
    resenas = request.json['resenas']
    pelicula_proyectandose = request.json['pelicula_proyectandose']
    horainicio = request.json['horainicio']
    imagen = request.json['imagen']
    horarios = request.json['horarios']
    IdCartelera = request.json['IdCartelera']
    
    cine.nombre = nombre
    cine.latitud = latitud
    cine.longitud = longitud
    cine.resenas = resenas
    cine.pelicula_proyectandose = pelicula_proyectandose
    cine.horainicio = horainicio
    cine.imagen = imagen
    cine.horarios = horarios
    cine.IdCartelera = IdCartelera
    
    bd.session.commit()
    
    return cines_schema.jsonify(cine)

@cines_bp.route('/cines/<id>', methods=['DELETE'])
@jwt_required()
def delete_cine(id):
    cine = Cines.query.get(id)
    bd.session.delete(cine)
    bd.session.commit()
    
    return cines_schema.jsonify(cine)