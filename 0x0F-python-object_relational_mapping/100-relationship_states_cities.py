#!/usr/bin/python3
"""Adds the State 'Louisiana' to the database hbtn_0e_6_usa"""

from model_state import Base, State
from relationship_state import State
from relationship_city import Base, City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    city = City(name="San Fraancisco", state=State(name="California"))
    session.add(city)
    session.commit()
    session.close
