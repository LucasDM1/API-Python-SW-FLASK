from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, url_for

db = SQLAlchemy()

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    username=db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username":self.username,
            # do not serialize the password, its a security breach
        }
    
    def getAllusers():
        users_query = User.query.all()
        all_users = list(map(lambda x: x.serialize(), users_query))
        return(all_users)
    
    def create_user(request_body_user):
        user1 = User(name=request_body_user["name"], lastname=request_body_user["lastname"], username=request_body_user["username"], email=request_body_user["email"], password=request_body_user["password"])
        db.session.add(user1)
        db.session.commit()
        return("An user has been added")

class Character(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    gender=db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    eye_color=db.Column(db.String(250), nullable=False)
    hair_color=db.Column(db.String(250), nullable=False)

    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    
    def getAllcharacters():
        characters_query = Character.query.all()
        all_characters = list(map(lambda x: x.serialize(), characters_query))
        return(all_characters)

    def create_character(request_body_char):
        char1 = Character(name=request_body_char["name"], birth_year=request_body_char["birth_year"], gender=request_body_char["gender"], height=request_body_char["height"], eye_color=request_body_char["eye_color"], hair_color=request_body_char["hair_color"])
        db.session.add(char1)
        db.session.commit()
        return("A character has been added")
    
    