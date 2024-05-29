from flask import Blueprint, request, jsonify
from config.bd import bd
from Models.Cartelera import Cartelera, cartelera_schema, carteleras_schema

cartelera_bp = Blueprint('cartelera_bp', __name__)

@cartelera_bp.route('/cartelera', methods=['POST'])
def add_cartelera():
    title = request.json['title']
    director = request.json['director']
    imageUrl = request.json['imageUrl']
    description = request.json['description']
    horario = request.json['horario']
    categories = request.json['categories']
    isFavorite = request.json['isFavorite']
    review = request.json['review']
    
    new_cartelera = Cartelera(title, director, imageUrl, description, horario, categories, isFavorite, review)
    
    bd.session.add(new_cartelera)
    bd.session.commit()
    
    return "Guardado"

@cartelera_bp.route('/cartelera', methods=['GET'])
def get_carteleras():
    all_carteleras = Cartelera.query.all()
    result = carteleras_schema.dump(all_carteleras)
    return jsonify(result)

@cartelera_bp.route('/cartelera/<id>', methods=['GET'])
def get_cartelera(id):
    cartelera = Cartelera.query.get(id)
    return cartelera_schema.jsonify(cartelera)

@cartelera_bp.route('/cartelera/<id>', methods=['PUT'])
def update_cartelera(id):
    cartelera = Cartelera.query.get(id)
    
    title = request.json['title']
    director = request.json['director']
    imageUrl = request.json['imageUrl']
    description = request.json['description']
    horario = request.json['horario']
    categories = request.json['categories']
    isFavorite = request.json['isFavorite']
    review = request.json['review']
    
    cartelera.title = title
    cartelera.director = director
    cartelera.imageUrl = imageUrl
    cartelera.description = description
    cartelera.horario = horario
    cartelera.categories = categories
    cartelera.isFavorite = isFavorite
    cartelera.review = review
    
    bd.session.commit()
    
    return cartelera_schema.jsonify(cartelera)

@cartelera_bp.route('/cartelera/<id>', methods=['DELETE'])
def delete_cartelera(id):
    cartelera = Cartelera.query.get(id)
    bd.session.delete(cartelera)
    bd.session.commit()
    
    return jsonify(cartelera_schema.dump(cartelera))