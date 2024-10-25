import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)

    favorites = relationship('Favorite', backref='user', lazy=True)

    def to_dit(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "subscription_date": self.subscription_date
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    birth_year = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    homeworld = Column(String(250), nullable=True)

    favorites = relationship('Favorite', backref='character', lazy=True)

    def to_dit(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=True)
    rotation_period = Column(String(250), nullable=True)
    orbital_period = Column(String(250), nullable=True)
    gravity = Column(String(250), nullable=True)
    population = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)

    favorites = relationship('Favorite', backref='planet', lazy=True)

    def to_dit(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain
        }

class Starship(db.Model):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    starship_class = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(String(250), nullable=True)
    length = Column(String(250), nullable=True)
    crew = Column(String(250), nullable=True)
    passengers = Column(String(250), nullable=True)
    max_atmosphering_speed = Column(String(250), nullable=True)
    hyperdrive_rating = Column(String(250), nullable=True)
    MGLT = Column(String(250), nullable=True)
    cargo_capacity = Column(String(250), nullable=True)
    consumables = Column(String(250), nullable=True)

    favorites = relationship('Favorite', backref='starship', lazy=True)

    def to_dit(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=True)

    def to_dit(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "starship_id": self.starship_id
        }
