#!/usr/bin/python3
"""Defines a City class and an instance Base=declarative_base()"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """cities MySQL database

    __tablename__ (string): the database name
    id (sqlalchemy.Integer): the city id
    name (sqlalchemy.String): the city name
    state_id (sqlalchemy.String): the state id of the city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
