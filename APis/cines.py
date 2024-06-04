from flask import Blueprint, request, jsonify

from config.bd import bd
from Models.Cines import Cines, CinesSchema
from config.routeProtection import token_required
cines_bp = Blueprint('cines_bp', __name__)

cines_schema = CinesSchema()
cineses_schema = CinesSchema(many=True)

@cines_bp.route('/Agregarcines', methods=['POST'])
@token_required()
def add_cine():
    nombre = request.json['nombre']
    latitud = request.json['latitud']
    longitud = request.json['longitud']
    resenas = request.json['resenas']
    pelicula_proyectandose = request.json['pelicula_proyectandose']
    horainicio = request.json['horainicio']
    imagen = request.json['imagen']
    horarios = request.json['horarios']
  
    
    new_cine = Cines(nombre, latitud, longitud, resenas, pelicula_proyectandose, horainicio, imagen, horarios)
    
    bd.session.add(new_cine)
    bd.session.commit()
    
    return "Guarado"

@cines_bp.route('/Obtenercines', methods=['GET'])
@token_required()
def get_cines():
    all_cines = Cines.query.all()
    result = cineses_schema.dump(all_cines)
    return jsonify(result)

@cines_bp.route('/ObtenercineId', methods=['GET'])
@token_required()
def get_cine(id):
    id = request.json['id']
    cine = Cines.query.get(id)
    return cines_schema.jsonify(cine)



@cines_bp.route('/Eliminarcine', methods=['DELETE'])
@token_required()
def delete_cine(id):
    id = request.json['id']
    cine = Cines.query.get(id)
    bd.session.delete(cine)
    bd.session.commit()
    
    return cines_schema.jsonify(cines_schema.dump(cine))