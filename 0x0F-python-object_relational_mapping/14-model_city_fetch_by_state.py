#!/usr/bin/python3
"""Fetch cities by state from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_query = session.query(State).filter(State.id == city.state_id)
        state_name = state_query.first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
