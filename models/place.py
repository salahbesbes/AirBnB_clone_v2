#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table('hbnb_dev_db', Base.metadata,
                      Column('places',
                             String(60),
                             ForeignKey('places.id'),
                             nullable=False),
                      Column('amenities',
                             String(60),
                             ForeignKey('amenities.id'),
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60),
                     ForeignKey("cities.id"),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id"),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    reviews = relationship('Review',
                           backref='place',
                           cascade='all, delete-orphan')
    amenities = relationship('Amenity',
                             secondary=place_amenity,
                             viewonly=False)
    amenity_ids = []

    if models.storage_type != 'db':
        @property
        def amenities(self):
            """ Get Linked Amenities"""
            amenitylist = []
            for amenity in list(models.storage.all(models.Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenitylist.append(amenity)
            return amenitylist

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
