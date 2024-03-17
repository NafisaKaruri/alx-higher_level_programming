#!/usr/bin/python3
"""Lists the State object with the name passed \
as argrument from the database hbtn_0e_6_usa"""

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
    state = session.query(State).filter(State.name.ilike(argv[4])).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close
