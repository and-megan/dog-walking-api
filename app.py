import json
from flask import Flask, jsonify, make_response, abort, request


app = Flask(__name__)


@app.route('/dogs', methods=['GET'])
def get_dogs():
    return jsonify(dogs_objs)

@app.route('/dogs/<int:dog_id>')
def get_dog(dog_id):
    for dog in dogs_objs:
        if dog['id'] == dog_id:
            return jsonify(dog)

    abort(404)

@app.route('/dogs', methods=['POST'])
def create_dog():
    data = json.loads(request.data)
    import pdb;pdb.set_trace()
    if not data or not _validate_dog(data):
        abort(400)
    dog_id = _get_dog_id()
    dog = {
        'id':dog_id,
        'name': data['name'],
        'credit': 100,
        'rating': 5.0,
        'color': data['color'],
        'age': data['age']
    }
    dogs_objs.append(dogs_objs)

    return jsonify({'dog': dog}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def _validate_dog(data):
    return data.keys().sort() == ['name', 'color', 'age'].sort()

def _get_dog_id():
    num = 0
    for dog in dogs_objs:
        if dog['id'] > num:
            num = dog['id']

    return num + 1


dogs_objs = [
    {
        "id": 1,
        "name": "Dusty",
        "credit": 100,
        "rating": 4.9,
        "color": "tricolor",
        "age": 13
    },
    {
        "id": 2,
        "name": "Alfie",
        "credit": 75,
        "rating": 4.4,
        "color": "white",
        "age": 6
    },
    {
        "id": 3,
        "name": "Sofie",
        "credit": 50,
        "rating": 4.2,
        "color": "brown",
        "age": 10
    },
    {
        "id": 4,
        "name": "Maggie",
        "credit": 80,
        "rating": 3.9,
        "color": "black",
        "age": 2
    },
    {
        "id": 5,
        "name": "Shadow",
        "credit": 15,
        "rating": 4.6,
        "color": "grey",
        "age": 5
    },
]
