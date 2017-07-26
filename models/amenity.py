#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String

class Amenity(BaseModel):
    """Amenity class handles all application amenities"""
    """if storage is db"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    """if storage is file"""
    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
