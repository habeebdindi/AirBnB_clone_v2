#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    """ Add the relationship for DBStorage """
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    """ For FileStorage, define a getter attribute for cities """
    @property
    def cities(self):
        return [city for city in models.storage.all(City).values() if
                city.state_id == self.id]
