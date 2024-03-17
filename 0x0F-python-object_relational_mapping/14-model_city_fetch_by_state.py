#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_6_usa"""

from model_city import City
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for c, s in session.query(City, State)\
            .filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close
