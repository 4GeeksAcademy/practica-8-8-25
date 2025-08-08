from flask import Blueprint, jsonify, request
from Models.animal_model import Animals

animal_bp = Blueprint('animals', __name__, url_prefix='/animals')

animals = []
next_id = 1

@animal_bp.route('/', methods= ['GET'])
def get_animals():
    return jsonify([a.serializer() for a in animals]), 200

@animal_bp.route('/', methods= ['POST'])
def create_animals():
    global next_id
    data = request.get_json()
    
    if not isinstance(data.get('name'), str) or not isinstance(data.get('type'), str) or not isinstance(data.get('age'), int):
        return jsonify({'msg': 'Datos incorrectos'}), 400

    new_animal = Animals(id= next_id, name=data.get('name'), type=data.get('type'), age=data.get('age'))

    animals.append(new_animal)
    next_id += 1
    return jsonify({'msg': 'Animal creado correctamente'}, new_animal.serializer()), 202

@animal_bp.route('/<int:id>', methods= ['GET'])
def show_animal(id):
    for a in animals:
        if id == a.id:
            return jsonify({'msg': 'Animal encontrado'}, a.serializer()), 200
    return jsonify({'msg': 'Animal no encontrado'}), 404

@animal_bp.route('/<int:id>', methods= ['DELETE'])
def delete_animal(id):
    for a in animals:
        if id == a.id:
            animals.remove(a)
            return jsonify({'msg': 'Animal eliminado'}, a.serializer()), 200
    return jsonify({'msg': 'Animal no encontrado'}), 404

@animal_bp.route('/<int:id>', methods= ['PUT'])
def update_animal(id):
    data = request.get_json()

    for a in animals:
        if id == a.id:
            a.name = data.get("name", a.name)
            a.age = data.get("age", a.age)
            a.type = data.get("type", a.type)
            return jsonify({'msg': 'Animal modificado'}, a.serializer()), 200
    return jsonify({'msg': 'Error'})

def find_animal(id):
    return next((a for a in animals if a.id == id), None)