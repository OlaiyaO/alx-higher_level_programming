#!/usr/bin/python3
"""List all City objects with associated State"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
