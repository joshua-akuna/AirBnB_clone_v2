#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column(String(128), nullable=True)
    state_id = Column(String(60), nullable=True, primary_key=True)

    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
