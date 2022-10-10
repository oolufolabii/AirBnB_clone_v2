#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cities_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_state.append(value)
            return cities_state
