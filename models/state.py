#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Add the relationship for DBStorage
    cities = relationship("City", cascade="all, delete-orphan",
                          back_populates="state")

    # For FileStorage, define a getter attribute for cities
    @property
    def cities(self):
        return [city for city in self.__FileStorage() if city.state_id ==
                self.id]
