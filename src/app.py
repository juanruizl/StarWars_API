"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Starship, Favorite

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET', 'POST'])
def handle_user():
    if request.method == 'GET':
        users = [user.to_dit() for user in User.query.all()]
        return jsonify(users), 200
    elif request.method == 'POST':
        data = request.get_json()
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dit()), 201

@app.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
def modify_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    if request.method == 'GET':
        return jsonify(user.to_dit()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(user.to_dit()), 200
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "User deleted"}), 204

@app.route('/character', methods=['GET', 'POST'])
def handle_character():
    if request.method == 'GET':
        characters = [character.to_dit() for character in Character.query.all()]
        return jsonify(characters), 200
    elif request.method == 'POST':
        data = request.get_json()
        new_character = Character(**data)
        db.session.add(new_character)
        db.session.commit()
        return jsonify(new_character.to_dit()), 201

@app.route("/character/<int:id>", methods=["PUT", "DELETE"])
def modify_character(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({"msg": "Character not found"}), 404
    if request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(character, key, value)
        db.session.commit()
        return jsonify(character.to_dit()), 200
    elif request.method == 'DELETE':
        db.session.delete(character)
        db.session.commit()
        return jsonify({"msg": "Character deleted"}), 204

@app.route('/planet', methods=['GET', 'POST'])
def handle_planet():
    if request.method == 'GET':
        planets = [planet.to_dit() for planet in Planet.query.all()]
        return jsonify(planets), 200
    elif request.method == 'POST':
        data = request.get_json()
        new_planet = Planet(**data)
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(new_planet.to_dit()), 201

@app.route("/planet/<int:id>", methods=["PUT", "DELETE"])
def modify_planet(id):
    planet = Planet.query.get(id)
    if not planet:
        return jsonify({"msg": "Planet not found"}), 404
    if request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(planet, key, value)
        db.session.commit()
        return jsonify(planet.to_dit()), 200
    elif request.method == 'DELETE':
        db.session.delete(planet)
        db.session.commit()
        return jsonify({"msg": "Planet deleted"}), 204

@app.route('/starship', methods=['GET', 'POST'])
def handle_starship():
    if request.method == 'GET':
        starships = [starship.to_dit() for starship in Starship.query.all()]
        return jsonify(starships), 200
    elif request.method == 'POST':
        data = request.get_json()
        new_starship = Starship(**data)
        db.session.add(new_starship)
        db.session.commit()
        return jsonify(new_starship.to_dit()), 201

@app.route("/starship/<int:id>", methods=["PUT", "DELETE"])
def modify_starship(id):
    starship = Starship.query.get(id)
    if not starship:
        return jsonify({"msg": "Starship not found"}), 404
    if request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(starship, key, value)
        db.session.commit()
        return jsonify(starship.to_dit()), 200
    elif request.method == 'DELETE':
        db.session.delete(starship)
        db.session.commit()
        return jsonify({"msg": "Starship deleted"}), 204

@app.route('/user/<int:id>/favorites', methods=['GET'])
def get_favorites(id):
    favorites = Favorite.query.filter_by(user_id=id).all()
    return jsonify([favorite.to_dit() for favorite in favorites]), 200

@app.route('/favorite', methods=['POST'])
def add_favorite():
    data = request.get_json()
    favorite = Favorite(**data)
    db.session.add(favorite)
    db.session.commit()
    return jsonify(favorite.to_dit()), 201

@app.route('/favorite/<int:id>', methods=['DELETE'])
def delete_favorite(id):
    favorite = Favorite.query.get(id)
    if not favorite:
        return jsonify({"msg": "Favorite not found"}), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg": "Favorite deleted"}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
