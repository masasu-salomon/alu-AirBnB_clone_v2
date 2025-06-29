#!/usr/bin/python3
"""Database storage engine for MySQL"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os


class DBStorage:
    """Manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage with MySQL connection"""
        user = os.getenv('HBNB_MYSQL_USER', 'hbnb_test')
        pwd = os.getenv('HBNB_MYSQL_PWD', 'hbnb_test_pwd')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB', 'hbnb_test_db')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a class or all classes"""
        classes = [User, State, City, Place, Review, Amenity]
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add object to current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes in current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and initialize session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session"""
        self.__session.remove()
