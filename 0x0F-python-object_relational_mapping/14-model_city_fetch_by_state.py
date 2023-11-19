#!/usr/bin/python3
"""
    lists all State objects from a database
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import State
    import sys
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id.asc()).all()

    for row in rows:
        print('{}: ({}) {}'.format(row[0], row[1], row[2]))

    session.close()
