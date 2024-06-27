#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from models import storage_t

if storage_t == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    __tablename__ = "places"

    if storage_t == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place_amenities", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenities = []

    @property
    def reviews(self):
        from models import storage
        all_r = storage.all('Review')
        return [r for r in all_r.values() if review.place_id == self.id]

    @property
    def amenities(self):
        """Return list of Amenity instances"""
        from models import storage
        return [storage.get(Amenity, id) for id in self.amenity_ids]

    @amenities.setter
    def amenities(self, value):
        """Add an Amenity.id to the list of amenities"""
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)
