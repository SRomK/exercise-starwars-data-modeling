import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(VARCHAR(250), nullable=False)
    lastname = Column(VARCHAR(250), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            
        }

    

class Favorites(Base):
    __tablename__= 'favorites'   

    id = Column(Integer, primary_key=True)
    planetfav_name = Column(String(250))
    characterfav_name = Column(String(250))

    def to_dict(self):
        return {
            "id": self.id,
            "planetfav_name": self.planetfav_name,
            "characterfav_name": self.characterfav_name
        }

class Planets(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    planets_name = Column(String(250))

    def to_dict(self):
        return {
            "id": self.id,
            "planets_name": self.planets_name
        }
    
class Characters(Base):
    __tablename__='characters'

    id = Column(Integer, primary_key=True) 
    characters_name = Column(String(250))

    def to_dict(self):
        return {
            "id": self.id,
            "characters_name": self.characters_name
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
