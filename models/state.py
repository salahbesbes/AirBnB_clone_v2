#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
    cities = relationship('City',
                          backref='state',
                          cascade='all, delete-orphan')

    if models.storage_type != "db":
        @property
        def cities(self):
            """Get a list of all Cities"""
            citieslist = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    citieslist.append(city)
            return citieslist

