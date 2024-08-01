#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel, Base
from models import storage_t
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if storage_t == "db":
        __tablename__ = 'states'
        name = Column("name", String(128), nullable=False)
    else:
        name = ""

        @property
        def cities(self):
            """
            getter method, returns list of City objs from storage
            linked to the current State
            """
            city_list = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
