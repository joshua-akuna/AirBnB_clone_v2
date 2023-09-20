#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
               primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
               primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns a list of reviews id
            """
            all_objs = models.storage.all()
            temp = []
            result = []

            for key in all_objs:
                if key.startswith("Review"):
                    temp.append(all_objs[key])

            for item in temp:
                if item.place_id == self.id:
                    result.append(item)

            return (result)

        @property
        def amenities(self):
            """returns the list of Amenity instances
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """Appends an Amenity id to the attribute amenity_ids
            """
            if type(obj) == "Amenity" and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
