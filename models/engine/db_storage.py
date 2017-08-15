#!/usr/bin/python3
"""
Database Storage Engine DBStorage
"""
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models import base_model, amenity, city, place, review, state, user


class DBStorage:
    """

    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initialize engine
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                                getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        queries all or selected database objects
        """
        CNC = {
            'BaseModel': base_model.BaseModel,
            'Amenity': amenity.Amenity,
            'City': city.City,
            'Place': place.Place,
            'Review': review.Review,
            'State': state.State,
            'User': user.User
        }
