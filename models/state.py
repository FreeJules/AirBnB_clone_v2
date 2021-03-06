#!/usr/bin/python3
"""
State Class from Models Module
"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import environ, getenv


class State(BaseModel, Base):
    """State class handles all application states"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all")
    else:
        name = ''

        @property
        def cities(self):
            """
                getter method, returns list of City objs from storage
                linked to the current State
            """
            cities_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
