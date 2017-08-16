#!/usr/bin/python3
"""
Database Storage Engine DBStorage
"""
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.state import State
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """
    class DBStorage
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

        CNC = {
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User
        }

    def all(self, cls=None):
        """
        queries all or selected database objects
        """
        dbd = {}
        if cls:
            for item in self.__session.query(cls).all():
                dbd[item.id] = item
        return (dbd)

    def new(self, obj):
        """
        add new object to the current database session
        self.__session.add(obj)
        """
        pass

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
