#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", cascade="all, delete-orphan",
                           backref="place")
    amenity = relationship("Amenity", secondary="place_amenity",
                           backref="place", viewonly=False)

    @property
    def reviews(self):
        """returns list of review instances
        """
        return [review for review in models.storage.all(Review).values() if
                review.place_id == self.id]

    @property
    def amenities(self):
        """ Getter method for amenities attribute """
        return [amenity for amenity in models.storage.all(Amenity).values() if
                amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity_obj):
        """ Setter method for amenities attribute """
        if isinstance(amenity_obj, Amenity):
            self.amenity_ids.append(amenity_obj.id)
