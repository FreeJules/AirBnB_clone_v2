#!/usr/bin/python3
"""
User Class from Models Module
"""
from sqlalchemy import Column, String
from models.base_model import BaseModel


class User(BaseModel):
    """User class handles all application users"""
    """if storage is db"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    """if storage is file"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
