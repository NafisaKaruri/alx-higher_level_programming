#!/usr/bin/python3
"""Defines a State class and an instance Base=declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """states MySQL database

    __tablename__ (string): the database name
    id (sqlalchemy.Integer): the state id
    name (sqlalchemy.String): the state name"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
