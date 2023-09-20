#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
import shlex
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=True)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        all_objs = models.storage.all()
        new_list = []
        res = []

        for key in all_objs:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                new_list.append(all_objs[key])

        for item in new_list:
            if item.state_id == self.id:
                result.append(item)

        return result
