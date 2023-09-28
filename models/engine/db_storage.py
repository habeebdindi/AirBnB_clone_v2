#!/usr/bin/python3
"""DB storage
"""
import os
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime
from models.city import City


class DBStorage:
    """new engine for db storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization
        """
        self.user = os.environ.get('HBNB_MYSQL_USER')
        self.pwd = os.environ.get('HBNB_MYSQL_PWD')
        self.host = os.environ.get('HBNB_MYSQL_HOST')
        self.db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            self.user, self.pwd, self.host, self.db), pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            self.__engine.dispose()
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
           all objects depending of the class name (argument cls)
        """
        obj_l = []
        obj_d = {}
        classes = [City, State]

        if cls is not None:
            obj_l.extend(self.__session.query(cls).all())
        else:
            for clas in classes:
                obj_l.extend([obj for obj in self.__session.query(clas).all()])
            obj_d = {f"{obj.__class__.__name__}.{obj.id}":
                     obj for obj in obj_l}
        return obj_d

    def new(self, obj):
        """add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commit the object to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete the object to the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create current database session
        """
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """call remove() method on the priv session attribute(self.__session)
        """
        self.__session.remove()
