#!/usr/bin/python3
""" State Module for HBNB project """

from models.city import City
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete,delete-orphan")
else:
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            """return city to state"""
            from models import storage
            list_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
