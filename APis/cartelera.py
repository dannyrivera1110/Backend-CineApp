from flask import Blueprint, request, jsonify
from config.bd import bd
from Models.Cartelera import CarteleraSchema, Cartelera

cartelera_bp = Blueprint('cartelera_bp', __name__)

cartelera_schema = CarteleraSchema()
carteleras_schema = CarteleraSchema(many=True)  


@cartelera_bp.route('/Agregarcartelera', methods=['POST'])
def add_cartelera():
    title = request.json['title']
    director = request.json['director']
    imageUrl = request.json['imageUrl']
    description = request.json['description']
    horario = request.json['horario']
    categories = request.json['categories']
    isFavorite = request.json['isFavorite']
    review = request.json['review']
    IdCines = request.json['IdCines']
    
    new_cartelera = Cartelera(title, director, imageUrl, description, horario, categories, isFavorite, review,IdCines)
    
    bd.session.add(new_cartelera)
    bd.session.commit()
    
    return "Guardado"

@cartelera_bp.route('/Obtenercarteleras', methods=['GET'])
def get_carteleras():
    all_carteleras = Cartelera.query.all()
    result = carteleras_schema.dump(all_carteleras)
    return jsonify(result)

@cartelera_bp.route('/ObtenercarteleraId', methods=['GET'])
def get_cartelera(id):
    id = request.json['id']
    cartelera = Cartelera.query.get(id)
    return cartelera_schema.jsonify(cartelera)


@cartelera_bp.route('/Eliminarcartelera', methods=['DELETE'])
def delete_cartelera(id):
    id = request.json['id']
    cartelera = Cartelera.query.get(id)
    bd.session.delete(cartelera)
    bd.session.commit()
    
    return jsonify(cartelera_schema.dump(cartelera))