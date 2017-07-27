#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import *


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    """if storage is db"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary="place_amenity",
                                   backref=backref('amenities'))
    """if storage is file"""
    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
